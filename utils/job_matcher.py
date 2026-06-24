from utils.skill_extractor import extract_skills


def calculate_match(resume_text, job_description):

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_description))

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills

    if len(jd_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = round(
            (len(matched_skills) / len(jd_skills)) * 100,
            2
        )

    return match_percentage, matched_skills, missing_skills