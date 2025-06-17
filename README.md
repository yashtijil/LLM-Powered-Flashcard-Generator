# 🧠 AI Flashcard Generator

This project generates study flashcards from educational text using the powerful **Mistral-7B-Instruct** language model. It features a user-friendly **Streamlit interface** and uses **Google Colab** to run heavy model inference. Generated flashcards are automatically saved to a file and can be viewed in the interface.

---

## 📦 Features

- Upload `.txt` or `.pdf` files OR paste raw text
- Uses Mistral-7B-Instruct for high-quality Q&A generation
- Generates 5–10 flashcards per input (adjustable)
- Saves flashcards to a text file
- Web-based interface built using Streamlit + Pyngrok
- Model runs on Colab backend (lightweight frontend on local device)

---

## 🚀 How It Works

1. **Launch Streamlit App**:
   - Accepts user input (file or text)
   - Saves input text as `input.txt` to Colab file system

2. **Colab Model Inference**:
   - Mistral model loads input from `input.txt`
   - Generates flashcards and saves output to `output.txt`

3. **Streamlit Output**:
   - Reads from `output.txt` and displays the flashcards
   - Allows download of the generated flashcards

---

## 🛠 Setup Instructions

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/yashtijil/LLM-Powered-Flashcard-Generator
cd LLM-Powered-Flashcard-Generator
```

### 🔹 2. Install Dependencies
Install required packages using pip:
```bash
pip install -r requirements.txt
```

### 🔹 3. Launch the Streamlit App (Local)
```
streamlit run app.py
```
This will start a local server. If you're using Colab, the Streamlit app will automatically be tunneled via Pyngrok and the public URL will be shown.


### 🔹 4. Run the Model in Colab
- Open the provided Colab notebook: model_runner.ipynb
- Click Run All after input has been submitted in Streamlit
- The model reads input.txt, generates flashcards, and writes to output.txt
- Return to the Streamlit app to view/download results

### 🔹 5. 📁 Project Structure
```text
flashcard-generator/
│
├── app.py                # Streamlit UI
├── LLM_Flashcard.ipynb   # Colab notebook to run the model
├── requirements.txt      # All dependencies
├── sample_input.txt      # Auto-saved input file
├── sample_output.txt     # Generated flashcards
└── README.md             # Project documentation
```
### 🔹 6. 🔐 Model Details
**Model Used**: [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)

Inference Backend: Google Colab GPU

Memory Efficient: Loaded with 4-bit quantization via bitsandbytes
