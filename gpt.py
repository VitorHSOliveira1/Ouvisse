import openai
import base64


openai.api_key = "sk-...OrcA"

def ler_audiograma(caminho_imagem):
    with open(caminho_imagem, "rb") as f:
        imagem_base64 = base64.b64encode(f.read()).decode("utf-8")

    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": "Leia os valores do audiograma nesta imagem e retorne um dicionário com a perda auditiva (em dB) para cada frequência."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_base64}"}}
            ]}
        ],
        max_tokens=1000
    )

    return response.choices[0].message["content"]

resultado = ler_audiograma("caminho/para/a/imagem.jpg")
print(resultado)