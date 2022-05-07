import smtplib
import datetime as dt


myemail='sjitbh121993@gmail.com'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=myemail, password=your_password)
    connection.sendmail(from_addr=myemail, to_addrs='sjitbh@rediffmail.com', msg='Subject:Hello\n\n This is my mail body ')

    connection.close()
