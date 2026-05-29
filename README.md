# Exercices Python — Bases depuis zéro

Objectif : apprendre les bases de Python progressivement, sans copier-coller de solution complète.  
Thème utilisé : films à regarder.

---

## Exercice 1 — Variables simples

Dans `main.py`, crée quatre variables :

- `movie_title`
- `release_year`
- `duration_minutes`
- `is_watched`

Avec les valeurs de ton choix.

Ensuite, affiche-les avec `print`.

### Notions travaillées

- créer une variable
- utiliser `str`, `int`, `bool`
- afficher une valeur avec `print`

---

## Exercice 2 — Les types

Dans `main.py`, crée une variable de chaque type :

- un texte : `str`
- un entier : `int`
- un nombre décimal : `float`
- un booléen : `bool`

Ensuite, affiche le type de chaque variable avec :

```python
type(...)
```

et :

```python
print(...)
```

### Résultat attendu dans le terminal

Tu dois obtenir des lignes du genre :

```txt
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### Notions travaillées

- comprendre les types de base
- utiliser `type`
- distinguer `1.2` de `1,2`

Attention : en Python, un nombre décimal s’écrit avec un point :

```python
price = 1.2
```

Pas avec une virgule :

```python
price = 1,2
```

---

## Exercice 3 — Les f-strings

Crée trois variables :

- `first_name`
- `favorite_movie`
- `favorite_year`

Avec les valeurs de ton choix.

Ensuite, affiche une phrase en utilisant une f-string.

### Exemple de phrase attendue

```txt
Bonjour Thomas, ton film préféré est Interstellar, sorti en 2014.
```

### Contraintes

- utiliser `f"..."`
- mettre les variables entre `{}`
- ne pas utiliser `+` pour coller les textes

### Notions travaillées

- insérer des variables dans une phrase
- utiliser une f-string
- produire un affichage lisible

---

## Exercice 4 — Conditions, `and` et `not`

Crée deux variables :

- `rating`
- `is_watched`

Exemple de sens :

- `rating` = note du film
- `is_watched` = est-ce que le film a déjà été vu ?

Ensuite, écris une condition qui fait ceci :

```txt
Si le film est déjà vu ET que la note est supérieure ou égale à 8 :
    afficher "Excellent film déjà vu"

Sinon si le film n’est pas encore vu :
    afficher "À regarder"

Sinon :
    afficher "Film moyen ou déjà vu"
```

### Contraintes

Tu dois utiliser :

- `if`
- `elif`
- `else`
- `and`
- `not`

### Rappels

`and` veut dire : les deux conditions doivent être vraies.

```txt
True and True   → True
True and False  → False
False and True  → False
False and False → False
```

`not` inverse une valeur booléenne.

```txt
not True  → False
not False → True
```

Donc :

```python
if is_watched:
```

veut dire :

```txt
si le film est vu
```

Et :

```python
if not is_watched:
```

veut dire :

```txt
si le film n’est pas vu
```

### Notions travaillées

- conditions
- booléens
- opérateurs logiques
- indentation Python

---

## Exercice 5 — Les listes

Crée une liste appelée :

```python
movies
```

Elle doit contenir au moins 4 films.

Ensuite :

1. affiche toute la liste
2. affiche uniquement le premier film
3. affiche uniquement le dernier film
4. ajoute un nouveau film avec `append`
5. affiche le nombre total de films avec `len`

### Rappel

Le premier élément d’une liste est à l’index `0`.

```python
movies[0]
```

Le dernier élément peut être récupéré avec :

```python
movies[-1]
```

### Notions travaillées

- créer une liste
- accéder à un élément
- ajouter un élément
- compter les éléments

---

## Exercice 6 — Les boucles

Avec ta liste de films, fais une boucle qui affiche chaque film sous cette forme :

```txt
Film : Interstellar
Film : Gladiator
Film : Inception
```

Tu dois utiliser une boucle `for`.

### Structure à comprendre

```python
for element in liste:
    ...
```

### Notions travaillées

- parcourir une liste
- répéter une action
- comprendre l’indentation dans une boucle

---

## Exercice 7 — Les dictionnaires

Crée un dictionnaire appelé :

```python
movie
```

Avec ces clés :

- `title`
- `year`
- `duration`
- `watched`

Ensuite :

1. affiche le titre
2. affiche l’année
3. modifie `watched`
4. ajoute une clé `rating`
5. affiche le dictionnaire complet

### Rappel

Un dictionnaire Python ressemble à un objet JavaScript.

```python
movie = {
    "title": "Interstellar",
    "year": 2014,
    "watched": True
}
```

Accéder à une valeur :

```python
movie["title"]
```

Modifier une valeur :

```python
movie["watched"] = False
```

Ajouter une valeur :

```python
movie["rating"] = 8.7
```

### Notions travaillées

- dictionnaires
- clés / valeurs
- lecture, modification et ajout de données

---

## Exercice 8 — Liste de dictionnaires

Crée une liste appelée :

```python
movies
```

Elle doit contenir 3 dictionnaires.

Chaque dictionnaire représente un film avec :

- `title`
- `year`
- `watched`

Ensuite, fais une boucle qui affiche chaque film sous cette forme :

```txt
Interstellar - 2014
Gladiator - 2000
Dune - 2021
```

Tu peux utiliser tes propres films.

### Notions travaillées

- liste de dictionnaires
- structure de données proche d’une base de données
- boucle sur des objets

---

## Exercice 9 — Fonctions

Crée une fonction appelée :

```python
display_movie
```

Elle doit recevoir un dictionnaire représentant un film.

Elle doit afficher :

```txt
Titre - Année
```

Ensuite, appelle cette fonction pour chaque film de ta liste.

Tu dois donc combiner :

- fonction
- boucle
- dictionnaire
- liste

### Rappel

Une fonction se définit avec :

```python
def function_name():
    ...
```

Une fonction avec un paramètre :

```python
def function_name(parameter):
    ...
```

### Notions travaillées

- créer une fonction
- passer un paramètre
- réutiliser du code

---

## Exercice 10 — Annotations de type

Reprends ta fonction `display_movie` et ajoute des annotations de type.

Pour l’instant, tu peux utiliser :

```python
dict
```

comme type simple.

### Forme attendue

```python
def nom_de_fonction(parametre: dict) -> None:
    ...
```

`None` veut dire que la fonction ne retourne rien.

### Notions travaillées

- annotations de type
- lisibilité du code
- structure plus professionnelle

---

# Objectif final de cette série

Composer un `main.py` qui fait tout ça, dans cet ordre :

1. créer une liste vide de films
2. créer une fonction pour ajouter un film
3. créer une fonction pour afficher un film
4. créer une fonction pour afficher tous les films
5. ajouter 3 films
6. afficher tous les films

## Contraintes finales

- chaque film doit être un dictionnaire
- chaque film doit avoir `title`, `year`, `watched`
- la liste doit contenir plusieurs dictionnaires
- utiliser au moins une boucle `for`
- utiliser au moins deux fonctions
- utiliser des f-strings
- ne pas copier-coller une solution complète

---

# Commande pour lancer ton fichier

Dans le terminal, depuis ton dossier projet :

```bash
python main.py
```
