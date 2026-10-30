"""
Layer 2 — Designed prompt (version 2 in your evaluation comparison).

Load a prompt from prompts/ and run it against your evaluation questions.
Keep a new prompt file for every version you test.
"""

import os
import anthropic
from pathlib import Path

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL = "claude-opus-4-5"
PROMPT_FILE = Path(__file__).parent / "prompts" / "v001_initial.md"


def load_system_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ask(question: str, system_prompt: str) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


if __name__ == "__main__":
    system = load_system_prompt(PROMPT_FILE)
    print(f"Loaded prompt: {PROMPT_FILE.name}")
    question = "TODO: replace with one of your evaluation questions"
    print(f"Q: {question}")
    print(f"A: {ask(question, system)}")
