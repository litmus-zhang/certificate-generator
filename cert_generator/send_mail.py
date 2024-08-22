import resend
import os


class Mailer:
    def __init__(self):
        self.resend = resend
        self.resend.api_key = os.environ["RESEND_API_KEY"]

    def send_mail(self, recipient, subject, body, attachment):
        body = f"""
                <p>Dear Attendee,</p>
                <p>Congratulations on completing the course. attached  is your certificate.</p>
                <p>Best regards,</p>
                <p>AIRLAB x BLSC Foundation</p>
            """

        params: resend.Emails.SendParams = {
            "from": "Acme <onboarding@resend.dev>",
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
