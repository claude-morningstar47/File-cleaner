import click
import os
import send2trash
from pathlib import Path
import random


def find_files_with_extension(directory: Path, extension: str, sort_order: str = 'asc') -> tuple:
    """Retourne une liste des fichiers avec l'extension donnée dans le répertoire donné, ainsi que le chemin du dossier."""
    if not directory.is_dir():
        raise click.BadParameter(f"Le dossier '{directory}' n'existe pas.")

    # Vérifier que l'extension est valide
    if not extension:
        raise click.BadParameter("L'extension doit être spécifiée.")
    elif not extension.startswith("."):
        extension = f".{extension}"

    # Récupérer la liste des noms de fichiers avec l'extension donnée
    files = [entry.name for entry in os.scandir(
        directory) if entry.is_file() and entry.name.endswith(extension)]
    if not files:
        raise click.BadParameter(
            f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

    # Trier la liste selon l'ordre alphabétique croissant ou décroissant
    if sort_order == "asc":
        files.sort()
    elif sort_order == "desc":
        files.sort(reverse=True)
    elif sort_order == "random":
        random.shuffle(files)
    else:
        raise click.BadParameter(
            "L'ordre de tri doit être 'asc', 'desc' ou 'random'.")
    return directory, files


def delete_file(directory_path: Path, file: str) -> bool:
    """Supprime un fichier."""
    chemin = directory_path.joinpath(file)
// nomp
    if not os.path.exists(chemin):
        click.echo(f"Le fichier '{file}' n'existe pas.")
        return False

    try:
        send2trash.send2trash(chemin)
        click.echo(f"Le fichier '{file}' a été envoyé dans la corbeille.")
        return True
    except Exception as e:
        click.echo(
            f"Erreur lors de la mise a la corbeille du fichier '{file}': {e}")
        return False


def delete_files(directory_path: Path, files: list[str], confirm: bool = False) -> None:
    """Supprime tous les fichiers de la liste."""
    # Afficher une liste des fichiers à supprimer
    click.echo("Fichiers à supprimer :")
    for file in files:
        path = Path(file)
        if confirm:
            prompt = input(
                f"Voulez-vous supprimer le fichier '{path}' ? [O/n] ")
            if prompt.lower() != "o":
                continue
        delete_file(directory_path, path)


def display_files_content(directory_path: Path, files: list[str], confirm: bool = False) -> None:
    """Affiche la liste des fichiers dans le dossier et permet de confirmer l'ouverture du contenu de chaque fichier."""
    click.echo(f"Liste des fichiers dans le dossier '{directory_path}':")
    click.echo(f"* Il existe '{len(files)}' fichiers dans ce répertoire. *")
    click.echo("---------------------------------------------------")

    if len(files) > 10:
        num_cols = 4
        num_rows, remainder = divmod(len(files), num_cols)
        if remainder > 0:
            num_rows += 1

        for i in range(num_rows):
            cols = [files[j] for j in range(i, len(files), num_rows)]
            col_text = "{:20s}" * len(cols)
            click.echo(col_text.format(*cols))

    else:
        for file in files:
            click.echo(f"- {file}")

    if confirm:
        for file in files:
            if confirm:
                user_input = input(
                    f"Voulez-vous afficher le contenu du fichier '{file}' ? (Oui/Non) ")
                if user_input.lower() not in ['oui', 'o']:
                    continue

                # Afficher le contenu du fichier
                path = directory_path.joinpath(file)
                click.echo(f"Contenu du fichier '{file}' :")
                try:
                    with open(path, 'r') as f:
                        content = f.read()
                        click.echo(content)
                except Exception as e:
                    click.echo(
                        f"Erreur lors de la lecture du fichier '{file}': {e}")


@click.command()
@click.argument('directory')
@click.argument('extension')
@click.option('-d', '--delete', is_flag=True, help='Supprime tous les fichiers.')
@click.option('-c', '--confirm', is_flag=True, help='Demande de confirmation.')
@click.option('-p', '--display', is_flag=True, help='Affiche les contenus.')
@click.option('-s', '--sort-order', type=click.Choice(['asc', 'desc', 'random']), default='asc', help='Définit l\'ordre de tri des fichiers.')
def main(directory: str, extension: str, delete: bool, confirm: bool, display: bool, sort_order: str) -> None:
    """
    Fonction principale.

    --delete : Supprime tous les fichiers.\n
    --confirm : Demande de confirmation.\n
    --display : Affiche les contenus.\n
    --sort-order : Définit l'ordre de tri des fichiers.
    """
    directory_path = Path(directory)
    directory, files = find_files_with_extension(
        directory_path, extension, sort_order)

    if delete:
        delete_files(directory_path, files, confirm)
    elif display:
        display_files_content(directory_path, files, confirm)
    else:
        click.echo(
            "Aucune option sélectionnée. Veuillez utiliser l'une des options suivantes :")
        click.echo(
            "--delete : Supprime tous les fichiers ayant l'extension spécifiée dans le dossier spécifié.")
        click.echo(
            "--confirm : Demande une confirmation avant de supprimer chaque fichier.")
        click.echo(
            "--display : Affiche le contenu de chaque fichier ayant l'extension spécifiée dans le dossier spécifié.")
        click.echo("--sort-order : Définit l'ordre de tri des fichiers. Les options possibles sont asc pour un tri alphabétique croissant, desc pour un tri alphabétique décroissant et random pour un tri aléatoire.")


if __name__ == "__main__":
    main()
