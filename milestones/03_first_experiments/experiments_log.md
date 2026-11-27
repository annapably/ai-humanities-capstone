# Milestone 3 — First Experiments Log
**Due: 27.11.2026**

Record each experiment here as you run it. Copy the template block for every new run.

See `src/evaluation/questions.md` for your 5–10 test questions.

Note: Since we ran a total of 81 experiments, we will showcase one experiment for each type in this log.
For the full experiment selection, see `milestones/03_first_experiments/experiments`, including the three main experiment types (baseline, prompted, Claude project) and the experiments respectively using Claude, Gemini, Qwen 1.5B and Qwen 3B with the different questions on two excerpts of the protocols.
The code used for the Qwen experiment instances can be found under `src/02_prompt_engineering_prompts`.

Disclaimer: Use of Claude for goldstandard template and prompt inspiration and scripts for Qwen code.

---

## Model comparison notes

Note how at least **two models** differ for your material:

| Model          | Strength observed                                     | Weakness observed                                                |
|----------------|-------------------------------------------------------|------------------------------------------------------------------|
| Claude         | Exp. 1: Mostly correct                                | Made up names                                                    |
|                | Exp. 2: Correct, complete, gives quotes               | Occurrence with faulty gender detection                          |
|                | Exp. 3: Similar to Exp. 2 but also able to use inputs | Still missed a gender que                                        |
| Gemini         | Exp. 1: Mostly correct                                | Made up names                                                    |
|                | Exp. 2: Almost entirely correct, complete             | Totals not always accurate to gold standard, inconsistent gender |
| Qwen 1.5B      | TODO                                                  | TODO                                                             |
| Qwen 3B        | TODO                                                  | TODO                                                             |

---

# Experiment template

## Experiment 1 - Baseline
### Experiment 1.1 — Claude: Testing 5 Questions on 2 Excerpts Without Further Prompting
Date: 2026-11-25

Model: Claude Sonnet 5.5 Medium

Prompt version: v1 - prompt only as question with excerpt

Layer: baseline
 
**Question 1/Excerpt 1 & Output:**
[exp1_claude_q1_e1](experiments/experiment_1/exp1_claude_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp1_claude_q1_e2](experiments/experiment_1/exp1_claude_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp1_claude_q2_e1](experiments/experiment_1/exp1_claude_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp1_claude_q2_e2](experiments/experiment_1/exp1_claude_q2_e2.md)

**Question 3 & Output:**
[exp1_claude_q3](experiments/experiment_1/exp1_claude_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp1_claude_q4_e1](experiments/experiment_1/exp1_claude_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp1_claude_q4_e2](experiments/experiment_1/exp1_claude_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp1_claude_q5_e1](experiments/experiment_1/exp1_claude_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp1_claude_q5_e2](experiments/experiment_1/exp1_claude_q5_e2.md)

**What I noticed:**
- Claude manages to grasp the information and context correctly, recognizes forms and address and separates them from a simple mention of name
- For Q3, Claude claims that academic titles are regularly stated
- For Q4, the content is correct, but Claude exceeded the limit of 2-3 sentences (4 sentences)
- The questions that are answered with a number are in line with our manually annotated gold standard (Q2, Q5)

**What I will change next:**
- Try the same thing for Gemini

### Experiment 1.2 — Gemini: Testing 5 Questions on 2 Excerpts Without Further Prompting
Date: 2026-11-25

Model: Gemini Hydrogen

Prompt version: v1 - prompt only as question with excerpt

Layer: baseline

 
**Question 1/Excerpt 1 & Output:**
[exp1_gemini_q1_e1](experiments/experiment_1/exp1_gemini_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp1_gemini_q1_e2](experiments/experiment_1/exp1_gemini_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp1_gemini_q2_e1](experiments/experiment_1/exp1_gemini_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp1_gemini_q2_e2](experiments/experiment_1/exp1_gemini_q2_e2.md)

**Question 3 & Output:**
[exp1_gemini_q3](experiments/experiment_1/exp1_gemini_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp1_gemini_q4_e1](experiments/experiment_1/exp1_gemini_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp1_gemini_q4_e2](experiments/experiment_1/exp1_gemini_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp1_gemini_q5_e1](experiments/experiment_1/exp1_gemini_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp1_gemini_q5_e2](experiments/experiment_1/exp1_gemini_q5_e2.md)

**What I noticed:**
- Like Claude, Gemini manages to grasp the information and context correctly, recognizes forms and address and separates them from a simple mention of name
- Content correct
- For Q3, Gemini also claims that academic titles are regularly stated
- The questions that are answered with a number are in line with our manually annotated gold standard (Q2, Q5)

