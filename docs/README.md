# 🎓 StudyAI Pro

## AI-Powered Multi-Agent Learning Assistant

StudyAI Pro is an intelligent educational platform that transforms study materials into personalized learning experiences using Multi-Agent AI, Retrieval-Augmented Generation (RAG), memory systems, and advanced analytics.

Built with Flask, Google Gemini, FAISS, and Sentence Transformers, StudyAI Pro helps students learn faster, revise smarter, and track their academic progress through autonomous AI agents.

---

## 🚀 Problem Statement

Students spend significant time reading lengthy PDFs, creating notes, preparing quizzes, and organizing revision schedules.

Traditional learning methods often lead to:

* Information overload
* Inefficient revision
* Poor knowledge retention
* Lack of personalized guidance
* Difficulty identifying weak topics

---

## 💡 Solution

StudyAI Pro automates the learning process by deploying specialized AI agents that collaborate to analyze documents, generate learning resources, and guide students throughout their study journey.

Students simply upload a PDF and receive:

* Smart Revision Notes
* Flashcards
* Quizzes
* Assessments
* Personalized Learning Roadmaps
* AI Tutoring Support
* Progress Analytics
* Study Recommendations

---

# 🤖 Multi-Agent Architecture

### 📄 Document Analysis Agent

Processes uploaded PDFs and extracts key concepts, topics, and learning objectives.

### 📝 Notes Agent

Generates concise, structured revision notes from study materials.

### 🎴 Flashcard Agent

Creates active-recall flashcards for effective revision.

### ❓ Quiz Agent

Generates adaptive quizzes to evaluate understanding.

### 📊 Assessment Agent

Creates comprehensive assessments and learning evaluations.

### 🗺 Roadmap Agent

Builds personalized learning paths and study schedules.

### 👨‍🏫 Tutor Agent

Provides contextual AI tutoring using Retrieval-Augmented Generation (RAG).

### 🎯 Study Coach Agent

Analyzes learning behavior and recommends study improvements.

### 📈 Analytics Agent

Tracks performance and visualizes learning progress.

---

# ✨ Features

## Learning Features

* PDF Upload & Processing
* AI Tutor
* Quiz Generator
* Flashcard Generator
* Assessment Generator
* Revision Notes Generator
* Learning Roadmap Generator
* Personalized Study Coach

## AI Features

* Multi-Agent Architecture
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* User Memory
* Context-Aware Responses
* Personalized Recommendations

## Analytics

* Session Analysis
* Learning Progress Tracking
* Performance Dashboard
* Knowledge Insights

## Security

* Secure File Uploads
* Environment Variable Protection
* Input Validation
* Production Logging

## Quality Assurance

* Automated Testing
* Modular Architecture
* Scalable Design

---

# 🏗 System Architecture

```text
Student Uploads PDF
        │
        ▼
Document Analysis Agent
        │
        ▼
Embedding Generation
        │
        ▼
FAISS Vector Database
        │
        ▼
RAG Retrieval Layer
        │
        ▼
 ┌───────────────────────┐
 │      AI Agents        │
 ├───────────────────────┤
 │ Notes Agent           │
 │ Flashcard Agent       │
 │ Quiz Agent            │
 │ Assessment Agent      │
 │ Roadmap Agent         │
 │ Tutor Agent           │
 │ Study Coach Agent     │
 │ Analytics Agent       │
 └───────────────────────┘
        │
        ▼
 Personalized Learning Experience
```

---

# 🛠 Technology Stack

## Backend

* Python 3.13
* Flask

## Artificial Intelligence

* Google Gemini
* Sentence Transformers
* FAISS
* Retrieval-Augmented Generation (RAG)

## Database

* SQLite

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Testing

* Pytest

---

# 📂 Project Structure

```text
studyai-pro/
│
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
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone <repository-url>
cd studyai-pro
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
SECRET_KEY=studyai-secret
```

## Initialize Project

```bash
python scripts/init_project.py
```

## Run Application

```bash
python app.py
```

---

# 🔌 API Endpoints

| Endpoint    | Method | Description               |
| ----------- | ------ | ------------------------- |
| /           | GET    | Home Page                 |
| /upload     | POST   | Upload PDF                |
| /chat       | POST   | AI Tutor Chat             |
| /quiz       | POST   | Generate Quiz             |
| /flashcards | POST   | Generate Flashcards       |
| /notes      | POST   | Generate Notes            |
| /assessment | POST   | Generate Assessment       |
| /roadmap    | POST   | Generate Learning Roadmap |
| /dashboard  | GET    | Analytics Dashboard       |

---

# 🧪 Testing

Run all tests:

```bash
python -m pytest -v
```

---

# 🏆 Competition Highlights

* Multi-Agent Educational AI Platform
* Retrieval-Augmented Generation (RAG)
* Personalized Learning Memory
* Semantic Search with FAISS
* Intelligent Study Coaching
* Learning Analytics Dashboard
* Secure Architecture
* Automated Testing Pipeline
* Production Logging

---

# 🔮 Future Enhancements

* Voice-Based Learning Assistant
* Multi-Language Support
* Learning Gap Detection
* Autonomous Revision Scheduling
* Mobile Application
* Collaborative Study Rooms
* Advanced Knowledge Graph Visualization
* Predictive Exam Preparation

---

# 👨‍💻 Developer

**S. DEVI VARA PRASAD REDDY**

Building AI systems that make education smarter, more personalized, and more accessible.

---

# 📜 License

MIT License
