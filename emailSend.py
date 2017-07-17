import smtplib
import email.utils

smtpclient = smtplib.SMTP('smtp.gmail.com',587)
smtpclient.ehlo()
smtpclient.starttls()

user = "email@gmail.com"
passw = "senha"
to = "email2@gmail.com"
number = 1
msg = "Testando"

try:
 smtpclient.login(user,passw)
 print(" ~Logado com sucesso ")
except:
 print(" ~Email ou senha incorreto")

x = 0

while(x<number):
 smtpclient.sendmail(user,to,msg) 
 x=x+1
 print("Enviado ",x," Emails ")
