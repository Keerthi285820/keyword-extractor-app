from keybert import KeyBERT

model = KeyBERT()

def get_keywords(text, num_keywords=10):
    return model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        use_maxsum=True,
        nr_candidates=20,
        top_n=num_keywords
    )
