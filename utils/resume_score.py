from utils.info_extractor import (
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github
)

from utils.skill_extractor import extract_skills


def calculate_resume_score(resume_text):

    score = 0
    suggestions = []

    if extract_email(resume_text) != "Not Found":
        score += 10
    else:
        suggestions.append("Add your email address.")

    if extract_phone(resume_text) != "Not Found":
        score += 10
    else:
        suggestions.append("Add your phone number.")

    if extract_linkedin(resume_text) != "Not Found":
        score += 10
    else:
        suggestions.append("Add your LinkedIn profile.")

    if extract_github(resume_text) != "Not Found":
        score += 10
    else:
        suggestions.append("Add your GitHub profile.")

    skills = extract_skills(resume_text)

    if len(skills) >= 8:
        score += 20
    elif len(skills) >= 4:
        score += 10
        suggestions.append("Add more technical skills.")
    else:
        suggestions.append("Add more relevant technical skills.")

    text_lower = resume_text.lower()

    if "project" in text_lower or "projects" in text_lower:
        score += 15
    else:
        suggestions.append("Add an academic or personal projects section.")

    if "education" in text_lower:
        score += 10
    else:
        suggestions.append("Add your education details.")

    if "certification" in text_lower or "certifications" in text_lower:
        score += 10
    else:
        suggestions.append("Add certifications related to AI, Data Science, Python, SQL, or Machine Learning.")

    if "internship" in text_lower or "experience" in text_lower:
        score += 5
    else:
        suggestions.append("Add internship, training, or work experience if available.")

    return score, suggestions