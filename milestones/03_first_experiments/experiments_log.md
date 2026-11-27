# Milestone 3 — First Experiments Log
**Due: 27.11.2026**

Record each experiment here as you run it. Copy the template block for every new run.

See `src/evaluation/questions.md` for your 5–10 test questions.

Note: Since we ran a total of 81 experiments, we will showcase one experiment for each type in this log.
For the full experiment selection, see `milestones/03_first_experiments/experiments`, including the three main experiment types (baseline, prompted, Claude project) and the experiments respectively using Claude, Gemini, Qwen 1.5B and Qwen 3B with the different questions on two excerpts of the protocols.
The code used for the Qwen experiment instances can be found under `src/02_prompt_engineering_prompts`.

Disclaimer: Use of Claude for goldstandard template and prompt inspiration and scripts for Qwen code.

---

## Experiment template

```

### Experiment [1] — Qwen 2.5 1.5B baseline across Q1–Q5 with excerpts 1 and 2
Date: 22026-11-26
Model: Qwen2.5-1.5B
Prompt version: v000 (no prompt)
Layer: baseline

**Question asked:**
Q1: Which forms of address occur in this excerpt, and who is addressed in each case? Please provide the title, the form of the name (first name/last name), and the gender, as far as it can be recognised from the text for each instance. (Excerpt 1 & Excerpt 2)
Q2: Do interjections occur in this excerpt and what are they? For each instance, please state who calls out (name, gender, party) and what is said. Finish with the total number. (Excerpt 1 & Excerpt 2)
Q3: How does the President of the Austrian National Council usually address speakers? Give examples and say whether the form of address differs for women and men. (No excerpt)
Q4: In two to three sentences, please describe how the speaker is addressed and interrupted in this excerpt regarding tone and attitude. (Excerpt 1 & Excerpt 2)
Q5: Which interjections in this excerpt come from members of the FPÖ? (Excerpt 1 & Excerpt 2)


**Output:**
-----------Q1: Excerpt 1:-----------
Here's a breakdown of the forms of address used in the excerpt:

    Ines Holzegger - Addressed to Ines Holzegger, a member of parliament.
        Title: Member of Parliament
        Form of Name: First name
        Gender: Female

    Herr Präsident - Addressed to the President.
        Title: None
        Form of Name: Last name
        Gender: Male

    Frau Staatssekretärin - Addressed to the State Secretary.
        Title: State Secretary
        Form of Name: Last name
        Gender: Female

    Liebe Zuseherinnen und Zuseher - Addressed to women voters.
        Title: None
        Form of Name: None
        Gender: Both

    Matznetter [SPÖ] - Addressed to Matthias Netter, a member of the Social Democratic Party (SPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Darmann [FPÖ] - Addressed to Daniel Darmann, a member of the Freedom Party of Austria (FPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Kaniak [FPÖ] - Addressed to Andreas Kaniak, a member of the Freedom Party of Austria (FPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Wurm [FPÖ] - Addressed to Wolfgang Wurm, a member of the Freedom Party of Austria (FPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Steiner [FPÖ] - Addressed to Christian Steiner, a member of the Freedom Party of Austria (FPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Petschnig [FPÖ] - Addressed to Peter Petschnig, a member of the Freedom Party of Austria (FPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Schiefer - Addressed to Hans Schiefer, a member of the Austrian People's Party (ÖVP).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Kolm - Addressed to Elisabeth Kolm, a member of the Austrian People's Party (ÖVP).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Female

    Schiefer - Addressed to Hans Schiefer, a member of the Austrian People's Party (ÖVP).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Kaniak - Addressed to Andreas Kaniak, a member of the Freedom Party of Austria (FPÖ).
        Title: Member of Parliament
        Form of Name: First name
        Gender: Male

    Staatssekretärin - Addressed to the State Secretary.
        Title: State Secretary
        Form of Name: Last name
        Gender: Female

    Anzahl - Addressed to the number of people present.
        Title: None
        Form of Name: None
        Gender: Neutral

    Die Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regel - Addressed to the rule.
        Title: None
        Form of Name: None
        Gender: Neutral

    Regeln - Addressed to the rules.
        Title: None
        Form of Name: None

-----------Q1: Excerpt 2:-----------
Here's a breakdown of the forms of address used in the excerpt:

    Mr. - Used twice:
        "Herr Präsident" (Mr. President)
        "Frau Staatssekretärin" (Mrs. State Secretary)

    Ms. - Used once:
        "Frau Staatssekretärin" (Mrs. State Secretary)

    Dr. - Used once:
        "Dr. Wurm" (Mr. Wurm)

    Peter - Addressed to Mr. Wurm (FPÖ).

    Abg. - Abbreviation for "Abgeordneter", meaning Member of Parliament or Representative.
        "Abg. Wurm" (Member of Parliament Wurm)
        "Abg. Hofer" (Member of Parliament Hofer)
        "Abg. Hafenecker" (Member of Parliament Hafenecker)

    NEOS - Abbreviation for "Neue Europäische Sozialisten".

    Spä - Shortened version of "Sociálna pozicia" (Social Democratic Party).
        "Abg. Spä" (Member of Parliament Spä)

    Abg. - Abbreviation for "Abgeordneter".
        "Abg. Wurm" (Member of Parliament Wurm)
        "Abg. Hofer" (Member of Parliament Hofer)
        "Abg. Hafenecker" (Member of Parliament Hafenecker)

    Abg. - Abbreviation for "Abgeordneter".
        "Abg. Wurm" (Member of Parliament Wurm)
        "Abg. Hofer" (Member of Parliament Hofer)
        "Abg. Hafenecker" (Member of Parliament Hafenecker)

The gender of these individuals cannot be definitively determined based solely on their names and titles in the text. However, given the context, they appear to be male politicians.

-----------Q2: Excerpt 1:-----------
In this excerpt, there are several instances of interjections:

    "Vielen herzlichen Dank" - This is an interjection expressing gratitude.
        Who called out: Ines Holzegger (NEOS)
        What was said: "Vielen herzlichen Dank, Herr Präsident!"

    "Herr Präsident!" - This is an exclamation expressing respect or enthusiasm.
        Who called out: Ines Holzegger (NEOS)

    "Werte Frau Staatssekretärin!" - This is an interjection expressing respect for someone's position.
        Who called out: Ines Holzegger (NEOS)

    "Hohes Haus!" - This is an interjection expressing excitement or enthusiasm.
        Who called out: Ines Holzegger (NEOS)

    "Liebe Zuseherinnen und Zuseher!" - This is an interjection expressing affection towards people.
        Who called out: Ines Holzegger (NEOS)

The total number of interjections in this excerpt is 5.

-----------Q2: Excerpt 2:-----------
In this excerpt, there are several instances where interjections occur:

    "Danke, Herr Präsident!" - This is an interjection from Abgeordneter Michael Seemayer (SPÖ), addressing the President.
    "Frau Staatssekretärin!" - Another interjection from Abgeordneter Michael Seemayer to address the State Secretary.
    "(Heiterkeit des Abg. Hofer [NEOS])" - This is an interjection from Abgeordneter Hofer (NEOS) expressing amusement or laughter.
    "Einer hat’s geschafft! Einer!" - These are interjections from Abgeordneter Wurm (FPÖ) indicating that one person has succeeded in something.
    "Die Tankstellen machen sieben!" - This is another interjection from Abgeordneter Wurm, emphasizing the seven decimal places at gas stations.
    "Billiger! Der Neuner kommt eine Stelle vor!" - This is an interjection from Abgeordneter Wurm, suggesting that prices for gold and other metals are lower than usual.
    "Bravo!" - This is an interjection from both Abgeordneter Hofer (NEOS) and Abgeordneter Kocevar (SPÖ), expressing approval or admiration.
    "Neues!" - This is an interjection from Abgeordneter Hofer, possibly referring to new developments or changes.

The total number of interjections in this excerpt is 8.

-----------Q3:-----------
The President of the Austrian National Council typically addresses speakers in a formal manner that is respectful to all participants, regardless of gender. The style of addressing can vary slightly depending on the context or specific circumstances but generally follows these guidelines:

    Formal Address: When speaking formally, the President might use titles such as "Herr" (Mr.) or "Frau" (Mrs./Ms.), followed by their name. For example:
        "Herr Präsident," [Name] "würden Sie bitte Ihre Rede halten?"
        "Frau Präsidentin," [Name] "würden Sie bitte Ihre Rede halten?"

    Casual Address: In more informal settings, especially during social gatherings or when welcoming guests, the President may use a more casual tone. However, this would still be addressed with respect.
        "Guten Tag, Herr/ Frau [Name]."
        "Guten Tag, Herr/ Frau [Name]."

    Specific Contexts:
        If the speaker is known to have a significant influence or if they are particularly important, the President might use a title like "Herr Ministerpräsident" (Mr. Minister-President) before their name.
        During ceremonies or official events, the President might use an honorific like "Hochzeitsvater" (Married Father) or "Hochzeitsmutter" (Married Mother), which indicates respect for the couple.

    Gender-Neutral Language: It's worth noting that Austria has been moving towards gender-neutral language in its official documents and communications. This means that while the President will always address individuals using appropriate titles based on their gender, there is no longer a distinction made between male and female forms of address within the official discourse.

In summary, the President of the Austrian National Council uses formal and respectful language when addressing speakers, without making distinctions based on gender. This ensures that all participants feel valued and respected throughout the proceedings.

-----------Q4: Excerpt 1:-----------
The speaker is addressed as "Frau Staatssekretärin" and "Frau Zuseherinnen und Zuseher", indicating respect for their positions. However, they are also referred to with colloquial terms like "Liebe Zuseherinnen und Zuseher" and "Frau Kollegin", showing a more informal tone. The interruptions from other speakers, such as the laughter of the FPÖ representative and the applause from the NEOS members, indicate that the conversation has become somewhat rowdy or contentious.

-----------Q4: Excerpt 2:-----------
The speaker is addressed as "Herr Präsident" and "Frau Staatssekretärin", but is then interrupted multiple times throughout the excerpt with laughter from other speakers, indicating that they do not take the speaker's statements seriously or find them amusing. The overall tone and attitude of the excerpt is one of skepticism and criticism towards the speaker's claims about illegal gold trading, while also mocking their apparent naivety on the subject matter.

-----------Q5: Excerpt 1:-----------
Based on the excerpt provided, several interjections and exclamations can be identified as coming from members of the FPÖ (Folkspartei Österreich). These include:

    "Für Freiheit!" - This is repeated twice by Kaniak, indicating strong support for the FPÖ's stance on freedom.

    "Wir sind Volkspartei!" - This is also repeated by Kaniak, emphasizing his party affiliation with the FPÖ.

    "Das ist nur eine Verständnisfrage!" - This is said by Kaniak, showing disagreement or questioning the validity of something proposed by others.

    "Es hat die D-Mark gegeben!" - This statement is made by Steiner, suggesting that he disagrees with the idea that the FPÖ supports the use of the DM mark instead of the euro.

    "Vielen Dank." - This is used at the end of the speech, which could indicate appreciation or gratitude towards someone speaking on behalf of the FPÖ.

These elements clearly show that the speaker is likely representing the FPÖ in their comments and statements within the context of the discussion about mobile gold buying scams.

-----------Q5: Excerpt 2:-----------
Based on the excerpt provided, several interjections and comments can be identified as coming from members of the FPÖ (Frac de la Voie Romane). Here are some examples:

    "Einer hat's geschafft!" - This is a common phrase used by FPÖ members to express pride or satisfaction with their achievements.

    "Die Tankstellen machen sieben!" - This comment suggests that the speaker believes tank stations should have seven decimal places for prices, which aligns with FPÖ policies regarding price transparency.

    "Billiger! Der Neuner kommt eine Stelle vor!" - The use of "billiger" indicates support for lower prices, which is consistent with FPÖ economic policies.

    "Bravo!" - This exclamation is often used by FPÖ members to show approval or admiration.

    "NEOS, was ist denn los mit euch?" - This question shows frustration towards other parties, likely referring to opposition members like the SPÖ or ÖVP.

    "Das wollen wir mit unserem Antrag in die Wege leiten." - This statement expresses determination to push through the proposed legislation, which is characteristic of FPÖ positions.

    "Es braucht da einen besseren Schutz für die Konsumentinnen und Konsumenten." - This comment highlights concerns about consumer protection, which is another area where FPÖ tends to advocate strongly.

These elements demonstrate how FPÖ members frequently use humor, direct statements, and rhetorical questions to convey their views and engage with others during discussions.


**What I noticed:**
Q1: Excerpt 1: Lists Ines Holzegger, Herr Präsident, Frau Staatssekretärin, Liebe Zuseherinnen und Zuseher, etc but then it starts to hallucinates and gets stuck in a loop where it repeats "Regel - Addressed to the rule" a dozen times. 
               It also invents full first names (e.g., Matthias Netter, Daniel Darmann, Andreas Kaniak, Wolfgang Wurm, Christian Steiner, Peter Petschnig, Hans Schiefer, Elisabeth Kolm). 
               It and labels Zuseherinnen und Zuseher as "women voters" even though these are obviously not only women.
               It also says that Herr Präsident has no title
Q1: Excerpt 2: Uses "Mr." / "Mrs" even though the text is in German
               Maps "Herr Präsident" and "Frau STaatssektretärin" to "Mr."
               Doesnt provide the genders anymore
               Says that the invented name "Dr. Wurm" appears in the text
               Misidentifies NEOS as "Neue Europäische Sozialisten"
               Misidentifies SPÖ/Spä as "Sociálna pozicia"
               Repeats Abg. blocks, and concludes gender cannot be definitively determined from names/titles alone before guessing male politicians.
Q2: Excerpt 1: Says that Holzegger interject multiple times even though he doesnt
               ->it is his turn speaking and he is just greeting everyone
               It misses actual parliamentary interjections (Zwischenruf / Ruf / Abg. callouts)
Q2: Excerpt 2: Says that Seemayer has some interjections even though it is his turn speaking and he is just greeting everyone
               Gets some interjections correct
               Says that the interjection "Bravo!" is from Hofer and Kocevar even though it is Wurm who says this
               It hallucinates the interjection "Neues!" from Hofer
Q3: No excerpt: Says that the President uses "Herr Präsident," [Name] or "Frau Präsidentin," [Name] to adress others which doesnt make sense since he is the president and the others are not
                It invents casual greetings ("Guten Tag, Herr/ Frau [Name]")
                It invents titles like "Hochzeitsvater" / "Hochzeitsmutter"
                It contradicts itself in this statement: "while the president will always address individuals using appropriate titles based on their gender, there is no longer a distinction made between male and female forms of address within the official discourse."
Q4: Excerpt 1: Misindentifies that the speaker is addressed as "Frau Zuseherinnen und Zuseher" and "Frau Kollegin" 
               It gives only a vague explanation of who is addressed and interrupted
Q4: Excerpt 2: Says that the speaker is addressed as "Herr Präsident" and "Frau Staatssekretärin" which doesnt make sense
               It says that speaker is interrupted multiple times
               It states that the tone as skeptical, critical, and mocking
Q5: Excerpt 1 & 2: Misinterprets parties and roles—expands FPÖ as "Folkspartei Österreich" (Excerpt 1) and "Frac de la Voie Romane" (Excerpt 2), attributes Holzegger's "Vielen Dank." and Seemayer's own speech lines ("Das wollen wir...", "Es braucht da...") to FPÖ interjections, and confuses who holds which position.


Without prompting and with greedy decoding, the model hallucinates a lot and gets stuck in repititon loops
- 

**What I will change next:**
I will try out Qwen 3B instead of Qwen 1.5B to see if it makes a difference

## Experiment template


### Experiment [2] — [short description]
Date: YYYY-MM-DD
Model: [model name + version]
Prompt version: [e.g. v001]
Layer: [baseline | prompted | rag | agents]

**Question asked:**
> ...

**Output:**
> ...

**What I noticed:**
- 
- 

**What I will change next:**
- 

```

---

## Model comparison notes

Note how at least **two models** differ for your material:

| Model          | Strength observed | Weakness observed |
|----------------|-------------------|-------------------|
| Claude         | TODO              | TODO              |
| Gemini         | TODO              | TODO              |
| Qwen 1.5B      | TODO              | TODO              |
| Qwen 3B        | TODO              | TODO              |
| Claude Project | TODO              | TODO              |
