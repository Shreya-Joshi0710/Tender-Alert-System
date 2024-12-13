import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from io import StringIO
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Function to send email
def send_email(data, recipient_email):
    sender_email = os.getenv("EMAIL_SENDER")  # Replace with your email
    sender_password = os.getenv("EMAIL_PASSWORD")  # Replace with your App password
    smtp_server = os.getenv("EMAIL_SMTP_SERVER")
    smtp_port = int(os.getenv("EMAIL_SMTP_PORT"))  # Ensure port is read as an integer

    subject = "Upcoming Tender Details"
    body = f"\nDear Recipient,\nPlease find attached the tender details for the selected date range.\n\nBest regards\nTender Notification System\n\n\n"

    # Convert data to DataFrame and sort by BidSubmissionClosingDate
    df = pd.DataFrame(data, columns=["BidSubmissionClosingDate", "TenderTitle", "ReferenceNumber", "TenderID", "EPublishedDate"])
    df['BidSubmissionClosingDate'] = pd.to_datetime(df['BidSubmissionClosingDate'])
    df_sorted = df.sort_values(by='BidSubmissionClosingDate', ascending=True)

    # Convert sorted data to HTML table
    table_html = df_sorted.to_html(index=False)

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(table_html, 'html'))

    # Convert DataFrame to CSV and attach as CSV file
    csv_buffer = StringIO()
    df_sorted.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)  # Move to the beginning of the file
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(csv_buffer.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename="tender_details.csv")
    msg.attach(part)

    # Connect to server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)