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

| Model          | Strength observed | Weakness observed |
|----------------|-------------------|-------------------|
| Claude         | TODO              | TODO              |
| Gemini         | TODO              | TODO              |
| Qwen 1.5B      | TODO              | TODO              |
| Qwen 3B        | TODO              | TODO              |
| Claude Project | TODO              | TODO              |

---

## Experiment template

```

### Experiment 1 — Testing 5 Questions on 2 Excerpts Without Further Prompting
Date: 2026-11-25
Model: [model name + version]
Prompt version: v1 - prompt only as question with excerpt
Layer: baseline

**Question asked:**
> Which forms of address occur in this excerpt, and who is addressed in each case? Please provide the title, the form of the name (first name/last name), and the gender, as far as it can be recognised from the text for each instance.
Abgeordnete Ines Holzegger (NEOS): Vielen herzlichen Dank, Herr Präsident! Werte Frau Staatssekretärin! Hohes Haus! (Zwischenruf des Abg. Matznetter [SPÖ].) Liebe Zuseherinnen und Zuseher! Aktuell herrscht wieder Goldgräberstimmung, aber es ist nicht so wirklich eine Gräberstimmung, mehr eine Ankaufstimmung. Stellen Sie sich vor: ein Gasthaus am Land. In der Stube sitzt ein sehr freundlicher Herr, der anbietet, Ihren alten Schmuck, Ihr altes Gold zu wirklichen Toppreisen zu kaufen. (Abg. Darmann [FPÖ] – erheitert –: Ja, das ist die übliche Praxis in einem Landgasthaus!) Die Anzeige dafür haben Sie aus dem Postkasten – ein Flyer – beziehungsweise haben Sie es in der Wochenzeitung, der Sie vertrauen, oder auf sozialen Medien – Facebook und so weiter – gesehen. Für ganz viele ältere Menschen wirkt das harmlos und durchaus seriös. Was sie aber nicht wissen: Da geht es nicht immer fair zu. Denn wenn man dann nach dem Verkauf zu Hause ankommt, kommt man vielleicht drauf, dass man gescammt wurde – wir haben es vorhin schon gehört. Dann ist es leider schon zu spät. Der Ankäufer ist weg, wir können ihn nicht mehr finden. Lassen Sie mich auch eines in aller Deutlichkeit sagen: Das hat nichts und rein gar nichts mit fairem Wettbewerb zu tun. Denken wir nur an die Juwelierinnen und Juweliere, die sich an wirklich strenge Regeln halten müssen, und die tagtäglich damit konfrontiert sind, dann in die gleiche Schublade wie diese windigen Goldankäufer, die mobil unterwegs sind, gesteckt zu werden! Es gibt durchaus aus gutem Grund strenge Regeln, aber diese müssen auch für alle gelten. Das ist richtig so, denn besonders beim Gold geht es um jedes Gramm. Jedes Gramm kann wirklich viel Geld bedeuten, das dann am Ende in der Tasche fehlt. Egal ob mobil oder stationär, die Regeln müssen einfach für alle gelten. Darum brauchen wir einfach bessere Kontrollen direkt vor Ort. Die Finanzpolizei, die Marktaufsicht müssen da konsequent durchgreifen. Ja, der Antrag ist ein erster Schritt. Selbstverständlich wollen wir, dass das nicht nur eine Willensbekundung ist, sondern dass wir auch ins Tun kommen. Das erwarten wir uns auch: dass die Umsetzung gut und schnell vonstattengeht. Ich weiß, es ist heute schon relativ spät. Ich weiß nicht, wie viele Zuseherinnen und Zuseher noch via Livestream dabei sind. Ich hoffe aber wirklich inständig, dass mit unserer Arbeit hier, mit der Berichterstattung über die Medien das Thema wirklich ein bisschen breiter in die Öffentlichkeit kommt, denn die Regeln sind eine Sache, aber Awareness ist die andere Sache. Es ist wirklich extrem wichtig, dass in Zukunft weniger Bürgerinnen und Bürger Opfer dieser Scams werden. Weil wir ja schon über die Anträge im Ausschuss sprechen, erlauben Sie mir noch ein paar kurze Sätze zum Kollegen Wurm. Ich finde es spannend, dass genau beim Konsumentenschutzpunkt die beiden Kolleginnen und Kollegen von Ihnen, die ich mir eigentlich im Ausschuss einmal wünschen würde, nicht da sind, nämlich den Kollegen Schiefer und die Kollegin Kolm. Denn ich wüsste wirklich gerne, wofür die FPÖ jetzt steht: Für ein komplett sozialistisch angelegtes Wirtschaftssystem, wo der Staat maximal eingreift (Ruf bei der SPÖ: Was?), oder für das andere, für die wirtschaftliche Freiheit? (Abg. Kaniak [FPÖ]: Für Freiheit! Merk dir das, ein Wort reicht: Freiheit! – Ruf bei der FPÖ: Bei uns hat alles Platz! Wir sind Volkspartei!) Ich weiß es nicht. Es sind irgendwie gemischte Signale, die ich da bekomme: Wurm und Kolm. (Ruf bei der FPÖ: Das ist nur eine Verständnisfrage!) Also vielleicht entscheiden Sie sich da einmal. (Beifall bei den NEOS. – Abg. Kaniak [FPÖ]: Für diese Empfindungsstörungen können wir aber nichts!) Ein letzter Punkt noch zu dem Antrag mit den drei Dezimalstellen bei den Tankstellen. (Abg. Wurm [FPÖ]: Das ist relativ unkompliziert!) Ich habe Ihnen das auch schon im Ausschuss erklärt: Es ist ja interessant, wenn man sich den Antrag – der ist ja öffentlich, den kann sich jeder ansehen – und das, worauf er basiert, anschaut. (Zwischenruf des Abg. Petschnig [FPÖ].) Zur Erinnerung: Wir haben 2026. Der Antrag basiert auf einer Presseaussendung des Arbö von 2009 (Abg. Wurm [FPÖ]: Genau!), in der der Arbö explizit sagt: Wenn die dritte Dezimalstelle gestrichen wird, kann es zu Preissteigerungen kommen. (Abg. Wurm [FPÖ]: Das haben Sie nicht genau gelesen, Frau Kollegin!) – Das wollen Sie? Wirklich? Das wollen Sie? (Beifall bei den NEOS.) Begründet wird es auch damit, dass wir die dritte Dezimalstelle haben, weil ja die Umstellung vom Schilling auf den Euro passiert ist. Ich habe gar nicht gewusst – ich gebe zu, ich bin ein bisschen jünger, aber ich kann mich nicht erinnern –, dass es in so vielen europäischen Ländern vor dem Euro den Schilling gab. (Abg. Wurm [FPÖ]: Nein, aber andere Lokalwährungen!) Denn es ist nicht nur Österreich, das diese dritte Dezimalstelle hat, aber vielleicht habe ich mich da einfach geirrt. (Abg. Steiner [FPÖ]: Es hat die D-Mark gegeben!) Jedenfalls finde ich es gut, dass wir uns heute für bessere Regeln beim mobilen Goldankauf aussprechen und ich hoffe, dass in Zukunft weniger Bürgerinnen und Bürger gescammt werden. – Vielen Dank. (Beifall bei den NEOS. – Abg. Wurm [FPÖ]: Frau Kollegin, Sie haben nichts über das Gold gesagt! – Abg. Holzegger [NEOS] – auf dem Weg zu ihrem Sitzplatz –: Natürlich hab ich etwas übers Gold gesagt!)

**Output:**
> The excerpt has two kinds of address: what the speaker, Ines Holzegger (NEOS), says to people in the chamber, and what other MPs call out to her. The stenographic notes also name people, but those are references rather than address, so they're listed separately at the end.

## 1. Direct address by the speaker

| # | Form of address | Who is addressed | Title / function | Name form | Gender |
|---|---|---|---|---|---|
| 1 | „Herr Präsident!“ | The presiding President of the Nationalrat | Präsident | no name | male („Herr“) |
| 2 | „Werte Frau Staatssekretärin!“ | The state secretary on the government bench | Staatssekretärin | no name | female („Frau“, ending *-in*) |
| 3 | „Hohes Haus!“ | Parliament as a whole | collective form for the chamber | no name | none (collective) |
| 4 | „Liebe Zuseherinnen und Zuseher!“ | Viewers, including those on the livestream | none | no name | both, gender-inclusive pair form |
| 5 | „Stellen Sie sich vor …“ | The audience in general (formal *Sie*) | none | no name | not identifiable |
| 6 | „… die beiden Kolleginnen und Kollegen **von Ihnen** …“ | Abg. Wurm or the FPÖ group | none | no name (pronoun only) | not identifiable from this phrase |
| 7 | „… wofür die FPÖ jetzt steht“ / „Also vielleicht entscheiden **Sie** sich da einmal.“ | The FPÖ group | party name | no name | none (group) |
| 8 | „Ich habe **Ihnen** das auch schon im Ausschuss erklärt“ / „Das wollen **Sie**? Wirklich?“ | Abg. Wurm (FPÖ), who moved the fuel-price motion | none | no name (pronoun only) | male only from context („Kollege Wurm“) |

## 2. Third-person mentions in the speech (talked about, not to)

| Form | Person | Title / function | Name form | Gender |
|---|---|---|---|---|
| „zum Kollegen Wurm“ | Abg. Wurm (FPÖ) | Kollege | last name only | male |
| „den Kollegen Schiefer“ | Abg. Schiefer (FPÖ) | Kollege | last name only | male |
| „die Kollegin Kolm“ | Abg. Kolm (FPÖ) | Kollegin | last name only | female |
| „Wurm und Kolm“ | the same two | none | last names only, no title | not marked here |

## 3. Interjections addressed to the speaker

| Form | Speaker | Addressee | Title / function | Name form | Gender |
|---|---|---|---|---|---|
| „Merk dir das, ein Wort reicht: Freiheit!“ | Abg. Kaniak (FPÖ) | Holzegger | none (informal *du*) | no name | not marked in this phrase |
| „Das haben Sie nicht genau gelesen, **Frau Kollegin**!“ | Abg. Wurm (FPÖ) | Holzegger | Kollegin | no name | female |
| „**Frau Kollegin**, Sie haben nichts über das Gold gesagt!“ | Abg. Wurm (FPÖ) | Holzegger | Kollegin | no name | female |

## 4. Names in the stenographic notes (references, not address)

- **Speaker label:** „Abgeordnete Ines Holzegger (NEOS)“ gives the title in full, first and last name, and the female form *Abgeordnete*.
- **Interjectors:** „Abg. Matznetter [SPÖ]“, „Abg. Darmann [FPÖ]“, „Abg. Kaniak [FPÖ]“, „Abg. Wurm [FPÖ]“, „Abg. Petschnig [FPÖ]“, „Abg. Steiner [FPÖ]“ and „Abg. Holzegger [NEOS]“. Each has the abbreviated title, last name only, and party. The abbreviation *Abg.* doesn't show gender, so it can only be inferred from elsewhere in the text: Wurm is male and Holzegger female.
- **Unnamed callers:** „Ruf bei der SPÖ“ and „Ruf bei der FPÖ“ give no name or gender.

**Pattern:** The President and the state secretary are addressed by function and gendered honorific (*Herr*/*Frau*), with no name. MPs are named with *Kollege*/*Kollegin* plus last name. First names appear only in the speaker label. The heckles switch to *du* (Kaniak) or the nameless *Frau Kollegin* (Wurm).

**What I noticed:**
- 
- 

**What I will change next:**
- 

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
