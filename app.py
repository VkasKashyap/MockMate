import streamlit as st
import google.generativeai as genai
import PyPDF2
import time

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="MockMate Ultra",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "WORLD CLASS" CSS INJECTION ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;500;700;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #0f172a);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }
    
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    ::-webkit-scrollbar {
        width: 8px;
        background: #0f172a;
    }
    ::-webkit-scrollbar-thumb {
        background: #3b82f6;
        border-radius: 4px;
    }

    .hero-container {
        text-align: center;
        padding: 60px 0;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(to right, #60a5fa, #c084fc, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
        margin-bottom: 10px;
        text-shadow: 0 0 80px rgba(192, 132, 252, 0.3);
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #94a3b8;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
    }

    .glass-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    
    .glass-container:hover {
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
    }

    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
        width: 100%;
        text-transform: uppercase;
    }
    
    .stButton > button:hover {
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
        transform: scale(1.02);
    }

    .score-card {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
        border: 1px solid #10b981;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    @keyframes popIn {
        0% {transform: scale(0.8); opacity: 0;}
        100% {transform: scale(1); opacity: 1;}
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

</style>
""", unsafe_allow_html=True)

# 2. HERO SECTION
st.markdown("""
<div class="hero-container">
    <div class="hero-title">MockMate Ultra</div>
    <div class="hero-subtitle">The next-generation AI interviewer. Select your level and prove your skills.</div>
</div>
""", unsafe_allow_html=True)

# 3. API & SETTINGS LOGIC
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    with st.expander("🔐 Unlock the Experience (API Key)"):
        api_key = st.text_input("Gemini API Key", type="password", placeholder="Paste your AIzaSy... key here")

# 4. FUNCTIONS
def extract_text(uploaded_file):
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except:
        return None

def generate_questions(resume_text, category):
    base_prompt = f"""
    Act as a Senior Technical Interviewer at a Tier-1 Tech Company.
    Candidate's Resume: {resume_text[:3000]}
    
    Generate 3 {category} interview questions.
    """
    
    # --- DYNAMIC INSTRUCTIONS FOR LEVELS ---
    if category == "Intern / Fresher (Easy)":
        instruction = "Focus on basic definitions, OOP concepts, and simple logic. Avoid complex system design."
    elif category == "Data Structures & Algo (Medium)":
        instruction = "Focus on Arrays, Trees, HashMaps, and Time Complexity. Ask for logic, not code."
    elif category == "System Design (Hard)":
        instruction = "Focus on Scalability, Load Balancing, Database Sharding, and Caching."
    elif category == "Senior / Architect (Expert)":
        instruction = "Focus on Microservices patterns, Failure modes, Cloud-native tradeoffs, and high-level decision making."
    elif category == "Database & SQL (Specialist)":
        instruction = "Focus on Normalization, ACID properties, Indexing strategies, and complex JOIN scenarios."
    elif category == "Behavioral / Leadership":
        instruction = "Use the STAR method. Focus on conflict resolution, failure, and project ownership."
    else: # Trivia
        instruction = "Rapid fire technical trivia. One sentence answers expected."

    final_prompt = f"{base_prompt}\n{instruction}\nOutput format: Just the numbered list of 3 questions."
    
    model = genai.GenerativeModel("gemini-flash-latest")
    response = model.generate_content(final_prompt)
    return response.text

def get_feedback(questions, answers):
    prompt = f"""
    You are evaluating a candidate.
    Questions: {questions}
    Answers: {answers}
    
    Strictly follow this output format (Do not use markdown headers #, just bold text):
    
    SCORE: [X]/10
    
    STRENGTHS:
    [List strengths]
    
    WEAKNESSES:
    [List weaknesses]
    
    IDEAL ANSWER (For the hardest question):
    [Concise technical answer]
    """
    model = genai.GenerativeModel("gemini-flash-latest")
    response = model.generate_content(prompt)
    return response.text

# --- MAIN LAYOUT ---

if "questions" not in st.session_state:
    st.session_state.questions = None
    st.session_state.current_category = None

# Using a centered layout for the initial state for maximum impact
if st.session_state.questions is None:
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1. Upload Resume")
        uploaded_file = st.file_uploader("Upload PDF", type="pdf", label_visibility="collapsed")
    with col2:
        st.markdown("### 2. Select Protocol")
        interview_type = st.selectbox(
            "Difficulty / Track",
            [
                "Intern / Fresher (Easy)",
                "Data Structures & Algo (Medium)",
                "System Design (Hard)",
                "Senior / Architect (Expert)",
                "Database & SQL (Specialist)",
                "Behavioral / Leadership",
                "Rapid Fire Trivia"
            ],
            label_visibility="collapsed"
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # Centered Button
    st.write("")
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if uploaded_file and api_key:
            genai.configure(api_key=api_key)
            if st.button("INITIATE SEQUENCE ⚡"):
                with st.spinner("🔄 Neural Network Activating..."):
                    resume_text = extract_text(uploaded_file)
                    if resume_text:
                        st.session_state.questions = generate_questions(resume_text, interview_type)
                        st.session_state.current_category = interview_type
                        st.rerun()

# --- INTERVIEW MODE UI (Split Screen) ---
else:
    # Top Bar: Reset Button
    if st.button("⬅️ New Interview"):
        st.session_state.questions = None
        st.rerun()
    
    col_q, col_a = st.columns([1, 1], gap="large")
    
    with col_q:
        st.markdown(f"""
        <div class="glass-container" style="border-left: 5px solid #c084fc;">
            <h3 style="color: #c084fc; margin-top:0;">🤖 AI Question Stream</h3>
            <p style="opacity: 0.8; font-size: 0.9rem;">Category: {st.session_state.current_category}</p>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <div style="font-size: 1.15rem; line-height: 1.8;">
                {st.session_state.questions.replace(chr(10), '<br>')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_a:
        with st.form("answer_form"):
            st.markdown("### 🎤 Candidate Terminal")
            user_answer = st.text_area("Input response vector...", height=300, placeholder="Explain your logic here...")
            submit = st.form_submit_button("ANALYZE RESPONSE 🚀")
            
        if submit:
            with st.spinner("⚠️ Evaluating technical accuracy..."):
                feedback = get_feedback(st.session_state.questions, user_answer)
                
                # Extract Score (Simple parsing)
                try:
                    score = feedback.split("/10")[0].split()[-1]
                except:
                    score = "?"

            # RESULT CARD
            st.markdown(f"""
            <div class="score-card">
                <div style="font-size: 1rem; text-transform: uppercase; letter-spacing: 2px;">Compatibility Score</div>
                <div style="font-size: 4rem; font-weight: 800;">{score}/10</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="glass-container">
                {feedback.replace(chr(10), '<br>')}
            </div>
            """, unsafe_allow_html=True)

# Footer
st.write("")
st.write("")
st.markdown('<div style="text-align: center; opacity: 0.5; font-size: 0.8rem;">SYSTEM STATUS: ONLINE • GEN Z-2.0 MODEL</div>', unsafe_allow_html=True)