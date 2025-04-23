import requests

class ModelingAIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_prompt(self, prompt):
        """
        Envoie un prompt à l'IA de modélisation et retourne la réponse.
        """
        url = f"{self.base_url}/generate"
        payload = {"prompt": prompt}

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Erreur lors de l'envoi du prompt : {e}")
            return {"error": str(e)}

    def get_status(self):
        """
        Vérifie si l'IA de modélisation est en ligne.
        """
        url = f"{self.base_url}/status"

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get("status", "Inconnu")
        except requests.RequestException as e:
            print(f"⚠️ Erreur lors de la vérification du statut : {e}")
            return "Hors ligne"
