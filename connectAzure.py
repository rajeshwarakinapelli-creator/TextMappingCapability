import os
from openai import OpenAI

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://genaiserviceforrag.services.ai.azure.com/openai/v1")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-oss-120b")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

if not api_key:
    raise ValueError("AZURE_OPENAI_API_KEY environment variable is not set")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of India?",
        }
    ],
)

print(completion.choices[0].message)