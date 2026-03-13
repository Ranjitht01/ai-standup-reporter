# 🤖 AI Daily Standup Reporter

## 📌 Project Description
AI Daily Standup Reporter is a web-based application that helps teams track daily standup updates.  
Users can submit their work updates, store them in a MySQL database, and view summaries through an interactive dashboard built using Streamlit.

The system collects the following standup information:
- Work completed yesterday
- Work planned for today
- Any blockers preventing progress

The application stores the data and generates a readable summary of team activity.

---

## 🚀 Features

- Submit daily standup reports
- Store reports in MySQL database
- Dashboard showing team statistics
- Detect blockers in reports
- Generate AI-style summaries
- Clean and interactive web interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- MySQL
- Pandas

---

## 📊 System Workflow

User → Web Interface (Streamlit)  
↓  
Python Backend  
↓  
MySQL Database  
↓  
Dashboard + AI Summary  

---

## 📂 Project Structure
ai-standup-reporter
│
├── standup_app.py
├── standup_reporter.py
├── agentic_ai.py
└── README.md