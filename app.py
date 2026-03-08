from flask import Flask, render_template, request
import os

from pdf_utils import extract_text_from_pdf
from text_cleaner import clean_text
from summarizer import generate_summary
from keywords import extract_keywords

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    short_summary = ""
    key_points = []
    keywords = []

    if request.method == "POST":

        file = request.files["pdf"]

        if file:

            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            text = extract_text_from_pdf(path)

            text = clean_text(text)

            text = text[:20000]

            short_summary, key_points = generate_summary(text)

            keywords = extract_keywords(text)

    return render_template(
        "index.html",
        short_summary=short_summary,
        key_points=key_points,
        keywords=keywords
    )


if __name__ == "__main__":
    app.run(debug=True)