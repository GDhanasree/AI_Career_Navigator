# import streamlit as st
# import json

# from utils.skill_extractor import extract_skills
# from utils.gap_analysis import find_skill_gap
# from utils.structured_roadmap import generate_structured_roadmap
# from utils.phases import generate_learning_phases

# # HuggingFace (SAFE VERSION)
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # =====================
# # LOAD DATA
# # =====================
# with open("data/roles.json") as f:
#     roles = json.load(f)

# # =====================
# # LOAD MODEL (NO PIPELINE)
# # =====================
# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
#     model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
#     return tokenizer, model

# tokenizer, model = load_model()

# def generate_ai_text(prompt):
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
#     outputs = model.generate(**inputs, max_new_tokens=150)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

# # =====================
# # UI
# # =====================
# st.title("🚀 Skill-Bridge Career Navigator")

# mode = st.radio("Select Mode", ["AI Mode", "Fallback Mode"])

# resume = st.text_area("Paste your resume here")

# role = st.selectbox("Select target role", list(roles.keys()))

# # =====================
# # MAIN LOGIC
# # =====================
# if st.button("Analyze"):

#     if not resume.strip():
#         st.error("Please enter resume text")

#     else:
#         role_skills = roles[role]

#         # =====================
#         # SKILL EXTRACTION
#         # =====================
#         if mode == "AI Mode":
#             user_skills = extract_skills(resume, role_skills)
#         else:
#             user_skills = []

#         if not user_skills:
#             st.warning("AI failed or no skills detected. Using fallback...")
#             user_skills = []

#         # =====================
#         # GAP ANALYSIS
#         # =====================
#         missing_skills = find_skill_gap(user_skills, role_skills)

#         # =====================
#         # MATCH SCORE
#         # =====================
#         match_score = int((len(user_skills) / len(role_skills)) * 100) if role_skills else 0

#         st.subheader("📊 Match Score")
#         st.success(f"{match_score}% match with {role} role")
#         st.progress(match_score / 100)

#         # =====================
#         # DISPLAY SKILLS
#         # =====================
#         st.subheader("✅ Extracted Skills")
#         st.write(", ".join(user_skills) if user_skills else "No skills found")

#         st.subheader("❌ Missing Skills")
#         st.write(", ".join(missing_skills))

#         # =====================
#         # ROLE INSIGHTS
#         # =====================
#         st.subheader("📌 Role Insights")
#         st.write(", ".join(role_skills))

#         # =====================
#         # STRUCTURED SKILL GAP
#         # =====================
#         st.subheader("📊 Missing Skills (Industry Gap)")

#         structured = generate_structured_roadmap(missing_skills, role)

#         if structured:
#             for category, topics in structured.items():
#                 st.write(f"### {category}")
#                 for t in topics:
#                     st.write(f"- {t}")
#         else:
#             st.write("No structured gaps found (you are close to role readiness!)")

#         # =====================
#         # PHASE ROADMAP
#         # =====================
#         st.subheader("🚀 Learning Roadmap")

#         phases = generate_learning_phases(role)

#         for phase, steps in phases.items():
#             st.write(f"### {phase}")
#             for step in steps:
#                 st.write(f"- {step}")

#         # =====================
#         # AI GUIDANCE
#         # =====================
#         if mode == "AI Mode":
#             st.subheader("🤖 AI Career Guidance")

#             try:
#                 prompt = f"""
#                 You are a career advisor.

#                 Target role: {role}
#                 Missing skills: {', '.join(missing_skills)}

#                 Provide short structured guidance.
#                 """

#                 response = generate_ai_text(prompt)
#                 st.write(response)

#             except:
#                 st.warning("AI failed. Showing fallback guidance.")
#                 st.write("Focus on learning step-by-step and building projects.")

#         # =====================
#         # SEARCH FILTER
#         # =====================
#         st.subheader("🔍 Search Missing Skills")

#         search_skill = st.text_input("Type a skill")

#         if search_skill:
#             filtered = [s for s in missing_skills if search_skill.lower() in s]
#             st.write("Filtered Skills:", filtered)

#         # =====================
#         # MOCK QUESTIONS
#         # =====================
#         questions = {
#             "python": ["What are decorators?", "Explain GIL"],
#             "sql": ["What is normalization?"],
#             "machine learning": ["What is overfitting?"],
#             "deep learning": ["What is CNN?"]
#         }

#         st.subheader("🎯 Mock Interview Questions")

#         for skill in user_skills:
#             if skill in questions:
#                 st.write(f"{skill}: {questions[skill]}")

#         # =====================
#         # PROGRESS
#         # =====================
#         st.subheader("📈 Learning Progress Simulation")

#         progress = st.slider("Simulate Progress (%)", 0, 100)

#         if progress > 70:
#             st.success("You're close to being job-ready!")
#         elif progress > 40:
#             st.info("Good progress, keep going!")
#         else:
#             st.warning("You need to build more skills")

# import streamlit as st
# st.set_page_config(
#     page_title="Career Navigator",
#     page_icon="🚀"
# )
# import json

