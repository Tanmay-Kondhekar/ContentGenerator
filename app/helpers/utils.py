from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from sqlalchemy.orm import Session
import threading
from app.helpers import models, crud 
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
API_KEY = os.getenv("HF_KEY")

client = InferenceClient(
    provider="fireworks-ai",
    api_key=API_KEY,
)

seamaphore = threading.Semaphore(5)

def generate_content(db: Session, topic: str)->str:
    with seamaphore:
        search_term = crud.create_search_term(db, topic)
        if not search_term:
            search_term = crud.create_search_term(db, topic)
        
        response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"Write a 100 word article about {topic}."
            }
        ],
        )

        generate_text = response.choices[0].message.content.strip()
        crud.create_generated_content(db, generate_text, search_term.id)
        return generate_text
    
def analyze_content(db: Session, content: str) -> str:
    with seamaphore:
        search_term = crud.get_search_term(db, content)
        if not search_term:
            search_term = crud.create_search_term(db, content)

        readability = get_readability_score(content)
        sentiment = get_sentiment_score(content)

        crud.create_sentiment_analysis(db, readability, sentiment, search_term.id)

        return readability, sentiment

def get_readability_score(content: str) -> str:
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"Analyze the readability of the following text: {content}. Provide a Just a score, in a single line."
            }
        ],
        )
    return response.choices[0].message.content.strip()

def get_sentiment_score(content: str) -> str:
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"Analyze the sentiment of the following text: {content}. Provide a Just a score, in a single line."
            }
        ],
        )
    return response.choices[0].message.content.strip()