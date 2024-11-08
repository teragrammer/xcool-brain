import requests
from dotenv import load_dotenv
import os

load_dotenv()


def generate_explanation(student, context):
    level = student.current_level
    difficulty_instruction = context["difficulty_levels"][level]

    prompt = f"""
    You are a Biology expert.
    
    Topic: {context['topic']}
    Core Concepts: {context['core_concepts']}
    Common Misconceptions: {context['common_misconceptions']}
    
    Student Level: {level}
    Instruction: {difficulty_instruction}
    
    Generate a personalized explanation
    """

    ollama_url = os.getenv("OLLAMA_URL")
    ollama_model = os.getenv("OLLAMA_MODEL")
    response = requests.post(
        ollama_url,
        json={
            "model": ollama_model,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
