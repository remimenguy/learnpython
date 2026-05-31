#exo1
movie_title = "cars"
release_year = 2014
duration_minutes = 250
is_watched = True
print(movie_title, release_year, duration_minutes, is_watched)
#exo 2
a = "hello"
b = 1.2
c = True
d = 34


print(type(a))
print(type(b))
print(type(c))
print(type(d))

#exo3
first_name = "remi"
favorite_movie = "iron man"
favorite_year = 2011

print(f"Bonjour {first_name}, je suis {favorite_movie}, née en {favorite_year}")

#exo4

me = True

if me:
    print(f"salut {first_name}")
else:
    print("no")

year = 2039

if year == 2039:
    print("hello")
else:
    print("nooooo")


age = 14

ask = int(input("Quelle est mon age ?"))

if ask == age:
    print("Bravo tu as trouvé")
elif ask < age:
    print("non, trop bas")
elif ask > age:
    print("trop haut")
else:
    print("choisi un nombre")