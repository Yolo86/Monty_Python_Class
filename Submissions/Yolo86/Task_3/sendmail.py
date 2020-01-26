import smtplib,getpass

n= str(input('Email: '))
p= str(input('Password: '))

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()

mail.login(n,p)
rec = str(input('Recepient Email: '))
sub = str(input('Subject: '))
mes = str(input('Message: '))
body = f'Subject: {sub} \nMessage: {mes}'
mail.sendmail(n,rec,body)

mail.quit()
