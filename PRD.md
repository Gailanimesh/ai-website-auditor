📄 PRD: AI Website Auditor Agent
🧩 1. Product Overview

Product Name: AI Website Auditor Agent

Description:
A web-based system that allows users to input a website URL and receive an AI-generated audit report including SEO analysis, content quality evaluation, and accessibility checks. Results are streamed in real-time using WebSockets.

🎯 2. Goals
Automate website auditing using AI agents
Provide real-time feedback to users
Build a scalable backend using FastAPI
Use LangChain for tool-based reasoning
Store audit history using PostgreSQL + SQLAlchemy
👤 3. Target Users
Developers
SEO analysts
Content creators
Students learning AI + scraping
⚙️ 4. Core Features
4.1 Website Input
User enters URL
Validate URL format
4.2 Web Scraping Engine
Fetch HTML content
Extract:
Title
Meta tags
Headings
Images
Paragraph text
4.3 AI Agent (LangChain)

Agent Responsibilities:

Decide tool execution order
Combine outputs
Generate insights
4.4 Tools
🔍 SEO Tool
Title length check
Meta description check
Keyword presence
Heading structure
📝 Content Tool
Readability
Content length
Summary generation
♿ Accessibility Tool
Missing alt tags
Basic semantic checks
4.5 Real-Time Streaming (WebSocket)
Show progress:
“Scraping started…”
“Analyzing SEO…”
“Generating report…”
4.6 Report Output
Final structured JSON:
{
  "seo_score": 75,
  "content_score": 80,
  "accessibility_score": 65,
  "suggestions": []
}
4.7 Database Storage
Store:
URL
Results
Timestamp
🧠 5. System Architecture
Frontend (React)
   ↓ WebSocket + HTTP
Backend (FastAPI)
   ↓
LangChain Agent
   ↓
Tools (SEO / Content / Accessibility)
   ↓
Scraper (Playwright / BeautifulSoup)
   ↓
PostgreSQL Database
🪜 PHASED EXECUTION PLAN (Agent-Friendly)

This is the most important part 👇

🚀 Phase 1: Project Setup (Foundation)
Tasks:
Create FastAPI app
Setup folder structure
Install dependencies:
fastapi
uvicorn
sqlalchemy
psycopg2
langchain
beautifulsoup4 / playwright
Deliverables:
/health endpoint working
Basic server running
🚀 Phase 2: Scraper Module
Tasks:
Build scraper.py
Extract:
title
meta description
headings
images
Deliverables:
{
  "title": "...",
  "headings": [...],
  "images": [...]
}
🚀 Phase 3: Tool Implementation
Tasks:
Create:
seo_tool.py
content_tool.py
accessibility_tool.py
Deliverables:

Each tool returns:

{
  "score": number,
  "issues": [],
  "suggestions": []
}
🚀 Phase 4: LangChain Agent
Tasks:
Create agent with tools
Define tool calling logic
Deliverables:
Agent takes scraped data
Returns combined report
🚀 Phase 5: API Integration
Tasks:
Create endpoint:
POST /audit
Connect:
scraper
agent
tools
🚀 Phase 6: WebSocket Integration
Tasks:
Create /ws endpoint
Stream logs:
scraping
analysis
results
🚀 Phase 7: Database Integration
Tasks:
Setup PostgreSQL
Create Audit model
Store results
🚀 Phase 8: Frontend (React)
Tasks:
URL input form
WebSocket connection
Live updates panel
Results display
🚀 Phase 9: Advanced Features (Optional but Powerful)
Add:
Multi-page crawling
Competitor comparison
PDF report generation
Authentication (login system)
🧪 6. Non-Functional Requirements
Fast response time (<5s for small sites)
Modular code
Beginner-readable structure
Scalable design
⚠️ 7. Constraints
Avoid heavy crawling initially
Use simple heuristics for scoring
Keep AI usage controlled (cost-aware)
🧠 8. Agent Instructions (VERY IMPORTANT)

Use this as prompt for your coding agent 👇

🧾 AGENT PROMPT
You are building an AI Website Auditor system.

Tech Stack:
- Backend: FastAPI
- AI: LangChain agents
- Scraping: BeautifulSoup or Playwright
- Database: PostgreSQL with SQLAlchemy
- Frontend: React with WebSocket

Follow these rules:
1. Build modular, readable code
2. Follow the defined folder structure
3. Implement phase by phase
4. Add comments explaining logic
5. Do not skip steps
6. Ensure each module is testable independently

Start with Phase 1: FastAPI setup.
💬 Real Talk (important)

You’re doing something very high-level for a beginner — which is awesome.

But:
👉 Don’t rush phases
👉 Run code at every step
👉 Break things → fix them → learn