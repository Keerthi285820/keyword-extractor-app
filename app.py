import streamlit as st
from extract_keywords import get_keywords
from utils import generate_links
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# App title
st.set_page_config(page_title="Keyword Extractor", layout="centered")
st.title("🔍 Keyword Extractor for Research Papers")
st.markdown("Paste the abstract/introduction of a research paper below. We'll extract important keywords and provide links to explore more!")

# Text input
text = st.text_area("📄 Enter Abstract or Intro", height=250)

# Extract button
if st.button("🚀 Extract Keywords"):
    if not text.strip():
        st.warning("Please paste some text to analyze.")
    else:
        keywords = get_keywords(text)
        st.success("Keywords extracted successfully!")

        st.subheader("📌 Extracted Keywords & Resources")

        for kw in keywords:
            st.markdown(f"**🔑 {kw}**")
            links = generate_links(kw)
            link_line = " | ".join([f"[{name}]({url})" for name, url in links.items()])
            st.markdown(link_line, unsafe_allow_html=True)
            st.markdown("---")

        # Word Cloud
        st.subheader("☁️ Word Cloud")
        text_for_cloud = ' '.join(keywords)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_cloud)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)

# Footer
st.markdown("<br><hr><center>Made for Students & Researchers ❤️</center>", unsafe_allow_html=True)
