from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text, num_keywords=10):

    vectorizer = TfidfVectorizer(stop_words="english")

    X = vectorizer.fit_transform([text])

    feature_names = vectorizer.get_feature_names_out()

    scores = X.toarray()[0]

    pairs = list(zip(feature_names, scores))

    pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

    keywords = [w for w, s in pairs[:num_keywords]]

    return keywords