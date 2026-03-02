# 🤖 AI Resume & Interview Assistant

An AI-powered Full Stack Web Application that helps users:

- Generate professional resumes
- Analyze uploaded resumes
- Calculate ATS (Applicant Tracking System) score
- Get keyword matching insights
- Download resumes as PDF

Built using **React (Frontend)** and **Flask (Backend)**.

---

## 🚀 Features

### ✅ AI Resume Generator
Generate resume content dynamically and export as PDF.

### ✅ ATS Score Checker
- Compare resume with job description
- Calculate ATS match percentage
- Display matched keywords

### ✅ Resume Upload Analyzer
- Upload PDF resume
- Extract text
- Detect technical skills
- Get improvement suggestions

### ✅ PDF Generation
Download resume in professional PDF format.

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- JavaScript
- CSS
- Fetch API

### Backend
- Flask
- Flask-CORS
- PyPDF2
- ReportLab
- Gunicorn (for production)

---

# 📂 Project Structure

AI-Resume-Assistant
│
├── client/      → React Frontend
│   ├── src/
│   └── package.json
│
├── server/      → Flask Backend
│   ├── app.py
│   ├── ats.py
│   ├── ai_generator.py
│   ├── resume_analyzer.py
│   ├── pdf_generator.py
│   └── requirements.txt
│
├── .gitignore
└── README.md

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Assistant.git
cd AI-Resume-Assistant
```
