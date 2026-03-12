# ⚖️ LegalEase — AI-Powered Legal Documentation Generator

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Gemini](https://img.shields.io/badge/Google_Gemini-1.5_Pro-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

LegalEase is an intelligent legal assistant that uses **Google Gemini 1.5 Pro** 
to generate professional legal documents instantly based on user inputs.
```

---

## Short Description (for GitHub repo description box)
```
⚖️ AI-powered legal document generator using Google Gemini 1.5 Pro, Flask & Python. Generate contracts, NDAs, lease agreements and more instantly.
```

---

## Topics/Tags (add these in GitHub)
```
python flask gemini-ai legal-documents nlp ai-generator 
google-gemini flask-app legal-tech generative-ai


## 🚀 Features

- 🤖 Powered by Google Gemini 1.5 Pro AI
- 📄 9 Document Types:
  - Employment Contract
  - Non-Disclosure Agreement (NDA)
  - Lease Agreement
  - Service Agreement
  - Partnership Agreement
  - Power of Attorney
  - Freelance Contract
  - Independent Contractor Agreement
  - Cease & Desist Letter
- 🌍 10 Jurisdiction Options (India, USA, UK, Canada, Australia & more)
- ✏️ Editable Document Preview before downloading
- 📥 Multi-Format Downloads — TXT, DOCX, PDF
- 🕐 Document History (last 5 documents)
- 🎨 Professional Blue Dark Theme UI
- 🔒 Secure API key handling with python-dotenv

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| AI Model | Google Gemini 1.5 Pro |
| PDF Export | ReportLab |
| DOCX Export | python-docx |
| API Security | python-dotenv |

## ⚙️ Installation

# Clone the repository
git clone https://github.com/yourusername/legalease.git
cd legalease

# Install dependencies
pip install -r requirements.txt

# Add your API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Run the app
python app.py

## 🔑 Get API Key
Visit https://aistudio.google.com/app/apikey
Create a free Gemini API key and paste it in your .env file

## 📸 Project Structure

legalease/
├── app.py              ← Flask backend
├── requirements.txt    ← Dependencies
├── .env                ← API Key (never commit!)
├── templates/
│   └── index.html      ← Frontend UI
└── static/
    └── style.css       ← Styling

## ⚠️ Disclaimer
AI-generated documents are for reference only.
Always review with a qualified attorney before legal use.

## 👨‍💻 Author
Made by [Your Name]
Powered by Google Gemini AI
```

---

## ⚠️ Important — Add .gitignore file

Create a file called `.gitignore` in your project and add:
```
.env
venv/
__pycache__/
*.pyc
