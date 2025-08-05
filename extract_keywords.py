from keybert import KeyBERT

# Load model once
model = KeyBERT()

def get_keywords(text, num_keywords=10):
    """
    Extract top keywords using KeyBERT.
    """
    keywords = model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')
    return [kw[0] for kw in keywords[:num_keywords]]
