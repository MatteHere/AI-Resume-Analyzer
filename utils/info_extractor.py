import re


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):
    pattern = r"(\+91[\-\s]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_linkedin(text):
    pattern = r"(https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+)"

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return "Not Found"


def extract_github(text):
    pattern = r"(https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+)"

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return "Not Found"


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 2:
            return line

    return "Not Found"