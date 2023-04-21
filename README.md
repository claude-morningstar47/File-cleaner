# File-cleaner

Script de gestion de fichiers ``Rechercher et supprimer des fichiers avec extension``

Ce script Python permet aux utilisateurs de rechercher et de supprimer des fichiers avec une extension spécifiée dans un répertoire spécifié. Il permet également aux utilisateurs d'afficher le contenu de chaque fichier avec l'extension spécifiée.

**Installation et utilisation**
Pour utiliser ce script, suivez ces instructions :

1. Clonez ce référentiel sur votre ordinateur local.
```
git clone https://github.com/Claude-Mops47/File-cleaner.git
```

2. Installez les dépendances requises en exécutant `pip install -r requirements.txt.`

Accédez au répertoire contenant le script dans la ligne de commande.
Exécutez le script en utilisant `python main.py <répertoire> <extension> --option(s).`
Où <répertoire> est le chemin d'accès au répertoire dans lequel vous souhaitez effectuer la recherche, <extension> est l'extension de fichier que vous souhaitez rechercher (sans le point) et --option(s) est une ou plusieurs des options suivantes :

- `-d ou --delete` : supprime tous les fichiers avec l'extension spécifiée dans le dossier spécifié.
- `-c ou --confirm` : demande confirmation avant de supprimer ou afficher le contenu de chaque fichier.
- `-p ou --display` : affiche le contenu de chaque fichier avec l'extension spécifiée dans le dossier spécifié.
- `-s ou --sort-order` : définit l'ordre de tri de la liste des fichiers. Les options possibles sont `asc` pour un tri alphabétique croissant, `desc` pour un tri alphabétique décroissant et `random` pour un tri aléatoire.
  
Par exemple, 
- pour rechercher tous les fichiers texte du dossier Documents et afficher leur contenu, exécutez la commande suivante :
``python file_cleaner.py /Users/username/Documents txt -p``
- Pour supprimer tous les fichiers avec l'extension .txt dans le dossier Documents :
``python file_cleaner.py /Users/username/Documents txt -d``
- Pour afficher le contenu de tous les fichiers avec l'extension .txt dans le dossier Documents, triés par ordre alphabétique décroissant :
``python file_cleaner.py /Users/username/Documents txt -p -s desc``

**Dépendances**
Ce script nécessite les bibliothèques Python suivantes :

Cliquez sur
os
send2trash
pathlib
aléatoire
  
Ceux-ci peuvent être installés à l'aide de pip. Pour les installer, exécutez la commande suivante :

``pip install -r exigences.txt``

**Contribuant**
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir un problème ou à soumettre une pull request si vous avez des suggestions ou des améliorations.

Assurez-vous de tester soigneusement vos modifications avant de soumettre une demande d'extraction.
  
**Auteur**
Ce script a été créé par `Claude-Mops47`.


**Licence**
Ce projet est sous licence MIT. Voir LICENSE.md pour plus d'informations.
