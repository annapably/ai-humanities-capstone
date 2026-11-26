import argparse
from datetime import date
from pathlib import Path
from transformers import pipeline

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "milestones" / "03_first_experiments" / "outputs" / "experiment_2"

QUESTIONS = {
    "Q1": "Which forms of address occur in this excerpt, and who is addressed in each case? Please provide the title, the form of the name (first name/last name), and the gender, as far as it can be recognised from the text for each instance.",
    "Q2": "Do interjections occur in this excerpt and what are they? For each instance, please state who calls out (name, gender, party) and what is said. Finish with the total number.",
    "Q3": "How does the President of the Austrian National Council usually address speakers? Give examples and say whether the form of address differs for women and men.",
    "Q4": "In two to three sentences, please describe how the speaker is addressed and interrupted in this excerpt regarding tone and attitude.",
    "Q5": "Which interjections in this excerpt come from members of the FPÖ?",
}
NEEDS_TEXT = {"Q1", "Q2", "Q4", "Q5"}

PROMPT = """You analyse excerpts from the stenographic protocols of the Austrian National Council. On request, please annotate forms of address towards the speaker, interjections ("Zwischenrufe") and calls to order ("Ordnungsrufe").

Rules:
1. Work only with the text provided. Do not mention anything that is not in it.
2. First quote the passage verbatim (in quotation marks), then give your interpretation.
3. For each passage, state: who speaks or calls out (name, gender, party if provided), who is addressed, and the type (address / interjection / call to order / reaction).
4. If something is unclear (e.g. a missing name or party), write "unclear" and do not guess.
5. If the text is not sufficient to answer the question, say so explicitly.
6. Describe language only. Do not evaluate persons or parties.
7. When needed, also consider whether an interjection / reaction is genuine or implicitly sarcastic.

You will now receive the question and the excerpt."""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
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

    for q, e in runs:
        # layout like in the Gemini/Claude chats: prompt, two blank lines, question, blank line, excerpt
        user = f"{PROMPT}\n\n\n{QUESTIONS[q]}" + (f"\n\n{excerpts[e]}" if e else "")
        messages = [{"role": "user", "content": user}]   # one message, no history
        result = gen(messages, max_new_tokens=args.max_new_tokens, do_sample=False)
        answer = result[0]["generated_text"][-1]["content"]

        name = f"exp2_qwen_3B_{q.lower()}" + (f"_e{e}" if e else "") + ".md"
        header = (
            "Experiment: 2 (prompted, v3 prepended to the question in one user message)\n"
            f"Model: {args.model} (local, transformers pipeline)\n"
            f"Date: {date.today().isoformat()}\n"
            f"Settings: do_sample=False (greedy), max_new_tokens={args.max_new_tokens}\n"
            f"Question: {q}" + (f", excerpt {e}" if e else ", no excerpt") + "\n\n---\n\n"
        )
        (OUT / name).write_text(header + answer + "\n", encoding="utf-8")
        print("saved", name)


if __name__ == "__main__":
    main()
