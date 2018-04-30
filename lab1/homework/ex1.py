import datetime
now = datetime.datetime.now()
# print(now)
print ("{0}:{1}:{2}\n{3}/{4}/{5}".format(now.hour,now.minute,now.second,now.day,now.month,now.year))
