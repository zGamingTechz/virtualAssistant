# Example: reuse your existing OpenAI setup
from openai import OpenAI


def chat(message):
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    completion = client.chat.completions.create(
      model="TheBloke/Llama-2-7B-Chat-GGUF",
      messages=[
        {"role": "user", "content": message}
      ],
      temperature=0.7,
    )

    return completion.choices[0].message.content
