# 🧠 AI OCR Extractor (FastAPI + React)

An AI-powered OCR (Optical Character Recognition) web application that extracts text from images and PDFs, processes it using AI, and returns structured data.

---

## 🚀 Features

- 📄 Upload Image (JPG, PNG) or PDF
- 🔍 Extract text using OCR (Tesseract)
- 🧠 AI-based parsing of extracted text
- 📊 Structured JSON output
- ⚡ FastAPI backend for high performance
- 🎨 React frontend for user interaction
- 🔗 Real-time frontend-backend integration
- 🌐 CORS-enabled API support

---

## 🏗️ Tech Stack

### Backend:
- FastAPI
- Python
- Tesseract OCR
- PyMuPDF / PDF processing
- AI Parsing Logic (custom / GPT-ready)

### Frontend:
- React.js
- Axios
- HTML/CSS

---

## 📂 Project Structure
ai-ocr-extractor/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── routes/
│ │ │ └── upload.py
│ │ ├── services/
│ │ │ ├── ocr_service.py
│ │ │ ├── pdf_service.py
│ │ │ └── ai_parser.py
│ │
│ └── uploads/
│
├── frontend/
│ ├── src/
│ │ └── App.js
│ └── package.json
│
└── README.md


---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/deepanshu-arya/Ai-Ocr-Extractor.git
cd ai-ocr-extractor

🔹 2. Backend Setup
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
🔹 3. Install Tesseract OCR

Download & install:
👉 https://github.com/tesseract-ocr/tesseract

Add to PATH (IMPORTANT)

🔹 4. Run Backend
uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000
🔹 5. Frontend Setup
cd ../frontend

npm install
npm start

Frontend will run at:

http://localhost:3000
🔌 API Endpoint
Upload File
POST /upload
Request:
Form-data
Key: file
Response:
{
  "data": {
    "items": [...],
    "total": 123
  }
}