**What I will change next:**
- Compare to an "embedded" LLM by coding using Qwen to see if there is a difference when using a chatbot or a model via programmed prompting. Also test with specific prompts (rules).

### Experiment 1.3 — Qwen 1.5B: Testing 5 Questions on 2 Excerpts Without Further Prompting
Date: 2026-11-25

Model: x

Prompt version: v1 - prompt only as question with excerpt

Layer: baseline

 
**Question 1/Excerpt 1 & Output:**
[exp1_claude_q1_e1](experiments/experiment_1/exp1_claude_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp1_claude_q1_e2](experiments/experiment_1/exp1_claude_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp1_claude_q2_e1](experiments/experiment_1/exp1_claude_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp1_claude_q2_e2](experiments/experiment_1/exp1_claude_q2_e2.md)

**Question 3 & Output:**
[exp1_claude_q3](experiments/experiment_1/exp1_claude_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp1_claude_q4_e1](experiments/experiment_1/exp1_claude_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp1_claude_q4_e2](experiments/experiment_1/exp1_claude_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp1_claude_q5_e1](experiments/experiment_1/exp1_claude_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp1_claude_q5_e2](experiments/experiment_1/exp1_claude_q5_e2.md)

**What I noticed:**
- d

**What I will change next:**
- d

### Experiment 1.4 — Qwen 3B: Testing 5 Questions on 2 Excerpts Without Further Prompting
Date: 2026-11-25
Model: x
Prompt version: v1 - prompt only as question with excerpt
Layer: baseline

 
**Question 1/Excerpt 1 & Output:**
[exp1_claude_q1_e1](experiments/experiment_1/exp1_claude_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp1_claude_q1_e2](experiments/experiment_1/exp1_claude_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp1_claude_q2_e1](experiments/experiment_1/exp1_claude_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp1_claude_q2_e2](experiments/experiment_1/exp1_claude_q2_e2.md)

**Question 3 & Output:**
[exp1_claude_q3](experiments/experiment_1/exp1_claude_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp1_claude_q4_e1](experiments/experiment_1/exp1_claude_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp1_claude_q4_e2](experiments/experiment_1/exp1_claude_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp1_claude_q5_e1](experiments/experiment_1/exp1_claude_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp1_claude_q5_e2](experiments/experiment_1/exp1_claude_q5_e2.md)

**What I noticed:**
- d

**What I will change next:**
- d

## Experiment 2 - Prompting with Rules
### Experiment 2.1 — Claude: Testing 5 Questions on 2 Excerpts With Specific Prompt
Date: 2026-11-25

Model: Claude Sonnet 5.5 Medium

Prompt version: v2 - prompt including specific set of rules

Layer: prompted


**Question 1/Excerpt 1 & Output:**
[exp2_claude_q1_e1](experiments/experiment_2/exp2_claude_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp2_claude_q1_e2](experiments/experiment_2/exp2_claude_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp2_claude_q2_e1](experiments/experiment_2/exp2_claude_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp2_claude_q2_e2](experiments/experiment_2/exp2_claude_q2_e2.md)

**Question 3 & Output:**
[exp2_claude_q3](experiments/experiment_2/exp2_claude_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp2_claude_q4_e1](experiments/experiment_2/exp2_claude_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp2_claude_q4_e2](experiments/experiment_2/exp2_claude_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp2_claude_q5_e1](experiments/experiment_2/exp2_claude_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp2_claude_q5_e2](experiments/experiment_2/exp2_claude_q5_e2.md)

**What I noticed:**
- Quantitative results same as gold standard
- Improvement: no guessing of names anymore
- Gave direct quotes so we can confirm
- Still gave longer answer
- Q3 does not work without prompt

**What I will change next:**
- Test the same with Gemini

### Experiment 2.2 — Gemini: Testing 5 Questions on 2 Excerpts With Specific Prompt
Date: 2026-11-25

Model: Gemini Hydrogen

Prompt version: v2 - prompt including specific set of rules

Layer: prompted

 
**Question 1/Excerpt 1 & Output:**
[exp2_gemini_q1_e1](experiments/experiment_2/exp2_gemini_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp2_gemini_q1_e2](experiments/experiment_2/exp2_gemini_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp2_gemini_q2_e1](experiments/experiment_2/exp2_gemini_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp2_gemini_q2_e2](experiments/experiment_2/exp2_gemini_q2_e2.md)

**Question 3 & Output:**
[exp2_gemini_q3](experiments/experiment_2/exp2_gemini_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp2_gemini_q4_e1](experiments/experiment_2/exp2_gemini_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp2_gemini_q4_e2](experiments/experiment_2/exp2_gemini_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp2_gemini_q5_e1](experiments/experiment_2/exp2_gemini_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp2_gemini_q5_e2](experiments/experiment_2/exp2_gemini_q5_e2.md)

