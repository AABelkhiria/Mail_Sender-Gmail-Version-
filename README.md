# Mail_Sender (Gmail Version)

This program written in Python allows you to send a mail to multiple adresses located in the list.txt file.

## How to use

Before executing the main.py python program, you will have to edit the program to fill your mail adress, your password, the mail topic, the mail body and the path of the file to attach.

* For safety reasons, make sure to delete your password from the program source !

* In order to attach multiple files, you have to duplicate the **##attachment** section like follow :

```python
    # open the file to be sent 
    filename = "file2.ext"
    attachment = open("file2.ext", "rb")
     
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
     
    # To change the payload into encoded form
    p.set_payload((attachment).read())
     
    # encode into base64
    encoders.encode_base64(p)
      
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
```

* You are asked to delete the **##attachment** section if you don't want to attach any file in your mail.
