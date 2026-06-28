import os
import imaplib
import email
from email.header import decode_header
from crewai import Agent, Task, Crew, Process, LLM

# =====================================================================
# 1. LIVE GMAIL & GEMINI CONFIGURATION
# =====================================================================
GMAIL_EMAIL = os.environ.get("GMAIL_EMAIL", "your_email@gmail.com")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "your_app_password")

# Free Gemini Model Setup
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.environ.get("GEMINI_API_KEY")
)

def fetch_latest_unread_email():
    """Fetches the latest email and accurately parses its flags for UNREAD status."""
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        mail.select("INBOX")
        
        status, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()
        
        if not email_ids:
            return None
            
        latest_email_id = email_ids[-1]
        
        # Fetch flags safely
        status, flags_data = mail.fetch(latest_email_id, '(FLAGS)')
        
        # IMAP response se flags decode karne ka sabse safe tarika
        flags_string = str(flags_data[0])
        if '\\Seen' in flags_string:
            print("Inbox ki sabse latest email pehle se 'Read' (Seen) hai. Please use Unread karein!")
            return None

        # Agar unread hai, to data fetch karo
        status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")
                sender = msg.get("From")
                
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                    
                return {"sender": sender, "subject": subject, "body": body}
    except Exception as e:
        print(f"Error fetching email: {e}")
        return None

def create_gmail_draft(to_email, subject, body_content):
    """Saves the final generated response into Gmail Drafts."""
    try:
        from email.mime.text import MIMEText
        import time

        msg = MIMEText(body_content)
        msg['To'] = to_email
        msg['Subject'] = f"Re: {subject}"
        msg['From'] = GMAIL_EMAIL

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        
        try:
            mail.append('[Gmail]/Drafts', '', imaplib.Time2Internaldate(time.time()), msg.as_bytes())
        except:
            mail.append('Drafts', '', imaplib.Time2Internaldate(time.time()), msg.as_bytes())
            
        mail.logout()
        print(f" Successfully saved draft response to Gmail Drafts folder!")
    except Exception as e:
        print(f"Failed to push draft to Gmail server: {e}")

# =====================================================================
# 2. CREWAI AGENTS AND TASKS DEFINITION
# =====================================================================
context_analyzer = Agent(
    role='Email Classification and Intent Specialist',
    goal='Identify the exact type/category of the email and its urgency level.',
    backstory='You look at incoming text and explicitly categorize it (e.g., HR, Support, Inquiry, Refund, Casual) and note the sender\'s mood.',
    llm=gemini_llm,
    verbose=True
)

draft_writer = Agent(
    role='Professional Corporate Copywriter',
    goal='Draft high-quality, authentic, and naturally flowing email text.',
    backstory='An empathetic writer who creates human-like, custom communication.',
    llm=gemini_llm,
    verbose=True
)

def run_email_replier_pipeline():
    print("Checking live email inbox for new unread messages...")
    email_data = fetch_latest_unread_email()
    
    if not email_data:
        print("No NEW unread emails found right now. (Make sure you have an unread email in your Primary inbox!)")
        return

    print(f"\n New Email Detected!")
    print(f"From: {email_data['sender']}")
    print(f"Subject: {email_data['subject']}\n")

    analysis_task = Task(
        description=(
            f"Analyze this live incoming email:\n"
            f"Sender: {email_data['sender']}\n"
            f"Subject: {email_data['subject']}\n"
            f"Body: {email_data['body']}\n\n"
            "Determine the Category (e.g., HR Request, Question, Support, Complaint) and the Urgency level."
        ),
        expected_output="A clear statement showing the classified Email Type, Urgency, and customer intent.",
        agent=context_analyzer
    )

    writing_task = Task(
        description="Based on the analysis, write a highly professional and tailored email reply.",
        expected_output="The final exact text body for the email reply.",
        agent=draft_writer,
        output_file="latest_email_response_log.md"
    )

    email_crew = Crew(
        agents=[context_analyzer, draft_writer],
        tasks=[analysis_task, writing_task],
        process=Process.sequential
    )
    
    print("Starting CrewAI Classification & Writing workflow...")
    final_reply_text = email_crew.kickoff()
    
    print("\nSaving draft back to Gmail...")
    create_gmail_draft(
        to_email=email_data['sender'],
        subject=email_data['subject'],
        body_content=str(final_reply_text)
    )

if __name__ == "__main__":
    run_email_replier_pipeline()