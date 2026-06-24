import pandas as pd
import re


def extract_skills(text):

    skills = pd.read_csv(
        "data/skills.csv",
        header=None
    )

    skill_list = skills[0].tolist()

    detected_skills = []

    resume_text = text.lower()

    for skill in skill_list:

        skill_pattern = re.escape(skill.lower())

        if re.search(skill_pattern, resume_text):
            detected_skills.append(skill)

    return sorted(list(set(detected_skills)))