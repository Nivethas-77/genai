import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="What is Generative AI? Explain its types and real-world applications.",
    model="openai/gpt-oss-20b",
)

print(response.output_text)