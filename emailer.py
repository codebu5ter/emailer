from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = input("Enter your email address (Gmail):")
password = input("Enter your password: ")
from_email = username
to_list = []
t = True
while (t):
    to_list.append(input("Enter the email address of receiver: "))
    put = input("Do you want to enter more email adresses? (y/n)")
    if (put == "n" or put == "N"):
        t = False

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
try:
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list,
                        "Hello there! This is an email message.")
except SMTPAuthenticationError:
    print("Could not log in. Please check your login credentials.")
    exit()
except SMTPException:
    print("An error occured!")
    exit()
email_conn.quit()
print("Email successfully sent!")
