movie_title = "itron"
release_year = 2019
duration_minutes = 123
duration_hour = duration_minutes/60
is_watched = True
rating = 3.9
name = "Remi"

print(f"Bonjour {name}, le film {movie_title} est sorti en {release_year} et dure {duration_hour} heures")
print(f"Note : {rating}/5")

#pas besoin du type de toutes les varibale, je connais le process de toute facon
print(type(movie_title))

if is_watched and rating >= 4:
    print("Excellent film déjà vu")
elif is_watched is False:
    print(f"Je dois encore le regarder, moi, {name}")
else:
    print("Film déjà vu, mais pas exceptionnel")

#part4
devinette = int(input("Devine l année de sortie du film"))

if devinette == release_year:
    print("Bravo, bonne reponse !")
elif devinette < release_year:
    print("Trop ancien")
elif devinette > release_year:
    print("Trop recent")