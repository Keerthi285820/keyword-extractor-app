import streamlit as st
from extract_keywords import get_keywords
from utils import generate_links
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io

# Set page config
st.set_page_config(page_title="Keyword Extractor", layout="centered")

# App title
st.title("🔍 Keyword Extractor for Research Papers")
st.markdown("Paste your research paper abstract or introduction below. We'll extract the most important keywords and show a word cloud + research links.")

# Input area
text = st.text_area("📄 Enter Abstract or Intro Here:", height=250)

# Extract keywords
if st.button("🚀 Extract Keywords"):
    if not text.strip():
        st.warning("Please paste some content first.")
    else:
        keyword_scores = get_keywords(text)
        keywords = [kw for kw, _ in keyword_scores]

        st.success("✅ Keywords extracted!")

        # Show keywords with scores
        st.subheader("📌 Extracted Keywords & Scores")
        for kw, score in keyword_scores:
            st.markdown(f"**🔑 {kw}** — *Relevance Score:* {score:.2f}")
            links = generate_links(kw)
            link_line = " | ".join([f"[{name}]({url})" for name, url in links.items()])
            st.markdown(link_line, unsafe_allow_html=True)
            st.markdown("---")

        # Word cloud visualization
        st.subheader("☁️ Word Cloud")
        flattened_keywords = ' '.join(' '.join(kw.split()) for kw in keywords)
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='black',
            colormap='pastel'
        ).generate(flattened_keywords)

        # Show the image
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)

        # Download button
        buf = io.BytesIO()
        wordcloud.to_image().save(buf, format='PNG')
        st.download_button(
            label="📥 Download Word Cloud",
            data=buf.getvalue(),
            file_name="wordcloud.png",
            mime="image/png"
        )

# Footer
st.markdown("<hr><center>💡 Made for Students & Researchers — Powered by KeyBERT + Streamlit</center>", unsafe_allow_html=True)
