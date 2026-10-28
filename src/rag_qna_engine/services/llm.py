import openai
import os


def generate_questions(context: str, n: int = 3) -> list:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"""Given the following context, generate {n} questions a student could be asked to test their understanding.\nContext:\n{context}"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip().split("\n")


def evaluate_answer(question: str, answer: str, context: str) -> dict:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"""Given the context, evaluate if the answer to the question is correct.\nContext: {context}\nQuestion: {question}\nAnswer: {answer}\nRespond with 'Correct' or 'Incorrect' and a short feedback."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    content = response["choices"][0]["message"]["content"].strip()
    is_correct = content.lower().startswith("correct")
    return {"is_correct": is_correct, "feedback": content}
