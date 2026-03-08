from transformers import pipeline
import nltk

nltk.download("punkt")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1
)

MAX_CHUNK = 900


def split_into_chunks(text):

    sentences = nltk.sent_tokenize(text)

    chunks = []
    chunk = ""

    for sentence in sentences:

        if len(chunk) + len(sentence) < MAX_CHUNK:

            chunk += sentence + " "

        else:

            chunks.append(chunk)
            chunk = sentence + " "

    if chunk:
        chunks.append(chunk)

    return chunks


def summarize_text(text):

    chunks = split_into_chunks(text)

    summaries = []

    for chunk in chunks[:10]:

        if len(chunk) < 100:
            continue

        result = summarizer(
            chunk,
            max_length=130,
            min_length=40,
            do_sample=False
        )

        summary = result[0]["summary_text"]

        summaries.append(summary)

    return " ".join(summaries)


def generate_summary(text):

    first_summary = summarize_text(text)

    final = summarizer(
        first_summary,
        max_length=180,
        min_length=60,
        do_sample=False
    )

    final_summary = final[0]["summary_text"]

    sentences = final_summary.split(". ")

    key_points = sentences[:5]

    return final_summary, key_points