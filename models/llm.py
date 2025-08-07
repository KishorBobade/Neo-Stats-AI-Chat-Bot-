from openai import OpenAI
from config.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt, mode="concise"):
    style = "Keep it short and summarized." if mode == "concise" else "Provide a detailed and informative response."
    full_prompt = f"{prompt}\n\n{style}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response.choices[0].message.content
