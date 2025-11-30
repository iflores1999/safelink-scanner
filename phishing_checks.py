import re
from urllib.parse import urlparse

def analyze_url(url: str) -> dict:
    score = 0
    reasons = []

    # Normalize a bit
    lower_url = url.lower()
    parsed = urlparse(url)
    domain = parsed.netloc

    # Rule 1: '@' in URL (often used by attackers)
    if "@" in url:
        score += 25
        reasons.append("The URL has '@', which attackers sometimes use to hide the real destination.")

    # Rule 2: URL is very long
    if len(url) > 60:
        score += 10
        reasons.append("The URL is very long, which can be used to hide suspicious parts.")

    # Rule 3: Suspicious words
    suspicious_keywords = ["login", "verify", "update", "secure", "account", "confirm", "gift", "winner"]
    if any(word in lower_url for word in suspicious_keywords):
        score += 20
        reasons.append("The URL has words often used in phishing (like login/verify/account).")

    # Rule 4: Uses plain IP address instead of domain
    # e.g. http://192.168.0.1/login
    ip_pattern = r"^\d{1,3}(?:\.\d{1,3}){3}$"
    if re.match(ip_pattern, domain):
        score += 25
        reasons.append("The URL uses an IP address instead of a normal website name, which is suspicious.")

    # Rule 5: Not using HTTPS
    if parsed.scheme == "http":
        score += 10
        reasons.append("The link does not use HTTPS (secure connection).")

    # Rule 6: Suspicious domain endings (TLDs)
    suspicious_tlds = [".ru", ".cn", ".xyz", ".top", ".gq", ".ml", ".tk"]
    if any(domain.endswith(tld) for tld in suspicious_tlds):
        score += 15
        reasons.append("The domain uses a less common ending often seen in phishing campaigns.")

    # Rule 7: Too many dots or dashes in the domain
    if domain.count(".") >= 3:
        score += 10
        reasons.append("The domain has many dots/subdomains, which can be used to imitate trusted sites.")
    if domain.count("-") >= 2:
        score += 10
        reasons.append("The domain has many dashes, which is common in fake or throwaway sites.")

    # Decide risk level
    if score < 20:
        risk = "Low"
    elif score < 50:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "risk": risk,
        "score": score,
        "reasons": reasons
    }