# from utils.skill_extractor import extract_skills
# from utils.gap_analysis import find_skill_gap
# from utils.structured_roadmap import generate_structured_roadmap
# from utils.phases import generate_learning_phases

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # =====================
# # SESSION STATE FIX
# # =====================
# if "analyzed" not in st.session_state:
#     st.session_state.analyzed = False

# # =====================
# # LOAD DATA
# # =====================
# with open("data/roles.json") as f:
#     roles = json.load(f)

# # =====================
# # LOAD MODEL
# # =====================
# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
#     model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
#     return tokenizer, model

# tokenizer, model = load_model()

# def generate_ai_text(prompt):
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
#     outputs = model.generate(**inputs, max_new_tokens=150)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

# # =====================
# # UI
# # =====================

# st.title("🚀 Skill-Bridge Career Navigator")

# mode = st.radio("Select Mode", ["AI Mode", "Fallback Mode"])

# resume = st.text_area("Paste your resume here")

# role = st.selectbox("Select target role", list(roles.keys()))

# # =====================
# # BUTTON
# # =====================
# if st.button("Analyze"):
#     st.session_state.analyzed = True

# # =====================
# # MAIN LOGIC (WRAPPED)
# # =====================
# if st.session_state.analyzed:

#     if not resume.strip():
#         st.error("Please enter resume text")

#     else:
#         role_skills = roles[role]

#         # =====================
#         # SKILL EXTRACTION
#         # =====================
#         if mode == "AI Mode":
#             user_skills = extract_skills(resume, role_skills)
#         else:
#             user_skills = []

#         if not user_skills:
#             st.warning("AI failed or no skills detected. Using fallback...")
#             user_skills = []

#         # =====================
#         # GAP ANALYSIS
#         # =====================
#         missing_skills = find_skill_gap(user_skills, role_skills)

#         # =====================
#         # MATCH SCORE
#         # =====================
#         match_score = int((len(user_skills) / len(role_skills)) * 100) if role_skills else 0

#         st.subheader("📊 Match Score")
#         st.success(f"{match_score}% match with {role} role")
#         st.progress(match_score / 100)

#         # =====================
#         # DISPLAY SKILLS
#         # =====================
#         st.subheader("✅ Extracted Skills")
#         st.write(", ".join(user_skills) if user_skills else "No skills found")

#         st.subheader("❌ Missing Skills")
#         st.write(", ".join(missing_skills))

#         # =====================
#         # ROLE INSIGHTS
#         # =====================
#         st.subheader("📌 Role Insights")
#         st.write(", ".join(role_skills))

#         # =====================
#         # STRUCTURED GAP
#         # =====================
#         st.subheader("📊 Missing Skills (Industry Gap)")

#         structured = generate_structured_roadmap(missing_skills, role)

#         if structured:
#             for category, topics in structured.items():
#                 st.write(f"### {category}")
#                 for t in topics:
#                     st.write(f"- {t}")
#         else:
#             st.write("No structured gaps found (you are close to role readiness!)")

#         # =====================
#         # PHASE ROADMAP
#         # =====================
#         st.subheader("🚀 Learning Roadmap")

#         phases = generate_learning_phases(role)

#         for phase, steps in phases.items():
#             st.write(f"### {phase}")
#             for step in steps:
#                 st.write(f"- {step}")

#         # =====================
#         # AI GUIDANCE
#         # =====================
#         if mode == "AI Mode":
#             st.subheader("🤖 AI Career Guidance")

#             try:
#                 prompt = f"""
#                 You are a career advisor.

#                 Target role: {role}
#                 Missing skills: {', '.join(missing_skills)}

#                 Provide short structured guidance.
#                 """

#                 response = generate_ai_text(prompt)
#                 st.write(response)

#             except:
#                 st.warning("AI failed. Showing fallback guidance.")
#                 st.write("Focus on learning step-by-step and building projects.")

#         # =====================
#         # SEARCH FILTER
#         # =====================
#         st.subheader("🔍 Search Missing Skills")

#         search_skill = st.text_input("Type a skill")

#         if search_skill:
#             filtered = [s for s in missing_skills if search_skill.lower() in s]
#             st.write("Filtered Skills:", filtered)

#         # =====================
#         # MOCK QUESTIONS
#         # =====================
#         questions = {
#             "python": ["What are decorators?", "Explain GIL"],
#             "sql": ["What is normalization?"],
#             "machine learning": ["What is overfitting?"],
#             "deep learning": ["What is CNN?"]
#         }

#         st.subheader("🎯 Mock Interview Questions")

#         for skill in user_skills:
#             if skill in questions:
#                 st.write(f"{skill}: {questions[skill]}")

#         # =====================
#         # PROGRESS (NOW STABLE)
#         # =====================
#         st.subheader("📈 Learning Progress Simulation")

#         progress = st.slider("Simulate Progress (%)", 0, 100)

#         if progress > 70:
#             st.success("You're close to being job-ready!")
#         elif progress > 40:
#             st.info("Good progress, keep going!")
#         else:
#             st.warning("You need to build more skills")


