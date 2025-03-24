import requests

class TextualAI:
    def __init__(self, modeling_ai_url):
        self.modeling_ai_url = modeling_ai_url

    def generate_prompt(self, user_input):
        return f"Créer un modèle 3D basé sur : {user_input}"

    def send_prompt_to_modeling_ai(self, prompt):
        try:
            response = requests.post(f"{self.modeling_ai_url}/generate", json={"prompt": prompt})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erreur lors de l'envoi du prompt : {e}")
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
                print("Détails :", result)
            else:
                print("❌ Échec de la génération du modèle.")

