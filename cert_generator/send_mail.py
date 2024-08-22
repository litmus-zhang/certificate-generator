import resend
import os
import streamlit as st


def send_mail(recipient, subject, body, attachment):
    resend.api_key = st.secrets["mail_credential"]["RESEND_API_KEY"]
    print(f"API KEY {resend.api_key}")
    body = """
                <p>Dear Attendee,</p>
                <p>Congratulations on completing the course. attached  is your certificate.</p>
                <p>Best regards,</p>
                <p>AIRLAB x BLSC Foundation</p>
            """

    params: resend.Emails.SendParams = {
        "from": "AIRLAB x BLSC <airolunilag@gmail.com>",
        "to": [recipient],
        "subject": subject,
        "html": body,
        "attachments": [
            {
                "filename": attachment,
                "content": "base64_encoded_pdf",
                "type": "application/pdf",
            }
        ],
    }

    return resend.Emails.send(params)
