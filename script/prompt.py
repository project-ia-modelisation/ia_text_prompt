import asyncio
from modules.textual_ai import TextualAI
from modules.modeling_ai_client import ModelingAIClient

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

async def main():
    print("🚀 Démarrage de l'IA textuelle...")
    textual_ai = TextualAI()
    modeling_client = ModelingAIClient()

    while True:
        prompt = input("💬 Entrez votre prompt (ou 'exit' pour quitter) : ")
        if prompt.lower() == 'exit':
            break

        response = await textual_ai.generate_response(prompt)
        print(f"🧠 IA Textuelle : {response}")

        correction = await modeling_client.send_and_receive(response)
        print(f"🎨 IA 3D : {correction}")

        textual_ai.learn_from_feedback(correction)

if __name__ == "__main__":
    asyncio.run(main())
    client = ModelingAIClient("http://localhost:5000")

    status = client.get_status()
    print(f"Statut de l'IA : {status}")

    if status == "En ligne":
        result = client.send_prompt("Génère une sphère avec un rayon de 5")
        if result:
            print(f"✅ Réponse de l'IA : {result}")
        else:
            print("❌ Aucune réponse reçue.")
