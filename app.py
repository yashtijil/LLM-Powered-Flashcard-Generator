import streamlit as st
import os

st.set_page_config(page_title="Flashcard Generator")
st.title("Flashcard Generator")
input_method = st.radio("Choose input method:", ["Upload file", "Paste text manually"])

text_content = ""

if input_method == "Upload file":
    uploaded_file = st.file_uploader("Upload a .pdf or .txt file", type=["pdf", "txt"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".txt"):
            text_content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.name.endswith(".pdf"):
            import pdfplumber
            with pdfplumber.open(uploaded_file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
                text_content = text
else:
    text_content = st.text_area("Paste text here:", height=250)

# Number of flashcards
num_flashcards = st.number_input("Number of flashcards", min_value=1, max_value=10, value=5)

# Submit button
if st.button("🚀Generate Flashcards"):
    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(text_content)
    with open("num.txt", "w") as f:
        f.write(str(num_flashcards))
    st.success("Model will now generate flashcards. Please wait...")

# Refresh
if st.button("🔄 Refresh Output"):
    if os.path.exists("output.txt"):
        with open("output.txt", "r", encoding="utf-8") as f:
            flashcards = f.read()
        st.subheader("🧠 Generated Flashcards:")
        st.text_area("Flashcards Output", flashcards, height=400)
    else:
        st.error("❌ No flashcards found. Please run the model cell in Colab first.")