**What I noticed:**
- Generally very similar to the points in Claude
- Names mentions
- Gender not uniform

**What I will change next:**
- Test for Qwen

### Experiment 2.3 — Qwen 1.5B: Testing 5 Questions on 2 Excerpts With Specific Prompt
Date: 2026-11-25
Model: x
Prompt version: v2 - prompt including specific set of rules
Layer: prompted

 
**Question 1/Excerpt 1 & Output:**
[exp1_claude_q1_e1](experiments/experiment_1/exp1_claude_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp1_claude_q1_e2](experiments/experiment_1/exp1_claude_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp1_claude_q2_e1](experiments/experiment_1/exp1_claude_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp1_claude_q2_e2](experiments/experiment_1/exp1_claude_q2_e2.md)

**Question 3 & Output:**
[exp1_claude_q3](experiments/experiment_1/exp1_claude_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp1_claude_q4_e1](experiments/experiment_1/exp1_claude_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp1_claude_q4_e2](experiments/experiment_1/exp1_claude_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp1_claude_q5_e1](experiments/experiment_1/exp1_claude_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp1_claude_q5_e2](experiments/experiment_1/exp1_claude_q5_e2.md)

**What I noticed:**
- d

**What I will change next:**
- d

### Experiment 2.4 — Qwen 3B: Testing 5 Questions on 2 Excerpts With Specific Prompt
Date: 2026-11-25
Model: x
Prompt version: v2 - prompt including specific set of rules
Layer: prompted

 
**Question 1/Excerpt 1 & Output:**
[exp1_claude_q1_e1](experiments/experiment_1/exp1_claude_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp1_claude_q1_e2](experiments/experiment_1/exp1_claude_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp1_claude_q2_e1](experiments/experiment_1/exp1_claude_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp1_claude_q2_e2](experiments/experiment_1/exp1_claude_q2_e2.md)

**Question 3 & Output:**
[exp1_claude_q3](experiments/experiment_1/exp1_claude_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp1_claude_q4_e1](experiments/experiment_1/exp1_claude_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp1_claude_q4_e2](experiments/experiment_1/exp1_claude_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp1_claude_q5_e1](experiments/experiment_1/exp1_claude_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp1_claude_q5_e2](experiments/experiment_1/exp1_claude_q5_e2.md)

**What I noticed:**
- d

**What I will change next:**
- d

## Experiment 3 - Claude Project: Testing 5 Questions on 2 Excerpts With Specific Prompt and Further Information
Date: 2026-11-25

Model: Claude Sonnet 5.5 Medium

Prompt version: using project with information and context as well as prompts

Layer: project
 
**Question 1/Excerpt 1 & Output:**
[exp3_claudeproject_q1_e1](experiments/experiment_3/exp3_claudeproject_q1_e1.md)

**Question 1/Excerpt 2 & Output:**
[exp3_claudeproject_q1_e2](experiments/experiment_3/exp3_claudeproject_q1_e2.md)

**Question 2/Excerpt 1 & Output:**
[exp3_claudeproject_q2_e1](experiments/experiment_3/exp3_claudeproject_q2_e1.md)

**Question 2/Excerpt 2 & Output:**
[exp3_claudeproject_q2_e2](experiments/experiment_3/exp3_claudeproject_q2_e2.md)

**Question 3 & Output:**
[exp3_claudeproject_q3](experiments/experiment_3/exp3_claudeproject_q3.md)

**Question 4/Excerpt 1 & Output:**
[exp3_claudeproject_q4_e1](experiments/experiment_3/exp3_claudeproject_q4_e1.md)

**Question 4/Excerpt 2 & Output:**
[exp3_claudeproject_q4_e2](experiments/experiment_3/exp3_claudeproject_q4_e2.md)

**Question 5/Excerpt 1 & Output:**
[exp3_claudeproject_q5_e1](experiments/experiment_3/exp3_claudeproject_q5_e1.md)

**Question 5/Excerpt 2 & Output:**
[exp3_claudeproject_q5_e2](experiments/experiment_3/exp3_claudeproject_q5_e2.md)

**What I noticed:**
- For Q1, Claude Project achieved the best results so far (most likely due to the given files as context)
- Almost all same as gold standard
- Q3: Answered based on the given data -> works
- Is slightly inconsistent in one part (changes mind back and forth from answer given at the beginning compared to the one at the end)
- 

**What I will change next:**
- In the future, we aim at combining the methods that achieved best results and will most likely leave out Qwen 1.5B and Qwen 3B.

---
