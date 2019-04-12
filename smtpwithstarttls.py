import smtplib,ssl

smtp_server="smtp.gmail.com"
port=587 #for starttls
sender_email="wawerupytedu12@gmail.com"

password=input("Versman1")

#create a secure ssl context

context=ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 