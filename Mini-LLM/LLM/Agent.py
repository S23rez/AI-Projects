import requests
from google.genai._gaos.types.interactions import interaction

url = "https://datatalks.club./faq/json/courses.json"

response = requests.get(url=url)

# print(response.json())
# print(response.text)
# print(response.status_code)

"""
To use LLM to generate text
"""

# import package
import os
from google import genai
from dotenv import load_dotenv
from data import context

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

# response = client.interactions.create(
#     model="gemini-2.5-flash",
#     input="Explain what Ai is briefly"
# )
#
# print(response.output_text)


def llm(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text



user_prompt = input('Welcome to Suarez Corporation\n What would you like know: ')

prompt = f"""
    Your task is to answer the following questions related to the company
    and services based on the provided context.
    Use the context to find relevant information and provide accurate answers,
    however make research on the data given to you and elaborate the answers.
    And if you can't find any relevant context, respond with "I don't have context...
    "

    Question:{user_prompt}

    Context:{context}

"""

app = llm(prompt=prompt)
print(app)



#########################
# Vector Database
# Orchestrator
# RAG system
# Inference Layer