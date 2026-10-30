"""
Layer 1 — Plain LLM, no special setup.

This is version 1 of your evaluation baseline (Section 7 of the brief).
Run this first, then compare against your prompted and RAG versions.
"""

import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL = "claude-opus-4-5"  # change to compare models; try at least two
SYSTEM_PROMPT = "You are a helpful assistant."  # plain, no project-specific framing


def ask(question: str) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


if __name__ == "__main__":
    # Load your evaluation questions from src/evaluation/questions.md
    # and run each one here, logging the output for comparison.
    sample = "TODO: replace with one of your evaluation questions"
    print(f"Model: {MODEL}")
    print(f"Q: {sample}")
    print(f"A: {ask(sample)}")
