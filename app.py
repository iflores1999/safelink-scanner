from flask import Flask, render_template, request
from phishing_checks import analyze_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if url:
            # analyze_url returns a dict with "risk", "score", "reasons"
            result = analyze_url(url)

    # Pass result (or None) and the last typed url to the template
    return render_template("index.html", result=result, url=url)


if __name__ == "__main__":
    # For local testing. On Render, gunicorn will run: app:app
    app.run(host="0.0.0.0", port=5000)


