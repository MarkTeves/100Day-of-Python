import smtplib
import ssl

## run this command in terminal to start the server
## python -m smtpd -c DebuggingServer -n localhost:1025

## works with python < 3.12

smtp_server = "localhost"
port = 1025  # For starttls
sender_email = "my@gmail.com"
password = ""
receiver_email = "your@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
