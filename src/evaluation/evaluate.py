"""
Evaluation runner — compare all system versions against your test questions.

Usage:
    python src/evaluation/evaluate.py

Output: a Markdown table written to milestones/05_evaluation_and_reflection/results.md
"""

import os
import sys
from pathlib import Path

# Add src to path so we can import sibling modules
sys.path.insert(0, str(Path(__file__).parent.parent))

QUESTIONS = [
    # Copy your questions from questions.md here
    "TODO: question 1",
    "TODO: question 2",
    "TODO: question 3",
]

OUTPUT_FILE = (
    Path(__file__).parent.parent.parent
    / "milestones"
    / "05_evaluation_and_reflection"
    / "results.md"
)


def run_baseline(question: str) -> str:
    from baseline_llm.baseline import ask  # noqa: import adjusted to your structure
    return ask(question)


def run_prompted(question: str) -> str:
    from prompt_engineering.run_prompts import ask, load_system_prompt
    from pathlib import Path
    prompt = load_system_prompt(Path(__file__).parent.parent / "02_prompt_engineering" / "prompts" / "v001_initial.md")
    return ask(question, prompt)


# def run_rag(question: str) -> str:
#     from rag.query import ask
#     return ask(question)["answer"]


def main():
    rows = []
    for q in QUESTIONS:
        row = {"question": q}
        row["v1_baseline"] = run_baseline(q)
        row["v2_prompted"] = run_prompted(q)
        # row["v3_rag"] = run_rag(q)  # uncomment when RAG is ready
        rows.append(row)

    lines = ["# Evaluation Results\n"]
    for row in rows:
        lines.append(f"## Q: {row['question']}\n")
        lines.append(f"**v1 (baseline):** {row['v1_baseline']}\n")
        lines.append(f"**v2 (prompted):** {row['v2_prompted']}\n")
        # lines.append(f"**v3 (RAG):** {row.get('v3_rag', 'N/A')}\n")
        lines.append("---\n")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
