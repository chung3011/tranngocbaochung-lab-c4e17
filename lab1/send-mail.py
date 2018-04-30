from gmail import GMail, Message
from random import choice

gmail = GMail('20150413@student.hust.edu.vn','chung20150413')
# html_template="a {{a}}"
# sick=['bbb','ccc','ddd']
# sickness=choice(sick)
# html_content='abc'
# html_content=html_template.replace('{{a}}',sickness)
# msg = Message('Test Message',to='chung.hitc97@gmail.com',text='Hello')
msg = Message('Test Message',to='chung.hitc97@gmail.com',html='<p><img src="http://cfile26.uf.tistory.com/original/99F901405AD87EC31947E7" alt="" /></p>')
# msg = Message('Test Message',to='chung.hitc97@gmail.com',html=html_content)
gmail.send(msg)
