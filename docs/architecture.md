# 🏗 StudyAI Pro Architecture

## Overview

StudyAI Pro follows a multi-agent architecture that combines Retrieval-Augmented Generation (RAG), memory systems, analytics, and AI tutoring to create a personalized learning experience.

Each agent performs a specialized task while collaborating with other agents through an orchestration pipeline.

---

## System Flow

```text
User
 │
 ▼
Flask Web Interface
 │
 ▼
Planner Agent
 │
 ├─────────────┐
 ▼             │
Retrieval Agent│
 │             │
 ▼             │
Tutor Agent    │
 │             │
 ▼             │
Verifier Agent │
 └─────────────┘
 │
 ▼
Memory System
 │
 ▼
Analytics Engine
 │
 ▼
Dashboard
```

---

## Components

### 1. User Interface Layer

**Technology:** Flask, HTML, CSS, JavaScript

Responsibilities:

* PDF uploads
* Chat interaction
* Quiz generation requests
* Flashcard generation requests
* Study roadmap requests
* Analytics visualization

---

### 2. Planner Agent

The Planner Agent acts as the central orchestrator.

Responsibilities:

* Understand user intent
* Determine required workflow
* Route tasks to specialized agents
* Manage agent communication
* Coordinate learning activities

Examples:

* User requests quiz generation
* User asks a tutoring question
* User requests revision notes

The Planner Agent selects the appropriate workflow automatically.

---

### 3. Retrieval Agent

**Technology:** FAISS + Sentence Transformers

Responsibilities:

* Generate embeddings
* Store vectors
* Perform semantic search
* Retrieve relevant document chunks

Benefits:

* Fast document search
* Context-aware responses
* Reduced hallucinations

---

### 4. Tutor Agent

**Technology:** Google Gemini

Responsibilities:

* Answer academic questions
* Generate notes
* Create flashcards
* Generate quizzes
* Build study roadmaps
* Provide explanations

The Tutor Agent receives contextual information from the Retrieval Agent before generating responses.

---

### 5. Verifier Agent

Responsibilities:

* Validate AI-generated content
* Check relevance to source material
* Detect incomplete outputs
* Improve reliability

Benefits:

* Higher response quality
* Better educational accuracy
* Reduced misinformation

---

### 6. Memory System

Responsibilities:

* Store learning history
* Maintain conversation context
* Track completed activities
* Personalize future responses

Benefits:

* Long-term learning support
* Personalized recommendations
* Improved tutoring experience

---

### 7. Analytics Engine

Responsibilities:

* Monitor user activity
* Track quiz performance
* Analyze learning progress
* Identify weak topics

Outputs:

* Performance insights
* Learning recommendations
* Revision suggestions

---

### 8. Dashboard

Provides students with a centralized learning overview.

Features:

* Progress tracking
* Session analytics
* Quiz statistics
* Study recommendations
* Learning trends

---

## Retrieval-Augmented Generation (RAG) Pipeline

```text
PDF Upload
     │
     ▼
Text Extraction
     │
     ▼
Embedding Generation
     │
     ▼
FAISS Vector Database
     │
     ▼
Semantic Retrieval
     │
     ▼
Gemini Response Generation
```

This pipeline ensures that responses are grounded in uploaded study materials rather than relying solely on the language model's general knowledge.

---

## Key Architectural Advantages

* Multi-Agent Design
* Modular Components
* Retrieval-Augmented Generation
* Personalized Learning Memory
* Analytics-Driven Insights
* Scalable Architecture
* Improved Response Reliability
* Student-Centric Learning Experience
