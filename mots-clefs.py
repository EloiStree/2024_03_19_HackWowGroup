import argparse
from openai import OpenAI

# Fonction pour obtenir les arguments de la ligne de commande
def obtenir_arguments():
    parser = argparse.ArgumentParser(description="Script de création de liste de mots-clés et leurs définitions à partir d'un texte")
    parser.add_argument("fichier_texte", help="Chemin du fichier texte contenant le contenu pour la liste de mots-clés et définitions")
    parser.add_argument("fichier_sortie", help="Chemin du fichier de sortie pour la liste générée")
    parser.add_argument("--api_key", help="Clé API OpenAI")
    return parser.parse_args()

# Fonction principale du script
def main():
    # Obtenir les arguments de la ligne de commande
    args = obtenir_arguments()

    # Utiliser la clé API fournie ou celle stockée dans le script
    api_key = args.api_key 

    # Initialiser le client OpenAI
    client = OpenAI(api_key=api_key)

    # Ouvrir le fichier texte et lire son contenu
    with open(args.fichier_texte, 'r') as file:
        prompt = file.read()

    # Générer la liste de mots-clés et leurs définitions en utilisant le contenu du fichier texte
    completion = client.completions.create(
        engine="davinci",
        prompt="Générer une liste de mots-clés pertinents et leurs définitions grâce au texte: \n" + prompt,
        max_tokens=200
    )

    # Extraire le contenu de la liste générée
    generated_list = completion.choices[0].text.strip()

    # Écrire la liste dans le fichier de sortie spécifié
    with open(args.fichier_sortie, "w") as output_file:
        output_file.write(generated_list)

if __name__ == "__main__":
    main()
