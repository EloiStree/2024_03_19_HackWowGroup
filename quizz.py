## python quizz.py chemin_vers_votre_fichier_texte.txt chemin_vers_votre_fichier_sortie.txt --api_key VOTRE_CLE_API

import argparse
from openai import OpenAI

# Fonction pour obtenir les arguments de la ligne de commande
def obtenir_arguments():
    parser = argparse.ArgumentParser(description="Script de création de quiz à partir d'un texte")
    parser.add_argument("fichier_texte", help="Chemin du fichier texte contenant le contenu du quiz")
    parser.add_argument("fichier_sortie", help="Chemin du fichier de sortie pour le quiz généré")
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

    # Générer le quiz en utilisant le contenu du fichier texte
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "Tu es un créateur de Quizz / prof qui veut verifier que des eleves on bien lu et compris un texte "},
            {"role": "user", "content": "Composez un quiz contenant entre 5 et 10 questions à choix multiples (QCM), où chaque question présente 4 options de réponse parmi lesquelles une seule est correcte. À la fin du quiz, veuillez répertorier les réponses correctes pour que le professeur puisse les consulter. " + prompt}
        ]
    )

    # Extraire le contenu du quiz généré
    message = completion.choices[0].message.content

    # Écrire le quiz dans le fichier de sortie spécifié
    with open(args.fichier_sortie, "w") as output_file:
        output_file.write(message)

if __name__ == "__main__":
    main()
