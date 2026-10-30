# Evaluation Framework

Section 7 of the brief requires comparing increasingly capable versions of your system on the same fixed set of questions.

## Steps

1. Write your 5–10 evaluation questions in `questions.md`.
2. Run `python src/evaluation/evaluate.py` — it calls each version and writes a results table.
3. Analyse the table and fill in `milestones/05_evaluation_and_reflection/evaluation.md`.

## Versions to compare

| Version | What it is | Script |
|---------|-----------|--------|
| v1 | Plain LLM, no special setup | `src/01_baseline_llm/baseline.py` |
| v2 | LLM + designed prompt | `src/02_prompt_engineering/run_prompts.py` |
| v3 | v2 + RAG | `src/03_rag/query.py` |
| v4 | v3 + agents | `src/04_agents/agent.py` |

A project using RAG compares v1–v3. One using agents compares v1–v4.