import streamlit as st

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="Career Navigator",
    page_icon="🚀",
    layout="wide"
)

import json
from utils.skill_extractor import extract_skills
from utils.gap_analysis import find_skill_gap
from utils.structured_roadmap import generate_structured_roadmap
from utils.phases import generate_learning_phases

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# =====================
# SESSION STATE FIX
# =====================
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# =====================
# LOAD DATA
# =====================
with open("data/roles.json") as f:
    roles = json.load(f)

# =====================
# LOAD MODEL
# =====================
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    return tokenizer, model

tokenizer, model = load_model()

def generate_ai_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=120)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# =====================
# UI
# =====================
st.title("🚀 Skill-Bridge Career Navigator")
st.caption("Bridge your skill gap and reach your dream role")

mode = st.radio("Select Mode", ["AI Mode", "Fallback Mode"])
resume = st.text_area("Paste your resume here")
role = st.selectbox("Select target role", list(roles.keys()))

# =====================
# BUTTON
# =====================
if st.button("Analyze"):
    st.session_state.analyzed = True

# =====================
# MAIN LOGIC
# =====================
if st.session_state.analyzed:

    if not resume.strip():
        st.error("Please enter resume text")

    else:
        role_skills = roles[role]

        # =====================
        # SKILL EXTRACTION
        # =====================
        if mode == "AI Mode":
            user_skills = extract_skills(resume, role_skills)
        else:
            user_skills = []

        # =====================
        # FALLBACK FIX (IMPORTANT)
        # =====================
        if not user_skills:
            st.warning("AI failed or no skills detected. Using fallback...")

            resume_lower = resume.lower()
            user_skills = [skill for skill in role_skills if skill in resume_lower]

        # =====================
        # GAP ANALYSIS
        # =====================
        missing_skills = find_skill_gap(user_skills, role_skills)

        # =====================
        # MATCH SCORE
        # =====================
        match_score = int((len(user_skills) / len(role_skills)) * 100) if role_skills else 0

        st.subheader("📊 Match Score")
        st.success(f"{match_score}% match with {role} role")
        st.progress(match_score / 100)

        # =====================
        # DISPLAY SKILLS
        # =====================
        st.subheader("✅ Extracted Skills")
        st.write(", ".join(user_skills) if user_skills else "No skills found")

        st.subheader("❌ Missing Skills")
        st.write(", ".join(missing_skills))

        # =====================
        # ROLE INSIGHTS
        # =====================
        st.subheader("📌 Role Insights")
        st.write(", ".join(role_skills))

        # =====================
        # STRUCTURED GAP
        # =====================
        st.subheader("📊 Missing Skills (Industry Gap)")

        structured = generate_structured_roadmap(missing_skills, role)

        if structured:
            for category, topics in structured.items():
                st.write(f"### {category}")
                for t in topics:
                    st.write(f"- {t}")
        else:
            st.write("No structured gaps found (you are close to role readiness!)")

        # =====================
        # PHASE ROADMAP
        # =====================
        st.subheader("🚀 Learning Roadmap")

        phases = generate_learning_phases(role)

        for phase, steps in phases.items():
            st.write(f"### {phase}")
            for step in steps:
                st.write(f"- {step}")

        # =====================
        # AI GUIDANCE (FIXED)
        # =====================
        if mode == "AI Mode":
            st.subheader("🤖 AI Career Guidance")

            try:
                prompt = f"""
You are a career advisor.

Target role: {role}
Missing skills: {', '.join(missing_skills)}

Give:
1. 2-3 short actionable suggestions
2. Key focus areas
3. One practical tip

Do NOT repeat text.
Be concise.
"""

                response = generate_ai_text(prompt)

                st.markdown(f"```\n{response}\n```")

            except:
                st.warning("AI failed. Showing fallback guidance.")
                st.write("Focus on learning step-by-step and building projects.")

        # =====================
        # SEARCH FILTER
        # =====================
        st.subheader("🔍 Search Missing Skills")

        search_skill = st.text_input("Type a skill")

        if search_skill:
            filtered = [s for s in missing_skills if search_skill.lower() in s]
            st.write("Filtered Skills:", filtered)

        # =====================
        # MOCK QUESTIONS
        # =====================
        questions = {
            "python": ["What are decorators?", "Explain GIL"],
            "sql": ["What is normalization?"],
            "machine learning": ["What is overfitting?"],
            "deep learning": ["What is CNN?"]
        }

        st.subheader("🎯 Mock Interview Questions")

        for skill in user_skills:
            if skill in questions:
                st.write(f"{skill}: {questions[skill]}")

        # =====================
        # PROGRESS
        # =====================
        st.subheader("📈 Learning Progress Simulation")

        progress = st.slider("Simulate Progress (%)", 0, 100)

        if progress > 70:
            st.success("You're close to being job-ready!")
        elif progress > 40:
            st.info("Good progress, keep going!")
        else:
            st.warning("You need to build more skills")