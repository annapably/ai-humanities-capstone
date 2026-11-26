"""Experiment 2: prompted (v2 as system message). Local Qwen, one .md file per run.

Usage (repo root, venv active):
    python src/02_prompt_engineering/run_exp2.py
    python src/02_prompt_engineering/run_exp2.py --only Q3
"""
import argparse
from datetime import date
from pathlib import Path
from transformers import pipeline

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "milestones" / "03_first_experiments" / "outputs"

QUESTIONS = {
    "Q1": "Which forms of address occur in this excerpt, and who is addressed in each case? Please provide the title, the form of the name (first name/last name), and the gender, as far as it can be recognised from the text for each instance.",
    "Q2": "Do interjections occur in this excerpt and what are they? For each instance, please state who calls out (name, gender, party) and what is said. Finish with the total number.",
    "Q3": "How does the President of the Austrian National Council usually address speakers? Give examples and say whether the form of address differs for women and men.",
    "Q4": "In two to three sentences, please describe how the speaker is addressed and interrupted in this excerpt regarding tone and attitude.",
    "Q5": "Which interjections in this excerpt come from members of the FPÖ?",
}
NEEDS_TEXT = {"Q1", "Q2", "Q4", "Q5"}

PROMPT_V2 = """Du analysierst Ausschnitte aus Stenographischen Protokollen des österreichischen Nationalrats. Annotiere auf Anfrage Anredeformen, Zwischenrufe und Ordnungsrufe.

Regeln:
1. Arbeite nur mit dem gelieferten Text. Nenne nichts, was nicht darin steht.
2. Zitiere zuerst die Textstelle wörtlich (in Anführungszeichen), dann deine Einordnung.
3. Gib für jede Stelle an: wer spricht bzw. ruft, wer angesprochen wird, Art (Anrede / Zwischenruf / Ordnungsruf).
4. Wenn etwas unklar ist (z. B. fehlender Name oder Fraktion), schreibe "unklar" und rate nicht.
5. Wenn der Text nicht ausreicht, um die Frage zu beantworten, sage das ausdrücklich.
6. Beschreibe nur Sprache. Bewerte keine Personen oder Parteien."""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen2.5-1.5B-Instruct")
    ap.add_argument("--only", help="run only one question, e.g. Q2")
    ap.add_argument("--max-new-tokens", type=int, default=1500)
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    excerpts = {n: (RAW / f"milestone3_excerpt{n}.txt").read_text(encoding="utf-8").strip() for n in (1, 2)}
    gen = pipeline("text-generation", model=args.model)

    runs = []
    for q in QUESTIONS:
        if args.only and q != args.only:
            continue
        if q in NEEDS_TEXT:
            runs += [(q, 1), (q, 2)]
        else:
            runs.append((q, None))

    for q, ex in runs:
        user = QUESTIONS[q] if ex is None else f"{QUESTIONS[q]}\n\n{excerpts[ex]}"
        messages = [
            {"role": "system", "content": PROMPT_V2},
            {"role": "user", "content": user},
        ]   # fresh messages for every run, no history
        result = gen(messages, max_new_tokens=args.max_new_tokens, do_sample=False)
        answer = result[0]["generated_text"][-1]["content"]

        name = f"exp2_qwen_1.5B_{q.lower()}" + (f"_e{e}" if e else "") + ".md"
        header = (
            "Experiment: 2 (prompted, v2 as system message)\n"
            f"Model: {args.model} (local, transformers pipeline)\n"
            f"Date: {date.today().isoformat()}\n"
            f"Settings: do_sample=False (greedy), max_new_tokens={args.max_new_tokens}\n"
            f"Question: {q}" + (f", excerpt {ex}" if ex else ", no excerpt") + "\n\n---\n\n"
        )
        (OUT / name).write_text(header + answer + "\n", encoding="utf-8")
        print("saved", name)


if __name__ == "__main__":
    main()
