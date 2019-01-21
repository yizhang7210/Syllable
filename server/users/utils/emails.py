import os
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail

SENDGRID_API_KEY = 'SENDGRID_API_KEY'

class EmailClient:
    def __init__(self):
        print(os.environ.get(SENDGRID_API_KEY))
        self.sendgrid_api = sendgrid.SendGridAPIClient(apikey=os.environ.get(SENDGRID_API_KEY))

    def send_email(self, mail):
        response = self.sendgrid_api.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)

def create_email(from_email, to_email, subject, content):
    return Mail(Email(from_email), subject, Email(to_email), Content("text/plain", content))
