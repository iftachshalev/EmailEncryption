import smtplib


class EmailClass:

    def __init__(self, EMAIL_ADDRESS, EMAIL_PASSWORD):
        self.EMAIL_ADDRESS = EMAIL_ADDRESS
        # login to gmail
        self.smtp = smtplib.SMTP("smtp.gmail.com", 587)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()
        self.smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    def disconnect(self):
        self.smtp.__exit__()

    def SendEmail(self, to_addr, title, body):

        msg = f"subject: {title}\n\n{body}"

        self.smtp.sendmail(self.EMAIL_ADDRESS, to_addr, msg)

    def ReceiveEmail(self):
        pass