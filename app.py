import streamlit as st
import os
import plotly.express as px

from utils.pdf_reader import read_pdf, read_docx
from utils.skill_extractor import extract_skills
from utils.job_matcher import calculate_match
from utils.resume_score import calculate_resume_score
from utils.ats_score import calculate_ats_score
from utils.recommendation_engine import generate_recommendations
from utils.style import apply_custom_style

from utils.info_extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github
)

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")
apply_custom_style()

st.markdown('<div class="main-title">📄 AI Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Premium ATS scoring, skill intelligence, job matching, and resume recommendations.</div>',
    unsafe_allow_html=True
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

left_col, right_col = st.columns(2)

with left_col:
    resume = st.file_uploader("📄 Upload Your Resume", type=["pdf", "docx"])

with right_col:
    job_description = st.text_area("💼 Paste Job Description", height=150)

analyze_button = st.button("🚀 Analyze Resume", width="stretch")

if analyze_button:

    if resume is None:
        st.error("Please upload a resume first.")

    else:
        file_path = os.path.join(UPLOAD_FOLDER, resume.name)

        with open(file_path, "wb") as f:
            f.write(resume.getbuffer())

        if resume.name.endswith(".pdf"):
            resume_text = read_pdf(file_path)
        else:
            resume_text = read_docx(file_path)

        skills = extract_skills(resume_text)
        resume_score, suggestions = calculate_resume_score(resume_text)
        ats_score, ats_suggestions = calculate_ats_score(resume_text, job_description)

        final_recommendations = generate_recommendations(
            resume_text,
            job_description
        )

        matched_skills = set()
        missing_skills = set()
        match_percentage = 0

        if job_description.strip():
            match_percentage, matched_skills, missing_skills = calculate_match(
                resume_text,
                job_description
            )

        st.success("Resume analyzed successfully!")

        st.markdown('<div class="section-title">📊 Dashboard Overview</div>', unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(
                f"""
                <div class="metric-3d">
                    <h3>Detected Skills</h3>
                    <h1>{len(skills)}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m2:
            st.markdown(
                f"""
                <div class="metric-3d">
                    <h3>Resume Score</h3>
                    <h1>{resume_score}/100</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m3:
            ats_display = f"{ats_score}/100" if job_description.strip() else "N/A"
            st.markdown(
                f"""
                <div class="metric-3d">
                    <h3>ATS Score</h3>
                    <h1>{ats_display}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m4:
            match_display = f"{match_percentage}%" if job_description.strip() else "N/A"
            st.markdown(
                f"""
                <div class="metric-3d">
                    <h3>Job Match</h3>
                    <h1>{match_display}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('<div class="section-title">👤 Candidate Profile</div>', unsafe_allow_html=True)

        name = extract_name(resume_text)
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        linkedin = extract_linkedin(resume_text)
        github = extract_github(resume_text)

        p1, p2 = st.columns(2)

        with p1:
            st.markdown(
                f"""
                <div class="profile-card">
                    <h4>👤 Name</h4>
                    <p>{name}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with p2:
            st.markdown(
                f"""
                <div class="profile-card">
                    <h4>📧 Email</h4>
                    <p>{email}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        p3, p4 = st.columns(2)

        with p3:
            st.markdown(
                f"""
                <div class="profile-card">
                    <h4>📞 Phone</h4>
                    <p>{phone}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with p4:
            st.markdown(
                f"""
                <div class="profile-card">
                    <h4>💻 GitHub</h4>
                    <p>{github}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="profile-card">
                <h4>💼 LinkedIn</h4>
                <p>{linkedin}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="section-title">📈 Visual Analytics</div>', unsafe_allow_html=True)

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            score_data = {
                "Category": ["Resume Score", "ATS Score"],
                "Score": [
                    resume_score,
                    ats_score if job_description.strip() else 0
                ]
            }

            score_chart = px.bar(
                score_data,
                x="Category",
                y="Score",
                title="Resume Score vs ATS Score",
                range_y=[0, 100]
            )

            st.plotly_chart(score_chart, width="stretch")

        with chart_col2:
            if job_description.strip():
                match_data = {
                    "Type": ["Matched Skills", "Missing Skills"],
                    "Count": [len(matched_skills), len(missing_skills)]
                }

                match_chart = px.pie(
                    match_data,
                    names="Type",
                    values="Count",
                    title="Matched vs Missing Skills"
                )

                st.plotly_chart(match_chart, width="stretch")
            else:
                st.info("Paste a job description to view matched vs missing skills chart.")

        st.markdown('<div class="section-title">🛠 Detected Skills</div>', unsafe_allow_html=True)

        if skills:
            skill_html = '<div class="glass-card">'
            for skill in skills:
                skill_html += f'<span class="skill-chip">✅ {skill}</span>'
            skill_html += '</div>'

            st.markdown(skill_html, unsafe_allow_html=True)
        else:
            st.warning("No skills detected.")

        st.markdown('<div class="section-title">⭐ Resume & ATS Scores</div>', unsafe_allow_html=True)

        score_col1, score_col2 = st.columns(2)

        with score_col1:
            st.markdown(
                f"""
                <div class="glass-card">
                    <h3>⭐ Resume Score</h3>
                    <h1>{resume_score}/100</h1>
                    <p>Measures overall resume completeness based on contact details, skills, projects, education, and certifications.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.progress(resume_score / 100)

        with score_col2:
            if job_description.strip():
                st.markdown(
                    f"""
                    <div class="glass-card">
                        <h3>🤖 ATS Score</h3>
                        <h1>{ats_score}/100</h1>
                        <p>Measures alignment between resume skills and the pasted job description.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.progress(ats_score / 100)
            else:
                st.warning("Paste a job description to calculate ATS score.")

        st.markdown('<div class="section-title">🧠 Final Recommendations</div>', unsafe_allow_html=True)

        if final_recommendations:
            recommendation_html = '<div class="glass-card">'
            for recommendation in final_recommendations:
                recommendation_html += f"<p>💡 {recommendation}</p>"
            recommendation_html += "</div>"
            st.markdown(recommendation_html, unsafe_allow_html=True)
        else:
            st.success("Your resume looks strong. No major recommendations found.")

        if job_description.strip():

            st.markdown('<div class="section-title">🎯 Job Description Match</div>', unsafe_allow_html=True)

            match_col1, match_col2 = st.columns([1, 2])

            with match_col1:
                st.markdown(
                    f"""
                    <div class="metric-3d">
                        <h3>Match Percentage</h3>
                        <h1>{match_percentage}%</h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with match_col2:
                st.progress(match_percentage / 100)

            col5, col6 = st.columns(2)

            with col5:
                st.markdown('<div class="section-title">✅ Matched Skills</div>', unsafe_allow_html=True)

                if matched_skills:
                    matched_html = '<div class="glass-card">'
                    for skill in sorted(matched_skills):
                        matched_html += f'<span class="skill-chip">✅ {skill}</span>'
                    matched_html += '</div>'
                    st.markdown(matched_html, unsafe_allow_html=True)
                else:
                    st.warning("No matched skills found.")

            with col6:
                st.markdown('<div class="section-title">❌ Missing Skills</div>', unsafe_allow_html=True)

                if missing_skills:
                    missing_html = '<div class="glass-card">'
                    for skill in sorted(missing_skills):
                        missing_html += f'<span class="skill-chip">❌ {skill}</span>'
                    missing_html += '</div>'
                    st.markdown(missing_html, unsafe_allow_html=True)
                else:
                    st.success("No missing skills. Great match!")

        with st.expander("📁 File Details"):
            st.write("**Filename:**", resume.name)
            st.write("**File Type:**", resume.type)
            st.write("**File Size:**", round(resume.size / 1024, 2), "KB")

        with st.expander("📄 View Extracted Resume Text"):
            st.text_area("Resume Content", resume_text, height=400)

st.markdown(
    '<div class="footer">Built with Python, Streamlit, NLP, and Data Science techniques.</div>',
    unsafe_allow_html=True
)