import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  
fromaddr = "your mail here"

with open('list.txt','r') as f :
    mails = f.readlines()

for mail in mails:
    print('sending to ',mail.split()[0])
    toaddr = mail.split()[0]
      
    # instance of MIMEMultipart
    msg = MIMEMultipart()
     
    # storing the senders email address  
    msg['From'] = fromaddr
     
    # storing the receivers email address 
    msg['To'] = toaddr
     
    # storing the subject 
    msg['Subject'] = "The mail subject here !"
     
    # string to store the body of the mail
    body = "The mail body here !"
    
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
     
     
    ## Attachment of file1.ext file
    # open the file to be sent 
    filename = "file1.ext"
    attachment = open("file1.ext", "rb")
     
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
     
    # To change the payload into encoded form
    p.set_payload((attachment).read())
     
    # encode into base64
    encoders.encode_base64(p)
      
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

     
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
     
    # start TLS for security
    s.starttls()
     
    # Authentication
    s.login(fromaddr, "Password here !")
     
    # Converts the Multipart msg into a string
    text = msg.as_string()
     
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
     
    # terminating the session
    s.quit()
