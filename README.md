# ⚡ MockMate: AI Technical Interviewer

**Master your technical interview with an AI engine that adapts to your resume and grills you like a Senior Engineer.**

### 🚀 Live Demo
👉 **[Click here to try MockMate Live](https://mockmate.streamlit.app/)**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🧐 The Problem
Technical interviews are stressful.
* **Static Quizzes** (LeetCode/MCQs) don't test your ability to *explain* concepts.
* **Mock Interviews** with humans are expensive or hard to schedule.
* Most tools ask generic questions, ignoring your specific tech stack.

## 💡 The Solution
MockMate is a **Generative AI Platform** powered by **Google Gemini 2.0 Flash**.
1.  **Context-Aware:** It reads your PDF resume to understand *your* specific skills (e.g., if you know React, it asks about Hooks; if you know Java, it asks about JVM).
2.  **Adaptive Difficulty:** You can choose your level—from **Intern** to **System Architect**.
3.  **Instant Feedback:** It grades your answers (0/10) and provides the "Ideal Answer" instantly.

---

## 📸 Features

### 1. Multi-Level Intelligence
Choose your challenge level:
* 🟢 **Intern / Fresher:** OOPs, Basic Definitions.
* 🟡 **Data Structures:** Time Complexity, Logic.
* 🔴 **System Design:** Scalability, Load Balancing (Senior level).
* 🔵 **Behavioral:** STAR Method questions.

### 2. Glassmorphism UI
Built with a custom CSS engine injected into Streamlit to provide a **Dark Mode, Glass-morphic** aesthetic that feels premium and modern.

### 3. Smart Grading
The AI acts as a "Strict Interviewer." It doesn't just check keywords; it evaluates clarity, depth, and technical accuracy.

---

## 🛠️ Tech Stack
* **LLM Engine:** Google Gemini 2.0 Flash (`google-generativeai`)
* **Frontend:** Streamlit (Python)
* **PDF Parsing:** PyPDF2
* **Hosting:** Streamlit Community Cloud

---

## ⚙️ How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/MockMate.git](https://github.com/YourUsername/MockMate.git)
    cd MockMate
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Key**
    * Create a `.streamlit` folder.
    * Create a `secrets.toml` file inside it.
    * Add your key: `GEMINI_API_KEY = "AIzaSy..."`

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 🤝 Future Scope
* **Voice Mode:** Speak your answers instead of typing (Speech-to-Text).
* **Coding Sandbox:** A built-in code editor to solve DSA problems live.
* **History:** Save past interview scores to track progress.

---

**Made with ❤️ by Vikas Kashyap**