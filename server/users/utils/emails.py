import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail

SENDGRID_API_KEY = 'SENDGRID_API_KEY'

class EmailClient:
    def __init__(self):
        print(os.environ.get(SENDGRID_API_KEY))
        self.sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(SENDGRID_API_KEY))

    def send_email(self, mail):
        response = self.sg.client.mail.send.post(request_body=mail.get())

def create_email(from_email, to_email, subject, content):
    return Mail(Email(from_email), subject, Email(to_email), Content("text/plain", content))
