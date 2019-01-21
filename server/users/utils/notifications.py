from users.utils import emails

def notify_invite(invitor, org, to_emails):
    from_email = 'yi.zhang7210@gmail.com'
    subject = 'You are invited by {0} to join {1}!'.format(
        invitor.given_name, org.name)
    content = 'You are now part of the {0} organization! Log in at {1}.'.format(
        org.name, 'https://dev.syllable.acre.one')

    email_client = emails.EmailClient()
    for to_email in to_emails:
        email = emails.create_email(from_email, to_email, subject, content)
        email_client.send_email(email)
