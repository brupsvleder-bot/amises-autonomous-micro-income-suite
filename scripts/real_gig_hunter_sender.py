import os
import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_config(config_path):
    if not os.path.exists(config_path):
        return None
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return None

def load_jobs_db(db_path):
    if not os.path.exists(db_path):
        return None
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return None

def construct_html_email(sender_email, lead_email, job_title, proposal_text, solution_code):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Pre-Solved Solution for your request: {job_title}"
    msg["From"] = sender_email
    msg["To"] = lead_email
    plain_text = f"{proposal_text}\n\n====================\nCOMPLETED CODE SOLUTION:\n====================\n{solution_code}"
    html_text = f"""
    <html>
      <head>
        <style>
          body {{
            background-color: #080b11;
            color: #f8fafc;
            font-family: sans-serif;
            padding: 20px;
          }}
          .card {{
            background-color: #0f172a;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 24px;
            max-width: 600px;
            margin: 0 auto;
          }}
          .proposal {{
            color: #94a3b8;
            line-height: 1.6;
            white-space: pre-line;
            margin-bottom: 24px;
          }}
          .code-box {{
            background-color: #020306;
            padding: 16px;
            font-family: monospace;
            color: #e2e8f0;
            overflow-x: auto;
            white-space: pre;
          }}
        </style>
      </head>
      <body>
        <div class="card">
          <div class="proposal">{proposal_text}</div>
          <pre class="code-box"><code>{solution_code}</code></pre>
        </div>
      </body>
    </html>
    """
    part1 = MIMEText(plain_text, "plain", "utf-8")
    part2 = MIMEText(html_text, "html", "utf-8")
    msg.attach(part1)
    msg.attach(part2)
    return msg

def send_real_email(smtp_config, recipient, msg):
    host = smtp_config.get("smtp_server")
    port = smtp_config.get("smtp_port")
    use_ssl = smtp_config.get("use_ssl", True)
    sender = smtp_config.get("sender_email")
    password = smtp_config.get("sender_password")
    context = ssl.create_default_context()
    if use_ssl:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
    else:
        with smtplib.SMTP(host, port) as server:
            server.starttls(context=context)
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(script_dir)
    config_path = os.path.join(workspace_dir, "config.json")
    db_path = os.path.join(workspace_dir, "outputs", "jobs_database.json")
    config = load_config(config_path)
    if not config:
        return
    jobs_db = load_jobs_db(db_path)
    if not jobs_db:
        return
    dry_run = config.get("dry_run", True)
    smtp_settings = config.get("smtp_settings", {})
    leads = config.get("target_leads", [])
    if not leads:
        return
    for idx, lead in enumerate(leads):
        job = jobs_db[idx % len(jobs_db)]
        msg = construct_html_email(
            sender_email=smtp_settings.get("sender_email"),
            lead_email=lead,
            job_title=job["title"],
            proposal_text=job["proposal"],
            solution_code=job["solution_code"]
        )
        if not dry_run:
            try:
                send_real_email(smtp_settings, lead, msg)
            except Exception as e:
                pass

if __name__ == "__main__":
    main()