import requests

class TextualAI:
    def __init__(self, api_url):
        self.api_url = api_url

    def generate_prompt(self, user_input):
        return f"Créer un modèle 3D basé sur : {user_input}"

    def send_prompt_to_modeling_ai(self, prompt):
        try:
            response = requests.post(f"{self.api_url}/generate", json={"prompt": prompt})
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Erreur HTTP {response.status_code} : {response.text}")
                return None
        except Exception as e:
            print(f"❌ Erreur lors de l'envoi du prompt : {e}")
            return None

    def interact(self):
        print("💬 Bienvenue dans l'IA textuelle pour la modélisation 3D ! Tapez 'exit' pour quitter.")
        while True:
            user_input = input("👉 Entrez votre description : ")
            if user_input.lower() == 'exit':
                break

            prompt = self.generate_prompt(user_input)
            print(f"🚀 Prompt généré : {prompt}")

            result = self.send_prompt_to_modeling_ai(prompt)
            if result:
                print("✅ Modèle généré avec succès !")
                print(f"🖼️ Détails de l'IA de modélisation : {result.get('model_info', 'Aucune info')}")
            else:
                print("❌ Échec de la génération du modèle.")
