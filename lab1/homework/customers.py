from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (uri)

db = client.get_default_database()
posts = db["customers"]

list = ['ads','events','wom']
counts = []

for ref in list:
        count = posts.find({'ref' : ref}).count()
        counts.append(count)

pyplot.pie(counts,labels=list,autopct="%.2f%%")
pyplot.title("Statistical tables")
pyplot.axis("equal")
pyplot.show()
