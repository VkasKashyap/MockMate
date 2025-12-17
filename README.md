⚡ MockMate Ultra: AI Technical Interviewer

MockMate Ultra is a Next-Gen Technical Interview platform powered by Generative AI. Unlike static quiz apps, MockMate reads your resume in real-time and generates context-aware questions tailored to your specific tech stack and experience level.

🚀 Live Demo

👉 Click here to try the App

🧠 How It Works

The application uses a RAG (Retrieval-Augmented Generation) style approach combined with Dynamic Prompt Engineering:

Resume Parsing: Extracts raw text from uploaded PDF resumes using PyPDF2.

Context Injection: Feeds the resume text + selected difficulty level into Google Gemini 2.0 Flash.

Question Generation: Creates 3 unique questions (System Design, DSA, or Behavioral) based on the candidate's profile.

AI Grading: Evaluates the candidate's typed answers, providing a Compatibility Score (0-10) and "Ideal Model Answers".

💎 Key Features

✨ Cyber-Aesthetic UI: A fully custom "Glassmorphism" interface built with CSS injection (Animated backgrounds, Neon accents, Glass cards).

🎚️ Multi-Level Difficulty:

Intern/Fresher (Basic Concepts)

System Design (Scalability & Architecture)

Database Specialist (SQL & ACID)

Behavioral (HR/Leadership)

📝 Instant Feedback Loop: No more guessing. Get immediate critique on your technical accuracy and communication style.

🔐 Secure Architecture: Uses Streamlit Secrets management to handle API keys securely in the cloud.

🛠️ Tech Stack

LLM Engine: Google Gemini 2.0 Flash (via google-generativeai)

Frontend: Streamlit (Python)

Styling: Custom CSS / HTML Injection

Data Processing: PyPDF2

⚙️ Installation & Local Run

Clone the project to run it on your local machine.

# 1. Clone the repository
git clone [https://github.com/YourUsername/MockMate.git](https://github.com/YourUsername/MockMate.git)

# 2. Navigate to directory
cd MockMate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py


Setting up the API Key

Get your free key from Google AI Studio.

Create a folder .streamlit and a file secrets.toml inside it:

# .streamlit/secrets.toml
GEMINI_API_KEY = "Your_AIzaSy_Key_Here"


🔮 Future Scope

Voice Mode: Adding Speech-to-Text to conduct verbal interviews.

Coding Sandbox: Integrating a code editor to run Python/C++ code for DSA questions.

History Tracking: Saving previous interview scores to track progress over time.

<div align="center">
<sub>Built with ❤️ by Vikas Kashyap</sub>
</div>