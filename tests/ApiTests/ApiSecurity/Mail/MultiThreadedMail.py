import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import threading

import allure


class TestMail:
    def send_email(self, email, password, recipient, subject, body):
        message = MIMEMultipart()
        message['From'] = email
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        img_path = 'image.png'
        # with open(img_path, 'rb') as f:
        #     img_data = f.read()
        #     image = MIMEImage(img_data, name='image.png')
        #     message.attach(image)

        try:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(email, password)
            smtp_server.sendmail(email, recipient, message.as_string())
            smtp_server.quit()
            print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Error sending email to {recipient}: {str(e)}")

    def test_multy_theared_mail_send(self):
        email = 'amielnoy@gmail.com'
        password = ['a1m2i3!@']#, 'a1m2i3s4', 'your-password']
        recipients = ['amielnoy@gmail.com', 'amiel.noyfeld@gmail.com', 'amiel.noyfeld@gmail.com']
        #recipients = "amielnoy@gmail.com,amiel.noyfeld@gmail.com,amiel.noyfeld@gmail.com".split(",")
        #recipients =['a']
        subject = 'Test Email'
        body = 'This is a test email from Python'

        #recipients = ', '.join(recipients)
        threads = []
        #for i in range(3):
        recipients = [ recipient_encode.encode('UTF-8') for recipient_encode in recipients]
        #for recipient in recipients:
        #    print("recipents="+str(recipients))
        recipient = 'amielnoy@gmail.com'


        # t = threading.Thread(target=self.send_email, args=[email, password, 'amielnoy@gmail.com', subject, body])
        # t.start()
        # threads.append(t)
        #
        # for thread in threads:
        #     thread.join()
