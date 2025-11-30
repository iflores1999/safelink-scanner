# password_strength.py

import re

def analyze_password(password: str) -> dict:
    """
    Simple password strength checker.
    Returns a dict with:
      - label: "Weak", "Medium", "Strong", "Very strong"
      - score: 0–100
      - tips: list of suggestions
    """
    score = 0
    tips = []

    length = len(password)

    # Empty password
    if length == 0:
        return {
            "label": "Weak",
            "score": 0,
            "tips": ["Type a password to see the strength."],
        }

    # 1. Length score
    if length < 8:
        score += 10
        tips.append("Use at least 8 characters.")
    elif length < 12:
        score += 25
    else:
        score += 35

    # 2. Character types
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^\w\s]", password))  # punctuation / symbols

    if has_lower:
        score += 10
    else:
        tips.append("Add some lowercase letters.")

    if has_upper:
        score += 10
    else:
        tips.append("Add some uppercase letters.")

    if has_digit:
        score += 10
    else:
        tips.append("Include at least one number.")

    if has_symbol:
        score += 15
    else:
        tips.append("Include symbols (like !, @, #, ?).")

    # 3. Repetition / simple patterns (very basic checks)
    if re.search(r"(1234|abcd|password|qwerty)", password.lower()):
        score -= 15
        tips.append("Avoid common patterns like '1234' or 'password'.")

    if re.search(r"(.)\1\1", password):
        score -= 10
        tips.append("Avoid repeating the same character many times in a row.")

    # Clamp score between 0 and 100
    score = max(0, min(score, 100))

    # 4. Label based on score
    if score < 30:
        label = "Weak"
    elif score < 60:
        label = "Medium"
    elif score < 85:
        label = "Strong"
    else:
        label = "Very strong"

    # If there are no tips and score is high, give a positive note
    if score >= 80 and not tips:
        tips.append("Nice! This is a strong password. Just don't reuse it on other sites.")

    return {
        "label": label,
        "score": score,
        "tips": tips,
    }
