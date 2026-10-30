# Your Question, Your Archive, Your AI
## AI-Aided Creative Exploration in the Humanities — Capstone Template

This repository is a **starting scaffold** for the capstone project. Clone it, rename things to match your project, and work through each milestone folder in order.

---

## Milestones at a glance

| # | Milestone | Due | Folder |
|---|-----------|-----|--------|
| 1 | Pitch | 30.10.2026 | `milestones/01_pitch/` |
| 2 | Material and ethics note | 13.11.2026 | `milestones/02_material_and_ethics/` |
| 3 | First experiments | 27.11.2026 | `milestones/03_first_experiments/` |
| 4 | Working prototype | 18.12.2026 | `milestones/04_working_prototype/` |
| 5 | Evaluation and reflection | 22.01.2027 | `milestones/05_evaluation_and_reflection/` |
| 6 | Showcase and documentation | 29.01.2027 | `milestones/06_showcase_and_documentation/` |

---

## Technical layers

Work through these in order. You must implement **LLM + prompt engineering**. Choose at least one of **RAG** or **agents**.

```
src/
├── 01_baseline_llm/        ← Plain LLM call, no special setup
├── 02_prompt_engineering/  ← Versioned prompts + experiment log
├── 03_rag/                 ← Retrieval-augmented generation (optional)
├── 04_agents/              ← Agent scaffold (optional)
└── evaluation/             ← Compare versions across your test questions
```

The evaluation framework (Section 7 of the brief) requires you to compare versions 1 → 2 → 3 (→ 4 if you use agents) against a fixed set of 5–10 questions. See `src/evaluation/`.

---

## Quick start

```bash
# 1. Clone
git clone https://github.com/rsouza/ai-humanities-capstone.git
cd ai-humanities-capstone

# 2. Set up Python environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."

# 4. Run the baseline
python src/01_baseline_llm/baseline.py
```

---

## Repository layout

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── milestones/               # One folder per milestone — fill in the templates
├── src/                      # Runnable code for each technical layer
├── data/
│   ├── raw/                  # Original source material (do NOT commit large files)
│   └── processed/            # Chunked / embedded versions ready for RAG
└── docs/
    ├── design_decisions.md   # Log of key choices and why you made them
    └── data_sources.md       # Provenance, copyright, and consent notes
```

---

## Shared commitments (from the brief)

- **Transparent about sources** — make it clear what comes from your collection vs. the model.
- **Honest about limits** — no invented quotations or sources presented as real.
- **Know your data** — document provenance, copyright, and whose voices are present or absent.
- **Human in the loop** — state what the system may not do without your approval.
