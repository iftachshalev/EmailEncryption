from EmailClass import EmailClass

email = input("email:")
password = input("pass:")

title = 'test email'
body = 'this is the body of the email... :)'

Operation = EmailClass(email, password)

Operation.SendEmail(email, title, body)
