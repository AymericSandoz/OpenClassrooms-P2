# Description générale du projet

Projet Django réalisé dans le cadre d'une recherche d'alternance.
Application permettant de lister les corps célestes qui passent à proximité de la terre durant une période donnée.

## Installation et démarrage

Cloner le dépot Github

```
git clone https://github.com/AymericSandoz/asteroid_list.git
```

Charger l'application

```
cd asteroid_list
```

Créer puis charger un environnement virtuel

```
python -m venv env

env/Scripts/activate
```

Installer les packages nécéssaires

```
pip install -r requirements.txt
```

Lancer le serveur sur votre marchine

```
cd merchex

python manage.py runserver
```

Ouvrir un navigateur à l'adresse indiqué sur votre console suivi de home/ qui correspond à la page d'acceuil.

```
cd merchex

python manage.py runserver
```

## Outils utilisés

####

- Django
- Python
- Javascript
- Sass

## Option

La chargement de la date du prochain passage près de la terre de tous les astéroïdes n'est pas activé d'office. Cette option a été remplacé par un bouton permettant, au clic, de voir le prochain passage près de la terre d'un astéroïde donné. L'objectif étant d'éviter un temps de chargement trop long.

Pour réactiver cette option, il faut :

####

- Ouvrir le fichier view.py - asteroid_list\merchex\listings>
- Enlever les commentaires des lignes 22 à 44 et de la ligne 74.

- Ouvrir le fichier asteroids.html - asteroid_list\merchex\listings\templates\listings>
- Enlever les commentaires des lignes 36 à 40.
- Supprimez les lignes 43 à 45.

## Organisation

####

- asteroid.html --> Fichier affichant les 5 derniers passages d'un astéroïdes près de la terre.
- asteroids.html --> Fichier affichant la liste des astéroïdes passant près de la terre durant une période donnée.
- base.html --> fichier html de base.
- home.html --> page d'acceuil permettant à l'utilisateur de saisir une date d'entrée et une date.
- info.html --> Courte description du contexte du projet.
