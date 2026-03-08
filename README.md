# 📄 Research Paper Summarizer

AI-powered web application that automatically extracts, cleans, summarizes, and analyzes research papers from PDF files.

The system uses Natural Language Processing (NLP) and Transformer models to generate concise summaries, key points, and keywords from academic documents.

---

# 🚀 Features

• Upload research papers in PDF format
• Automatic text extraction from PDF
• Cleaning of academic formatting (references, figures, tables)
• AI-based summarization using **BART Transformer model**
• Key point extraction from summaries
• Keyword extraction using **TF-IDF**
• Simple web interface using **Flask**

---

# 🧠 Technologies Used

Python
Flask
Transformers (HuggingFace)
NLTK
Scikit-learn
pdfplumber

Machine Learning Models:

* `facebook/bart-large-cnn` for summarization
* TF-IDF for keyword extraction

---

# ⚙️ How It Works

1. User uploads a PDF research paper
2. Text is extracted using **pdfplumber**
3. Text is cleaned (references, figures, tables removed)
4. Text is split into chunks for transformer processing
5. BART model generates summaries for each chunk
6. Summaries are merged and summarized again
7. Key points are extracted
8. TF-IDF extracts important keywords

Pipeline:

PDF → Text Extraction → Cleaning → Chunking → AI Summarization → Keywords

---

# 📂 Project Structure

```
Research_Summarizer
│
├── app.py
├── pdf_utils.py
├── summarizer.py
├── keywords.py
├── text_cleaner.py
│
├── templates
│   └── index.html
│
├── uploads
│
└── requirements.txt
```

---

# ▶️ Running the Application

Start the Flask server:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

Upload a PDF research paper and receive:

* Summary
* Key Points
* Keywords

---

# 📊 Example Output

Summary:
A concise AI-generated overview of the research paper.

Key Points:

* Main contributions of the paper
* Important findings
* Methodology summary

Keywords:
Important terms extracted using TF-IDF.

---

# 👨‍💻 Author

Created by **Lambkath**

GitHub:
https://github.com/lambkath13
