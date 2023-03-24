import smtplib as sm
import getpass as gp

sender = raw_input("Enter your email ID : ")
passw=gp.getpass("Enter the password : ")
receiver=raw_input("Enter the destination email : ")
message = raw_input("Enter the message : ")

try:
	smtpObj=sm.SMTP('smtp.gmail.com',587)
	smtpObj.starttls()
	smtpObj.login(sender, passw)
	smtpObj.sendmail(sender, receiver, message)
	print "E-Mail sent successfully"
	smtpObj.close()
except sm.SMTPException:
	print "Failed to send the message. Try again"