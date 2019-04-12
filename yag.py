import yagmail

receiver = "waweruedwin2@gmail.com"
body = "Hello there from Yagmail"
filename = "total.csv"

yag = yagmail.SMTP("wawerupytedu12@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)