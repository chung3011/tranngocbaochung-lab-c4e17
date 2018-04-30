from pymongo import MongoClient

# connect db server
uri = "mongodb://admin:admin@ds259119.mlab.com:59119/chung"
client = MongoClient (uri)

# get default db
db = client.get_default_database()

# get blog collection
blog = db["blog"]

# write new blog
post = {
'title' : 'xyzabc',
'content' : 'abcxyz'
}
blog.insert_one(post)

all_posts = blog.find()
for post in all_posts:
    print(post)
