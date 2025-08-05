# 🔍 Keyword Extractor for Research Papers

A Streamlit web application that extracts the most relevant keywords from a research paper's **abstract** or **introduction** using **KeyBERT**, and presents them with a **word cloud** and **external research links** (Google Scholar, IEEE Xplore, arXiv).

## 📌 Features

- ✅ Extracts technical keywords using contextual embeddings (BERT-based)
- ☁️ Visualizes keywords in an interactive word cloud
- 🔗 Provides clickable links for deeper research (Google Scholar, IEEE, arXiv)
- 💾 Downloadable word cloud image
- 📚 Built for students, researchers, and paper reviewers

## 🧠 How It Works

1. User pastes the abstract or intro of a paper.
2. The `KeyBERT` model generates relevant keywords using **BERT embeddings**.
3. Keywords are displayed with relevance scores and research links.
4. A **word cloud** visualizes the extracted keywords.
5. Users can download the word cloud image.


## 🛠 Tech Stack

| Tool/Library        | Purpose                              |
|---------------------|--------------------------------------|
| **Streamlit**       | Web app framework                    |
| **KeyBERT**         | Keyword extraction                   |
| **transformers**    | BERT model backend                   |
| **Matplotlib**      | Word cloud rendering                 |
| **WordCloud**       | Word cloud generation                |
| **Python**          | Core logic and utilities             |

## 📂 Project Structure

📁 keyword-extractor-app/
├── app.py # Main Streamlit app
├── extract_keywords.py # Keyword extraction logic using KeyBERT
├── utils.py # Link generator for research portals
├── requirements.txt # Python dependencies
├── README.md # Project documentation

 Generated Keyword Links
Each keyword is linked to:

🔍 Google Scholar

📘 IEEE Xplore

📄 arXiv

Helpful for faster exploration of similar works or literature review.

📸 Preview

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📜 License
This project is open-source under the MIT License.

🙌 Acknowledgements
KeyBERT

Streamlit

HuggingFace Transformers


