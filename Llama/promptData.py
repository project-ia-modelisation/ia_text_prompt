import json
import logging

def save_to_json(data, filename="data.json"):
    """
    Sauvegarde les données dans un fichier JSON.

    :param data: Dictionnaire contenant les données à sauvegarder.
    :param filename: Nom du fichier de sortie (par défaut : "data.json").
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Résultat sauvegardé dans {filename}")
    except Exception as e:
        logging.error(f"Erreur lors de l'écriture du fichier JSON : {e}")
