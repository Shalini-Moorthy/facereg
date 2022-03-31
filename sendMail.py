import smtplib
from email.message import EmailMessage
def email_alert(to,result):
    subject=""
    body=""
    if result=='yes':
        subject="Alert: Face not recognized"
        body="Someone is trying to initiate a transaction and it has not been recognized as you. If it wasn't you kindly take necessary steps"
    else:
        subject = "Alert: Transaction is going to start"
        body = "The transaction is going to get initiated. If it wasn't you kindly take necessary steps"
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    user="secureonlinetransaction@gmail.com"
    msg['from']=user
    password="tuzgmrushgnnmfbx"
    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


