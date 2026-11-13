# Milestone 2 — Material and Ethics Note
**13.11.2026**

Dana Gordon, Anna Pably

---

## Your collection

**What is it?**
<!-- Describe the body of material your system will draw on -->
The collection consists of stenographic protocols of debates held in the Viennese parliament. These stenographic protocols detail the sessions, speeches, and interactions between the participants. It also includes public guidelines on gender-fair language, used as a reference for the address annotation scheme.

**Where does it come from?**
<!-- Source(s), institution(s), creator(s), date range -->
These stenographic protocols come from the official Austrian Parliament website ([https://www.parlament.gv.at/](https://www.parlament.gv.at/)) .
The guidelines will be public documents, focused on the guidelines from the City of Vienna (https://www.wien.gv.at/pdf/ma53/medien/leitfaden-richtiges-formulieren.pdf) and further Austrian guidelines (e.g. https://www.donau-uni.ac.at/dam/jcr:2fb47eb6-8681-410b-beb5-d2428fe3c8ec/Sprachleitfaden_UWK_5_Auflage_2025.pdf, https://www.bildung-bgld.gv.at/fileadmin/user_upload/Geschlechtergerechte_Sprache_Leitfaden.pdf).

**How will you prepare it?**
<!-- Cleaning, chunking, OCR, transcription, format — describe your pipeline -->
- First, we will download the PDFs of the protocols
- We will choose debates that are at least 15 minutes long and have at least 2 speakers, because if it is only one person talking, then this person most likely won’t interrupt/be interrupted and will also not address other participants.
- Then we will clean the text
→ Since the layout of these protocols often contains elements such as headers, page numbers, and footnotes, this needs to be cleaned first so only the plain text remains
→ Then we need to segment the text into distinct conversational turns (who speaks, who interrupts, who is addressed) and keep metadata, such as date, speaker, party, role, etc.
- We will annotate a gold standard ourselves with a shared scheme: form of address (title, first or last name, gender-inclusive form), interruptions, calls to order, and who is affected.
-  Since the City of Vienna’s gender-fair language guidelines will serve as a baseline, the text has to be structured in a way so the LLM can compare it against these guidelines
→ Need to preprocess the text so it is easy to extract how participants are addressed or interrupted

**Size and scope**
<!-- Approximate number of documents / images / recordings, word count, etc. -->
The exact number of debates we aim to select is difficult to choose beforehand, since after initial analysis of chosen debates, it became apparent that many of them are rather short and might not all include what we are looking for. In general, we will choose only a few samples at first (approximately 10) so we can annotate by hand as well and compare our results with the LLM’s results for verification.

---

## Ethical considerations

**Copyright and licensing**
<!-- Is the material in the public domain? Under a Creative Commons licence? Used with permission? -->
Since the parliament publishes open data under CC BY 4.0, including datasets on stenographic protocols from the XX. legislative period onwards, the stenographic protocols are considered open data and can be used for research. Furthermore, the guidelines that will be used in this project are public documents of institutions. We will check each document’s terms of use and make sure to cite them appropriately. Texts are sent to external LLM services. Since the material is public, the risk is low, but we state which services we use.

**Consent**
<!-- If the material involves living people or community archives: how was consent obtained? -->
As mentioned above, the stenographic protocols are public documents, so individual explicit consent is not required for processing or analysis. We will, however, still treat individuals with care. The tool describes language and does not judge politicians or parties. No private persons and no personal data beyond public statements are involved.

**Whose voices are present?**
<!-- Who created this material, and whose perspectives does it centre? -->
Within the National Council (Vienna), the voices of elected politicians, speakers from different parties, and parliamentary presidents are present.

**Whose voices are absent or marginalised?**
<!-- Who is missing, and does that matter for your question? -->
Our focus is on the parliament debates, not other settings. Depending on the chosen data, there are perhaps multiple voices that are not included. For example, it might be the case that not all marginalised groups will be included, or voices of the people outside parliament and the parties that were not represented in the debates are also absent. The main focus will be to gather intel about the behaviour towards women vs. men in parliament. On the other hand, our goal is to create a framework that can be modified to suit different domains and tackle other marginalised voices as well.

**Limits you will communicate to users**
<!-- What should users know before trusting the system's outputs? -->
The tool's purpose is to analyse the written texts from the stenographic protocols, so it will not take into account or be able to say anything about the tone of voice, body language, or unrecorded interactions. Furthermore, LLMs are known to hallucinate, exhibit bias, and make interpretation errors. Therefore, the output of the LLMs should always be evaluated by a human. The sample is not very large, and might not be representative of all debates, which is what we aim to examine during our first experiments. Lastly, the tool is not intended to judge individuals or parties and is not a tool for evaluating politicians.
