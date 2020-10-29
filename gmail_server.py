import email, smtplib, ssl, sys, os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

class Gmail_server:
    def __init__(self,user,pwd):
        while True:
            try:
                self.server = smtplib.SMTP("smtp.gmail.com", 587)
                self.server.ehlo()
                self.server.starttls()
                self.server.login(user, pwd)
                self.user = user
                print('gamil connection successful')
                break
            except:
                print ("failed to intial")
                print('retry the connnection')
                time.sleep(150)


    def close_email_server(self):
        self.server.close()

    def send_email(self, recipient, subject, body, base_dir, filename):

        FROM = self.user
        TO = recipient
        SUBJECT = subject
        

        message = MIMEMultipart()
        message["From"] = self.user
        message["To"] = recipient
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))
        

        # Open PDF file in binary mode
        with open(os.path.join(base_dir,filename), "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()
        try:
            self.server.sendmail(FROM, TO, text)
            print ('successfully sent the mail')
        except Exception as e:
            print ("failed to send mail",e)
