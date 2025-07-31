# 🧾 End-To-End Insurance Clause Query System 🚀

This project is built as part of a Hackathon challenge where the goal is to process **unstructured natural language insurance queries** and return relevant **insurance clause decisions** (e.g. claim approved or rejected) from uploaded policy PDFs.

---

## ✅ Features

- 🔍 Ask natural language questions about insurance policies
- 📄 PDF policy clause parsing with LangChain
- 🧠 Local LLM support using **Ollama** (Mistral or LLaMA models)
- 🧠 Semantic search with **FAISS + HuggingFace MiniLM Embeddings**
- 🌐 Fully functional Flask backend
- 🎨 Clean Tailwind-based HTML UI
- 📤 Upload & query from 5+ insurance PDFs
- ⚙️ Amount extraction from clause text using regex

---

## ⚙️ Tech Stack

| Component         | Tool/Library                          |
|------------------|----------------------------------------|
| Backend          | Flask                                  |
| LLM Engine       | Ollama (Mistral / LLaMA 2)             |
| Vector Store     | FAISS                                  |
| Embeddings       | HuggingFace MiniLM (`all-MiniLM-L6-v2`)|
| PDF Processing   | LangChain + PyMuPDF                    |
| UI               | HTML + Tailwind CSS                    |

---

## 🗂️ Folder Structure

chatbot/
│
├── app.py # Flask backend logic
├── templates/
│ └── index.html # Tailwind-based UI
├── documents/ # Uploaded insurance PDFs
├── utils/ # Model, vector store, prompt logic (optional)
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md # You're reading it!



---

## 🧠 How It Works

1. User enters a natural language insurance-related query.
2. LangChain searches vectorized chunks from PDFs using FAISS.
3. Query + top documents are passed to Ollama model for reasoning.
4. The model returns:
   - ✅ Decision (approved/rejected)
   - 💰 Extracted amount (if any)
   - 🧾 Justification with clause

---

## 🚀 Local Setup Instructions

### ✅ 1. Clone the repo
```bash
git clone https://github.com/code-with-krish/End-To-End-Hackathon-Project.git
cd End-To-End-Hackathon-Project


# setup Virtual Environment
conda create -n venv python=3.10 -y
conda activate venv


# Install requirements.txt
pip install -r requirements.txt


# Download & Run Ollama model
ollama run llama3.2:1b


#  Run the Flask app
python app.py


#📄 Example Queries You Can Ask
"Can I claim hospitalization for my 70-year-old father?"

"Is maternity covered under this policy?"

"Will the policy cover COVID treatment in Mumbai?"

"Can I claim ₹25,000 for physiotherapy?"


# Sample Output
Status: rejected
Amount: ₹0
Justification: Insured person’s age does not fall within the specified range (03 months to 90 years) as per clause 3 of Schedule of Benefits.




🤝 Team Members
1. Krishna Kanta Maiti — Backend Architect, LLM & LangChain Integration, Ollama Setup, Clause Extraction, Flask API, Vector Store & Embeddings
2.Subhadin Bera - Frontend Architecture


Hackathon Organizer: HackRx 5.0 (Bajaj Finserv)

