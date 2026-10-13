import json
import os
import subprocess
from html.parser import HTMLParser
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import Request, urlopen

from openai import OpenAI


class DuckDuckGoResultsParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.results = []
        self._capture = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()
        if tag == "a" and "result__a" in classes:
            self.results.append(
                {"title": "", "url": self._result_url(attributes.get("href", ""))}
            )
            self._capture = "title"
        elif "result__snippet" in classes and self.results:
            self._capture = "snippet"
            self.results[-1]["snippet"] = ""

    def handle_endtag(self, tag):
        if tag == "a" and self._capture == "title":
            self._capture = None
        elif self._capture == "snippet" and tag in {"a", "div"}:
            self._capture = None

    def handle_data(self, data):
        if self._capture == "title" and self.results:
            self.results[-1]["title"] += data
        elif self._capture == "snippet" and self.results:
            self.results[-1]["snippet"] += data

    @staticmethod
    def _result_url(href):
        if href.startswith("//duckduckgo.com/l/"):
            return parse_qs(urlsplit(href).query).get("uddg", [href])[0]
        return href


def search_web(query):
    search_url = "https://html.duckduckgo.com/html/?" + urlencode({"q": query})
    request = Request(
        search_url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; LearnPython/1.0)"},
    )
    with urlopen(request, timeout=15) as response:
        page = response.read().decode(
            response.headers.get_content_charset() or "utf-8", errors="replace"
        )

    parser = DuckDuckGoResultsParser()
    parser.feed(page)
    return parser.results[:5]


def read_multiline_prompt():
    print("Enter your prompt. Finish by entering END on its own line:")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            return "\n".join(lines).strip()
        lines.append(line)


api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY environment variable is not set.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "open_chrome",
            "description": "Open the Google Chrome app on the user's Mac.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": (
                "Search the public web for current information and sources. "
                "Use when the user requests up-to-date facts or web research."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A concise web search query.",
                    }
                },
                "required": ["query"],
                "additionalProperties": False,
            },
        },
    },
]

messages = [
    {
        "role": "system",
        "content": (
            "Answer the user's request helpfully. Use search_web for current "
            "information or web research, and cite the returned source URLs. "
            "Use open_chrome only when it is relevant."
        ),
    },
    {"role": "user", "content": read_multiline_prompt()},
]

while True:
    response = client.chat.completions.create(
        messages=messages,
        model="openai/gpt-oss-120b",
        tools=tools,
        tool_choice="auto",
    )
    message = response.choices[0].message

    if not message.tool_calls:
        print(message.content or "")
        break

    messages.append(message)
    for tool_call in message.tool_calls:
        arguments = json.loads(tool_call.function.arguments or "{}")
        if tool_call.function.name == "open_chrome":
            subprocess.run(["open", "-a", "Google Chrome"], check=True)
            result = "Google Chrome was opened successfully."
        elif tool_call.function.name == "search_web":
            result = json.dumps(search_web(arguments["query"]), ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported tool: {tool_call.function.name}")

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": result,
            }
        )
