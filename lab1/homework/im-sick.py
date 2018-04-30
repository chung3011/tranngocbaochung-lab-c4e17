from gmail import GMail, Message
import datetime
gmail = GMail('20150413@student.hust.edu.vn','chung20150413')
while True:
    time = datetime.datetime.now()
    if time.hour == 7 and time.minute > 0 :
        msg = Message('Test Message',to='chung.hitc97@gmail.com',text="I'm sick")
        gmail.send(msg)
        break
