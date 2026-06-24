from utils.job_matcher import calculate_match


def calculate_ats_score(resume_text, job_description):

    if not job_description.strip():
        return 0, ["Paste a job description to calculate ATS score."]

    match_percentage, matched_skills, missing_skills = calculate_match(
        resume_text,
        job_description
    )

    ats_score = match_percentage

    suggestions = []

    if missing_skills:
        for skill in sorted(missing_skills):
            suggestions.append(f"Add or improve this skill if relevant: {skill}")

    if ats_score < 50:
        suggestions.append("Your resume has low job-description alignment. Add more relevant keywords and skills.")
    elif ats_score < 75:
        suggestions.append("Your resume is moderately aligned. Add the missing skills and project keywords.")
    else:
        suggestions.append("Your resume is strongly aligned with the job description.")

    return ats_score, suggestions