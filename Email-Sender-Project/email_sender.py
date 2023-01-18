from email.message import EmailMessage

#for security reasons password is saved in another file: password_variable
from password_variable import password
import ssl
import smtplib

email_sender = 'mariyapopova95@gmail.com'
email_password = password

email_receiver = 'popovagalina@abv.bg'

subject = 'Test'
body = """
Send email from Pycharm.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


