# Milestone 1 — Pitch
**30.10.2026**

Dana Gordon, Anna Pably

---

## Working title
<!-- A short name for your project -->
For the Record: Address and Gender in the Parliament

## Focus area
Linguistics and languages: Linguistics and languages: A tool that explores how female and male speakers in the parliament are addressed and interrupted in debates, whether this is gender-specific, and if LLMs recognize such patterns.

## The theme and question
<!-- What are you exploring, and why does it matter to you? -->
This project aims to analyse political communication and legislative discourse in the Viennese parliament. Specifically, we want to detect differences, with the help of LLMs, in the treatment of female and male politicians. In particular, the focus will be on how the speakers are addressed (with/without titles, first/last names, …) and how often they are interrupted. The main question will then be whether an LLM-based AI tool can annotate such patterns as reliably as a human expert, or if it misses cases, hallucinates, or (re)produces bias. By doing so, we will take a look at gender bias in two instances: in the real-life case of political language itself, and in the LLMs that are trained on such language and therefore data itself.
As students with backgrounds in both computational linguistics and communication science, we are interested in the subtle ways language shapes gender and power dynamics. We are interested in exploring this topic because while gender-fair language guidelines exist on paper, we want to see if these are also reproduced in real-life legislative verbal interactions. Therefore, this project has not only a social interest, but also a personal one.

## The material
<!-- What will your system draw on? Who created it, and whose voices might be missing? -->
The tool that this project aims to build will draw on stenographic protocols of the Viennese parliament’s debates. This can be found under https://www.parlament.gv.at/ (National Council). To analyse whether politicians are addressed and treated equally, guidelines on gender-fair language will serve as a baseline and will be used to compare against actual parliamentary usage (ie. https://www.wien.gv.at/pdf/ma53/medien/leitfaden-richtiges-formulieren.pdf , especially relevant since it is provided by the city of Vienna itself).

## Why AI?
<!-- What could an AI system help you see or do here, and where might it mislead? -->
If used correctly, the AI tool can help us identify gender bias much faster than doing it manually, reducing the time for both watching videos and reading through protocols. On the other hand, the tool itself might reproduce bias.

## Who is it for?
<!-- Who might use what you build? -->
Students and researchers in the areas of linguistics, political science, and gender studies, or anyone interested in gender bias in the field of parliament debates.
Furthermore, this project aims to utilize political data as an instance but can be expanded to other domains dealing with similar issues afterwards (women in STEM, men vs. women in sports, female vs. male guests in talkshows, etc). The aim is to make this tool versatile so it can be used in different areas.

## Your team
<!-- Who is involved, and what does each person bring? -->
Anna Pably will be able to address the technical and linguistic side of the project due to her technical background (B.Sc. Computational Linguistics) with a focus on linguistics and in combination with societal issues (hate speech detection, bias detection).
Dana Gordon has a background in communication (B.Sc. Communication Science) and can therefore also address the technical side and bring expertise in discourse analysis and media framing theories.
The division of roles shall be discussed during the experiment phase (milestone 2).

## Concerns
<!-- The biggest technical or ethical uncertainty you can foresee -->
Depending on how well the AI tool we want to design works, it might reproduce bias or hallucinate and would bring up the question of how meaningful the results will be. However, since this is a very typical problem right now, we can then do further work to try and see the reasons for this (ie. explainability). Besides this, even though there are open access files from the Austrian Parliament itself (ie. National council protocols) that will provide our data, there might be more sources we would like to use, and those might be protected via licenses we would not know about at this point of the project. Furthermore, the fact that these sources are in the form of written transcripts, non-verbal cues, such as tone, facial expression, or body language, will be omitted. This results in us not being able to see the full picture of the debates happening in the parliament and therefore also potentially missing gender-specific biases that are expressed through non-verbal cues.
