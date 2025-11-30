from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- URL SCANNER ----------
def evaluate_url(url: str):
    reasons = []
    score = 100
    risk = "Low"

    if not url:
        reasons.append("No URL provided.")
        score = 0
        risk = "High"
    else:
        if not url.startswith("https://"):
            reasons.append("URL is not using HTTPS.")
            score -= 30

        if any(bad in url.lower() for bad in ["login", "verify", "update"]):
            reasons.append("URL contains a sensitive word like 'login' or 'verify'.")
            score -= 30

        if score < 40:
            risk = "High"
        elif score < 75:
            risk = "Medium"
        else:
            risk = "Low"

    return {
        "risk": risk,
        "score": max(score, 0),
        "reasons": reasons or ["Looks okay based on simple checks."],
    }

# ---------- PASSWORD CHECKER ----------
def evaluate_password(pwd: str):
    score = 0
    reasons = []

    # length scoring
    if len(pwd) < 8:
        reasons.append("Password is shorter than 8 characters.")
        score += 10
    elif len(pwd) < 12:
        reasons.append("Password length is okay but could be longer.")
        score += 40
    else:
        reasons.append("Good length (12+ characters).")
        score += 60

    # character types
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)

    types_count = sum([
        has_lower,
        has_upper,
        has_digit,
        has_special
    ])

    if types_count <= 1:
        reasons.append("Try mixing upper/lowercase, numbers, and symbols.")
        score += 5
    elif types_count == 2:
        reasons.append("You use a couple of character types. Add more variety.")
        score += 15
    else:
        reasons.append("Nice variety of characters (letters, numbers, symbols).")
        score += 25

    score = min(score, 100)

    if score < 40:
        label = "Weak"
    elif score < 75:
        label = "Okay"
        label = "Okay"
    else:
        label = "Strong"

    return {
        "label": label,
        "score": score,
        "reasons": reasons,
    }

# ---------- SINGLE PAGE (BOTH TOOLS) ----------
@app.route("/", methods=["GET", "POST"])
def home():
    url = ""
    password = ""
    url_result = None
    pwd_result = None

    if request.method == "POST":

        if "url" in request.form:
            url = request.form.get("url", "")
            url_result = evaluate_url(url)

        if "password" in request.form:
            password = request.form.get("password", "")
            pwd_result = evaluate_password(password)

    return render_template(
        "index.html",
        url=url,
        password=password,
        url_result=url_result,
        pwd_result=pwd_result,
    )

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
