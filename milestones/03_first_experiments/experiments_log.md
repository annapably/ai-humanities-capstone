# Milestone 3 — First Experiments Log
**Due: 27.11.2026**

Record each experiment here as you run it. Copy the template block for every new run.

See `src/evaluation/questions.md` for your 5–10 test questions.

**Note:** Since we ran a total of 81 experiments, we will link the questions and outputs for each experiment in this log.
For the full experiment selection, see `milestones/03_first_experiments/experiments`, including the three main experiment types (baseline, prompted, Claude project) and the experiments respectively using Claude, Gemini, Qwen 1.5B and Qwen 3B with the different questions on two excerpts of the protocols.
The code used for the Qwen experiment instances can be found under `src/02_prompt_engineering_prompts`.

**Disclaimer:** Use of Claude for gold standard template inspiration, prompt inspiration, and help for the scripts of the Qwen code.

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

Model:Qwen 2.5-1.5B

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
- Without prompting and with greedy decoding, the model hallucinates a lot and gets stuck in repetition loops
- It, for example, invents full names 
- It gets confused with the roles/titles and gender -> e.g. it says that Zuseherinnen und Zuseher addresses "women voters" 
- It gets confused with interjections -> says that the speakers interjects even though it is his turn to speak
- It invents titles such as "Hochzeitsvater" / "Hochzeitsmutter"
- it gets abbreviations wrong -> e.g. says FPÖ stands for Folkspartei Österreich or SPÖ/Spä for "Sociálna pozicia"
- doesnt get titles right -> e.g. says that Mr is the title even though the full title would be Herr Präsident

**What I will change next:**
- Will try the same with Qwen 3B instead of Qwen 1.5B

### Experiment 1.4 — Qwen 3B: Testing 5 Questions on 2 Excerpts Without Further Prompting
Date: 2026-11-25

Model: Qwen 2.5-3B

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
- Without prompting and with greedy decoding, Qwen 3B hallucinates a lot and gets stuck in repetition loops
- it labels roles, such as President or Colleague, as first names
- it invents full names again
- it identifies the speaker's words as interjection even though it is his turn to speak
- it gets confused about who is the main speaker and who is the one interrupting the speaker
- it also confuses the austrian Nationalrat with the german Bundestag
- it gives less incorrect abbreviation expansions compared to Qwen 1.5


**What I will change next:**
- i will try to use prompts

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

Model: Qwen 2.5-1.5B

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
- It still outputs repetition loops
- It still invents first names
- it assigns wrong party to people
- it did not work for Q3
- For Q4 it should in theory only give 2-3 as an output but it made a whole list of bulletpoints for excerpt 1 and for excerpt 2 in outputted a repetition loop
- prompt did however prevent Qwen 1.5 from counting the speaker's salutations as interjections

**What I will change next:**
- will try the same with Qwen 3B

### Experiment 2.4 — Qwen 3B: Testing 5 Questions on 2 Excerpts With Specific Prompt
Date: 2026-11-25

Model: Qwen 2.5-3B

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
- For a lot of the questions it just outputted the whole excerpt with nothing else
- so it doesnt answer a lot of the questions
- and the answers it gives are not good and not complete-> e.g. for Q2 it just cuts off at point 6 without giving gender or total number
- it also invents names again
- also doesnt stick to the 2-3 sentence limit
- it hallucinates interjections
- for Q5 it does identify some genuine interventions by Wurm but it states that who is addressed is unclear

**What I will change next:**
- instruct the model to not repeat the excerpt each time

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

## Model comparison notes

Note how at least **two models** differ for your material:

| Model           | Strength observed                                                  | Weakness observed                                                                               |
|-----------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Claude          | Exp. 1: Mostly correct                                             | Made up names                                                                                   |
| Claude          | Exp. 2: Correct, complete, gives quotes                            | Occurrence with faulty gender detection                                                         |
| Claude(Project) | Exp. 3: Similar to Exp. 2 but also able to use inputs              | Still missed a gender que                                                                       |
| Gemini          | Exp. 1: Mostly correct                                             | Made up names                                                                                   |
| Gemini          | Exp. 2: Almost entirely correct, complete                          | Totals not always accurate to gold standard, inconsistent gender                                |
| Qwen 1.5B       | Exp. 1: Follows Q4 sentence limit, runs locally                    | Hallucinated names/parties/quotes, repetition loops, counts greetings as interjections          |
| Qwen 1.5B       | Exp. 2: Stops counting opening greetings as interjections          | Severe repetition loops, refuses Q3 without excerpt, breaks Q4 format/length and Q2 total count |
| Qwen 3B         | Exp. 1: Better MP/party recognition than 1.5B, fewer wild acronyms | Repetition loops, made up first names, confuses speaker/interjector roles and Bundestag         |
| Qwen 3B         | Exp. 2: Identifies real FPÖ interjections in Q5 E2                 | Echoes full excerpts and truncates early, fabricates quotes in Q5 E1, misses counts/fields      |


---
