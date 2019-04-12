import smtplib,ssl

port=465 #fro ssl

password=input("Versman1")

#create a secure SSL context

context= ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)as server:
    server.login("wawerupytedu12@gmail.com",password)
    #todo:send email here
    
