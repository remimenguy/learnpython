import os
import subprocess

from openai import OpenAI

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
    }
]

messages = [
    {
        "role": "system",
        "content": "Answer the user's request helpfully. Use the open_chrome tool only when it is relevant.",
    },
    {"role": "user", "content": input("Enter your prompt: ")},
]

response = client.chat.completions.create(
    messages=messages,
    model="openai/gpt-oss-120b",
    tools=tools,
    tool_choice="auto",
)
message = response.choices[0].message

if not message.tool_calls:
    print(message.content or "")
    raise SystemExit(0)

messages.append(message)
for tool_call in message.tool_calls:
    if tool_call.function.name != "open_chrome":
        raise ValueError(f"Unsupported tool: {tool_call.function.name}")

    subprocess.run(["open", "-a", "Google Chrome"], check=True)
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": "Google Chrome was opened successfully.",
        }
    )

response = client.chat.completions.create(
    messages=messages,
    model="openai/gpt-oss-120b",
)
print(response.choices[0].message.content or "")
