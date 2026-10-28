# Example prompt templates for LLM
QUESTION_GEN_PROMPT = """
Given the following context, generate {n} questions a student could be asked to test their understanding.
Context:
{context}
"""

ANSWER_EVAL_PROMPT = """
Given the context, evaluate if the answer to the question is correct.
Context: {context}
Question: {question}
Answer: {answer}
Respond with 'Correct' or 'Incorrect' and a short feedback.
"""
