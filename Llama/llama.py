import logging
from llama_cpp import Llama
from promptData import save_to_json 

logging.basicConfig(level=logging.DEBUG)

modele_path = "C:/Users/noala/.llama/checkpoints/Llama3.1-8B-Instruct/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf"

try:
    llm = Llama(model_path=modele_path)
    logging.info(f"Le modèle a été chargé à partir de {modele_path}")
except Exception as e:
    logging.error(f"Erreur lors du chargement du modèle : {e}")
    exit(1)

# Prompt d'entrée
prompt = "Quel est le sens de la vie ?"

try:
    output = llm.create_completion(
        prompt,
        max_tokens=2048,
        temperature=0.6
    )
    logging.info("Complétion générée avec succès")
except Exception as e:
    logging.error(f"Erreur lors de la création de la complétion : {e}")
    exit(1)

# Vérifier que la réponse est bien structurée
try:
    response_text = output["choices"][0]["text"].strip()
    if not response_text:
        raise ValueError("La réponse est vide.")
    logging.info(f"Réponse générée : {response_text}")
except KeyError as e:
    logging.error(f"Clé manquante dans la réponse : {e}")
    exit(1)
except ValueError as e:
    logging.error(e)
    exit(1)

# Construire la structure JSON
output_data = {
    "prompt": prompt,
    "response": response_text,
    "model": modele_path,
    "parameters": {
        "max_tokens": 1024,
        "temperature": 0.3
    }
}

save_to_json(output_data, "data.json")

print(f"Réponse générée et sauvegardée dans data.json")
