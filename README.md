# File-cleaner

Script de gestion de fichiers

Ce script Python permet de gérer les fichiers dans un dossier spécifié. Il permet de trouver tous les fichiers ayant une extension donnée, de les supprimer ou d'afficher leur contenu.

**Prérequis**

- Python 3.x

**Installation**

1. Clonez le dépôt Git ou téléchargez les fichiers sur votre ordinateur.
2. Installez les dépendances en exécutant la commande suivante :
```python
pip install send2trash typer
```

**Utilisation**
Pour exécuter le script, utilisez la commande suivante :
`python file_cleaner.py [OPTIONS] DIRECTORY EXTENSION`

**Options**

- -d, --delete : Supprime tous les fichiers ayant l'extension spécifiée dans le dossier spécifié.
- -c, --confirm : Demande une confirmation avant de supprimer chaque fichier.
- -p, --display : Affiche le contenu de chaque fichier ayant l'extension spécifiée dans le dossier spécifié.
- -s, --sort-order : Définit l'ordre de tri des fichiers. Les options possibles sont asc pour un tri alphabétique croissant, desc pour un tri alphabétique décroissant et random pour un tri aléatoire.

**Exemples**

- Pour supprimer tous les fichiers avec l'extension .txt dans le dossier Documents :
  `python file_cleaner.py -d Documents txt`
- Pour afficher le contenu de tous les fichiers avec l'extension .md dans le dossier courant :
  `python file_cleaner.py -p . md`
- Pour afficher le contenu de tous les fichiers avec l'extension .txt dans le dossier Documents, triés par ordre alphabétique décroissant :
  `python file_cleaner.py -p -s desc Documents txt`

**Auteur**
Ce script a été créé par `Claude-Mops47`.
