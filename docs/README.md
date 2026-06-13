# StudyAI Pro

StudyAI Pro is an AI-powered learning assistant built using Flask, Gemini, and Retrieval-Augmented Generation (RAG).

It helps students upload study materials and automatically generates quizzes, notes, flashcards, assessments, roadmaps, and personalized study recommendations.

## Features

- Multi-Agent Architecture
- PDF Upload and Processing
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Search
- AI Tutor
- Quiz Generator
- Flashcard Generator
- Assessment Generator
- Revision Notes Generator
- Learning Roadmap Generator
- Study Coach
- Session Analysis
- User Memory
- Analytics Dashboard
- Secure File Uploads
- Automated Testing

## Tech Stack

### Backend
- Flask
- Python 3.13

### AI
- Google Gemini
- Sentence Transformers
- FAISS

### Database
- SQLite

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Testing
- Pytest

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd studyai-pro
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment:

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key
SECRET_KEY=studyai-secret
```

Initialize project:

```bash
python scripts/init_project.py
```

Run application:

```bash
python app.py
```

## Project Structure

studyai-pro/
├── agents/
├── database/
├── memory/
├── orchestrator/
├── scripts/
├── templates/
├── tests/
├── uploads/
├── utils/
├── vector_db/
├── app.py
├── config.py
├── requirements.txt
└── README.md

## API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| / | GET | Home Page |
| /upload | POST | Upload PDF |
| /chat | POST | Ask Tutor |
| /quiz | POST | Generate Quiz |
| /flashcards | POST | Generate Flashcards |
| /notes | POST | Generate Notes |
| /assessment | POST | Generate Assessment |
| /roadmap | POST | Generate Learning Roadmap |
| /dashboard | GET | Analytics Dashboard |

## Testing

Run all tests:

```bash
python -m pytest -v
```

## Competition Highlights

- Multi-Agent Educational AI System
- Retrieval-Augmented Generation
- Personalized Learning Memory
- Analytics Dashboard
- Secure Architecture
- Automated Testing
- Production Logging

