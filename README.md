# 🎓 Student Academics Tracker (Teacher Tool)

A web-based Student Progress Tracking System with an AI-powered Teacher Assistant, built using Flask, designed specifically for school teachers to manage student records, generate report cards, and receive intelligent academic guidance.

This project focuses on clarity, simplicity, real classroom usability, and AI-assisted decision support for teachers.

✨ Key Features
📋 Student Management

- Add student details (Name, Roll Number, Class)

- Store academic records permanently using JSON

- View all students in a clean list

📄 Report Card Generation

- Automatically generate school-style report cards

- Subject-wise marks and grades

- Total marks, percentage, and overall grade

- Teacher remarks section

- Printable, professional layout

🤖 AI Teacher Assistant (CampusAssist AI)

- Built-in AI chatbot for teachers

- Provides instant teaching guidance and academic suggestions

- Helps teachers support weak, average, and high-performing students

- Generates clear, helpful and supportive responses.

Designed to reduce teacher effort in:

- Writing remarks

- Planning interventions

- Improving student performance strategies

👩‍🏫 Teacher-Friendly Navigation

- View Report Card for any student anytime

- Persistent data (records remain after restart)

- AI Assistant accessible directly from the dashboard

🏫 Class-wise Filtering

- Filter students by class (e.g., 8A, 9B)

- Helps teachers managing multiple sections efficiently

🔍 Search by Student Name

- Search students by name or by class

- Designed to reduce teacher cognitive load

🧠 Design Philosophy

- Built to mirror real school workflows

- Backend-driven architecture (Flask + Jinja)

- AI used as decision support

- Focused on teachability, maintainability, and explainability

🛠️ Tech Stack

- Frontend: HTML, CSS (Responsive, clean UI)

- Backend: Python, Flask

- Templating: Jinja2

- Data Storage: JSON file (students.json)

- AI Integration: Google Gemini (GenAI API), Prompt Engineering

- Environment: Python Virtual Environment

📂 Project Structure
```bash
student_progress/
│
├── app.py                  # Flask backend + AI integration
├── students.json           # Persistent student data
│
├── templates/
│   ├── index.html          # Dashboard
│   ├── add_students.html   # Add student form
│   ├── students.html       # All students list (search & filter)
│   ├── report.html         # Detailed report card
│   └── ai_chat.html        # AI Teacher Assistant UI
│
├── static/
│   └── styles/
│       └── style.css       # Application styling
│
├── .env                    # Environment variables (API keys)
└── README.md
```

▶️ How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows
venv\Scripts\activate


Mac / Linux
source venv/bin/activate

2️⃣ Install Dependencies
pip install flask python-dotenv google-genai

3️⃣ Run the Application
python app.py


Open in browser:

http://127.0.0.1:5000/

🧪 How It Works (Flow)

- Teacher adds student details

- Backend calculates marks, grade, and remarks

- Data is stored in students.json

Teacher can:

- View all students

- Filter by class

- Search by name

- Generate and view report cards

- Ask CampusAssist AI for teaching and academic guidance

🎯 Use Cases

- School teachers

- Academic record management

- AI-assisted teaching support

- CS teaching aid (Flask, CRUD, AI integration)

- Beginner-friendly school management system

🚀 Future Enhancements

- Student-aware AI insights (AI reads marks and explains performance)

- AI-generated personalized teacher remarks

- Edit / Delete student records

- Attendance management

- PDF export of report cards

- Teacher login system

- Class-wise analytics dashboard