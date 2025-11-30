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
            result = analyze_url(url)

    return render_template("index.html", result=result, url=url)

# Simple health check for Render
@app.route("/health")
def health():
    return "OK", 200

# For running locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

