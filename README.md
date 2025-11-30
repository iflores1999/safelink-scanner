🔗 **Live demo:** https://safelink-scannex.onrender.com
# 🛡️ SafeLink Scanner  

**A simple cybersecurity tool that analyzes URLs and detects phishing signs.  
Built by Isela Flores as a beginner-friendly cybersecurity practice project.**

---

## 🚀 Features
- Detects common phishing patterns in URLs  
- Scores URL risk from **Low**, **Medium**, to **High**  
- Shows clear reasons why a URL looks suspicious  
- Clean, polished UI with light purple accents  
- Built using **Flask (Python)** + HTML/CSS  

---

## 🧠 How it works
The scanner checks URLs for things like:

-  Suspicious words (login, verify, update, account)  
-  Missing HTTPS  
-  IP address instead of domain  
-  `@` symbol tricks that hide the real destination  
-  Many subdomains or dots  
-  Suspicious TLDs (.xyz, .cn, etc.)  

Each rule adds to a score, and the score maps to:

- **Low** risk  
- **Medium** risk  
- **High** risk  

---

##  Tech Stack
- **Python (Flask)**  
- **HTML & CSS**  
- **Regex & URL parsing**  
- **Jinja templates**  

---

## ▶️ How to run it locally

```bash
# Clone the repo
git clone https://github.com/iflores1999/safelink-scanner.git
cd safelink-scanner

# (Optional) create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Flask if needed
pip install flask

# Run the app
python3 app.py
