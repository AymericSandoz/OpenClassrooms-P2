# Description générale du projet

Projet réalisé dans le cadre de la formation Développeur d'applications python.
Application python (un scraper), capable d'extraire les informations de la librairie en ligne http://books.toscrape.com/.

## Installation et démarrage

Cloner le dépot Github

```
git clone https://github.com/AymericSandoz/OpenClassrooms-P2.git
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

## Exécution

Ouvrez un terminal de commande au niveau du projet puis éxécutez la commande :

```
python index.py
```

ou

```
python index2.py
```

## Outils utilisés

####

- Python

## Options

Le fichier index2 permet de générer un fichier xlxs possédant une feuille par catégorie de livres.
Le fichier index permet de générer autant de fichiers csv qu'il y a de catégories de livres.
