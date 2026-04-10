# AI Website Auditor

![AI Website Auditor Banner](https://raw.githubusercontent.com/Gailanimesh/ai-website-auditor/main/frontend/src/assets/vite.svg)

A high-fidelity, full-stack website analysis suite that combines technical heuristic scanners with AI-powered semantic insights. Built with a premium **Glassmorphic** React frontend and a real-time WebSocket-enabled FastAPI backend.

---

## ✨ Features

- **🕷️ Deep Web Scraping**: Powered by Playwright and BeautifulSoup to handle JavaScript-heavy sites.
- **🔍 Technical Heuristics**: Automatic evaluation of:
  - **SEO**: Title tags, meta descriptions, and heading hierarchies.
  - **Content**: Word count and density analysis.
  - **Accessibility**: Image alt-text and semantic HTML checks.
- **🧠 AI Executive Summary**: Intelligent interpretation of audit data using **LangChain** and **Groq (Llama-3)**.
- **📡 Real-time Streaming**: Live WebSocket logs that show every step of the audit as it happens.
- **🎨 Glassmorphic UI**: Ultra-clean, macOS-inspired interface with animated background orbs and translucent panels.
- **🗄️ Database Tracking**: Persistent storage of every audit using **PostgreSQL** and SQLAlchemy.

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: React (Vite)
- **Styling**: Tailwind CSS v4 (Light Mode Glassmorphism)
- **Icons**: Lucide React
- **Routing**: React Router v7

### Backend
- **Framework**: FastAPI (Asynchronous Python)
- **Scraper**: Playwright (Synchronous thread-pool isolated)
- **AI**: LangChain & Groq API (Llama-3-8b)
- **Database**: PostgreSQL
- **Real-time**: WebSockets

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js & npm
- PostgreSQL installed and running
- **Groq API Key** (Get one at [console.groq.com](https://console.groq.com))

### 1. Backend Setup
1. Navigate to the root directory.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root:
   ```env
   GROQ_API_KEY=your_key_here
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/website_auditor
   ```
5. Run the server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

### 2. Frontend Setup
1. Open a new terminal and navigate to `frontend/`:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

---

## 🏗️ Architecture

- **WebSockets**: The frontend maintains a persistent connection to the backend, allowing it to stream logs such as "🕸️ Scraping..." and "🧠 Reasoning..." before the final JSON result is delivered.
- **Windows Async Patch**: The scraper uses an isolated thread pool to execute Playwright, avoiding common `asyncio` process spawning issues on Windows platforms.

## 📄 License
MIT License. Feel free to use and extend!

---
*Created by [Gailanimesh](https://github.com/Gailanimesh)*
