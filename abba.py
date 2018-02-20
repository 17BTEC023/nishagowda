Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("nayanagowdama@gmail.com", "7795822731")
 
# message to be sent
message = "hello"
 
# sending the mail
s.sendmail("nayanagowdama@gmail.com", "yusufhvr@gmail.com", message)
 
# terminating the session
s.quit()
