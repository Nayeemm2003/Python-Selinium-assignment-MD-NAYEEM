# app.py
import os
import smtplib
import traceback
from email.message import EmailMessage
from flask import Flask, jsonify
from dotenv import load_dotenv
from form_filling import run_fill  

# Load environment variables
load_dotenv()

# Gmail SMTP configuration
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "mohdnayeemm2003@gmail.com")  # your Gmail address
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD","tofr gwhi praa nuie")#  Gmail App Password 

FROM_EMAIL = SMTP_USERNAME
TO_EMAIL = "tech@themedius.ai"
CC_EMAIL = "hr@themedius.ai"
SUBJECT = "Python (Selenium) Assignment - MD NAYEEM"

# Files to attach 
FILES_TO_ATTACH = [
    "Confirmation.png", 
    "Technical Documentation.docx",
    "nayeem_resume.pdf"
    
]

app = Flask(__name__)

def send_email_with_attachments(subject, to_email, cc_email, text_body, files):
    """Send email with attachments using SMTP."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email
    msg["Cc"] = cc_email
    msg.set_content(text_body)

    # Attach all files
    for fpath in files:
        if not os.path.exists(fpath):
            print(f" Attachment missing: {fpath}")
            continue
        with open(fpath, "rb") as f:
            data = f.read()
        msg.add_attachment(
            data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(fpath),
        )

    recipients = [to_email, cc_email]
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg, FROM_EMAIL, recipients)
    print("Email sent successfully to:", recipients)

@app.route("/submit-assignment", methods=["POST"])
def submit_assignment():
    """Runs Selenium form filling and sends the email."""
    try:
        # Your answers for the form
        answers = [
            "MD NAYEEM",
            "8368888969",
            "mohdnayeemm2003@gmail.com",
            "D-45 MADANPUR KHADAR EXTN-3 NEAR MAKKI MASJID NEW DELHI",
            "110076",
            "29-10-2003",
            "MALE",
            "GNFPYC"
        ]

        # Run Selenium to fill form and get screenshot
        screenshot_path = run_fill(answers, headless=True)

        # all required files
        files = FILES_TO_ATTACH.copy()
        if screenshot_path and screenshot_path not in files:
            files.insert(0, screenshot_path)

        # Email body
        body = """Hello Team Medius,

I hope you're doing well.

Please find the attached documents related to my Selenium Automation Assignment submission:
1. Screenshot of the filled Google Form (automatically captured)
2. Source code (this project)
3. Technical documentation (approach and explanation)
4. Resume
5. Links to my past project repositories

I am fully available to work full-time (10 AM – 7 PM IST) for the next 3–6 months and can join immediately if selected.  
You can explore the GitHub repository for this assignment and my previous projects using the links below:

Assignment Repository: (https://github.com/Nayeemm2003/Python-Selinium-assignment-MD-NAYEEM)  
Past Projects Repository:(https://github.com/Nayeemm2003/RESUME-RANKING-AND-SCREENING-SYSTEM)(https://github.com/Nayeemm2003/TASK-SYNC-API)

Please let me know if any additional information is required.

Thank you for the opportunity.

Warm regards,  
MD NAYEEM 
mohdnayeemm2003@gmail.com  
+91 8368888969
"""

        send_email_with_attachments(SUBJECT, TO_EMAIL, CC_EMAIL, body, files)
        return jsonify({"status": "ok", "message": "Assignment submitted and email sent successfully."})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
