def bio(text):
    prompt = f"""
role: You are a summarizer of this Bio-related text in DUTCH.
Context: My BIO book & upcoming test.
Task: Summarize all the content given using list, tables, etc. Use the wording from the book and don't add anything else from outside sources.
WAY OF DOING: Don't hold back on length while explaining extra parts of a topic, use the structure to guide yourself in the summary. Bonus if you use the exact wording.
FORMATTING: google docs friendly.
KEY: ONLY GO OVER WHAT IS MENTIONED

Format:

For each topic:

Titel: (Clear heading from book itself)

Simpele uitleg: (Explain in plain Dutch with analogies if helpful)

definities:

Voorbeelden: (use a table, list, etc.)

Belangerijkste boodschap: (One bullet summarizing the most important point)

TEXT:
{text}

Use structure from the book
"""

    return prompt

def fysica(text):
    prompt = f"""
role: You are a summarizer of this fysica-related text in DUTCH.
Context: My fysica book & upcoming test.
Task: Summarize all the content given using list, tables, etc. Use the wording from the book and don't add anything else from outside sources.
Laat alle oefeningen weg, focus op theorie.
Do this chronologically, say what part like 1.1.1 or 1.2.1, etc in the headers. This is a must.
WAY OF DOING: Don't hold back on length while explaining extra parts of a topic, use the structure to guide yourself in the summary. Bonus if you use the exact wording.
FORMATTING: google docs friendly.
KEY: ONLY GO OVER WHAT IS MENTIONED

Format For each topic:

# [Concept Title] (Clear heading from book itself)

## [Simpele uitleg] (Explain in plain Dutch with analogies if helpful)

## [definities]

## [Voorbeelden] (use a table, list, etc.)

## [Belangerijkste boodschap] One bullet summarizing the most important point

TEXT:
{text}
"""
    return prompt

def aardrijkskunde(text):
    prompt = f"""
role: You are a summarizer of this Aarderijkskundig-related text in DUTCH.
Context: My Aarderijkskunde book & upcoming test.
Task: Summarize all the content given using list, tables, etc. Use the wording from the book and don't add anything else from outside sources.
Laat alle oefeningen weg, focus op theorie.
Do this chronologically, say what part like 1.1.1 or 1.2.1, etc in the headers. This is a must.
WAY OF DOING: Don't hold back on length while explaining extra parts of a topic, use the structure to guide yourself in the summary. Bonus if you use the exact wording.
FORMATTING: google docs friendly.
KEY: ONLY GO OVER WHAT IS MENTIONED

Format For each topic:

# [Concept Title] (Clear heading from book itself)

## [Simpele uitleg] (Explain in plain Dutch with analogies if helpful)

## [definities]

## [Voorbeelden] (use a table, list, etc.)

## [Belangerijkste boodschap] One bullet summarizing the most important point

TEXT:
{text}

"""
    return prompt
