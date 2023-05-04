import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import yagmail

fromaddr = ['amielnoy@gmail.com']
sendto = ['amielnoy@gmail.com']

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = sendto
msg['Subject'] = 'This is cool'

body = "this is the body of the text message"


class TestSendmail:
    def send_mail(self):
        msg.attach(MIMEText(body, 'plain'))

        # filename = 'Work.xlsx'
        # attachment = open('/home/mark/Work.xlsx', 'rb')

        # part = MIMEBase('application', "octet-stream")
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

        msg.attach(part)

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('amielnoy@gmail.com', 'a1m2i3!@')

        text = msg.as_string()
        smtpObj.sendmail(fromaddr, sendto, text)
        smtpObj.quit()

    def send_yaga_simple(self):
        try:
            # initializing the server connection
            yag = yagmail.SMTP(user='amielnoy@gmail.com', password='a1m2i3!')
            # sending the email
            yag.send(to='amielnoy@gmail.com', subject='Testing Yagmail', contents='Hurray, it worked!')
            print("Email sent successfully")
        except:
            print("Error, email was not sent")

    def test_send_mail(self):
        self.send_mail()

    def test_send_yaga_mail(self):
        self.send_yaga_simple()
