from utils.resume_score import calculate_resume_score
from utils.ats_score import calculate_ats_score
from utils.skill_extractor import extract_skills
from utils.job_matcher import calculate_match


def generate_recommendations(resume_text, job_description):

    recommendations = []

    resume_score, resume_suggestions = calculate_resume_score(resume_text)
    recommendations.extend(resume_suggestions)

    skills = extract_skills(resume_text)

    if len(skills) < 8:
        recommendations.append("Add more technical skills related to your target role.")

    if job_description.strip():
        ats_score, ats_suggestions = calculate_ats_score(resume_text, job_description)
        recommendations.extend(ats_suggestions)

        match_percentage, matched_skills, missing_skills = calculate_match(
            resume_text,
            job_description
        )

        if missing_skills:
            recommendations.append(
                "Focus on learning or mentioning these missing job skills: "
                + ", ".join(sorted(missing_skills))
            )

        if match_percentage < 70:
            recommendations.append(
                "Customize your resume according to the job description to improve match percentage."
            )

    text_lower = resume_text.lower()

    if "project" not in text_lower and "projects" not in text_lower:
        recommendations.append("Add at least 2 strong academic or personal projects.")

    if "github" not in text_lower:
        recommendations.append("Add your GitHub profile to showcase your project work.")

    if "linkedin" not in text_lower:
        recommendations.append("Add your LinkedIn profile for better professional visibility.")

    return list(dict.fromkeys(recommendations))