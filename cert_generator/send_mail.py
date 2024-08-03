import mailerlite as MailerLite
import os


class Mailer:

    def __init__(self):
        self.client = MailerLite.Client({"api_key": os.getenv("MAILER_API_KEY")})

        self.client.groups.create("AIRLAB-BLSC Bootcamp 2024")

    def send_mail(
        self,
        recipient,
        message,
        sender="airolunilag@gmail.com",
    ):
        params = {
            "name": "Certificate Distribution",
            "language_id": 1,
            "type": "regular",
            "emails": [
                {
                    "subject": "Certificate of completion",
                    "from_name": "AIROL x BLSC Bootcamp ",
                    "from": recipient,
                    "content": message,
                }
            ],
        }

        self.client.campaigns.create(params)

    def add_to_group(self, email, fullname, track):
        self.client.subscribers.create(
            email, fields={"fullname": fullname, "track": track}
        )
