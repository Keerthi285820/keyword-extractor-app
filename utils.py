def generate_links(keyword):
    """
    Generate resource links for a given keyword.
    """
    return {
        "Wikipedia": f"https://en.wikipedia.org/wiki/{keyword.replace(' ', '_')}",
        "Google Scholar": f"https://scholar.google.com/scholar?q={keyword}",
        "Semantic Scholar": f"https://www.semanticscholar.org/search?q={keyword}"
    }
