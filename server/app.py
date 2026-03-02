
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pdf_generator import generate_pdf
from ats import calculate_ats_score   # ✅ IMPORT ATS MODULE
from resume_analyzer import analyze_resume
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running ✅"

# =========================
# Resume Generate API
# =========================
@app.route("/generate", methods=["POST"])
def generate_resume():

    data = request.get_json()

    content = data.get("content")

    if not content:
        return jsonify({"error": "No content provided"}), 400

    file_path = generate_pdf(content)

    return jsonify({
        "message": "Resume Generated",
        "file": file_path
    })


# =========================
# Download PDF API
# =========================
@app.route("/download", methods=["GET"])
def download_pdf():

    file_path = "generated_resume.pdf"

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404


# =========================
# ATS Score API
# =========================
@app.route("/ats-score", methods=["POST"])
def ats_score():

    data = request.get_json()

    resume_text = data.get("resume")
    job_desc = data.get("job")

    if not resume_text or not job_desc:
        return jsonify({"error": "Missing fields"}), 400

    # ✅ Use function from ats.py
    score, matched_keywords = calculate_ats_score(resume_text, job_desc)

    return jsonify({
        "score": score,
        "matched_keywords": matched_keywords
    })
# =========================
# Resume Upload Analyzer
# =========================
@app.route("/analyze", methods=["POST"])
def analyze():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    result = analyze_resume(file)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)