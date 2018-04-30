from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (uri)

db = client.get_default_database()
posts = db["posts"]

post = {
'title' : 'C4E',
'author' : 'Chung',
'content' : '''Cứ ăn chơi cho hết đời trai trẻ
rồi âm thầm lặng lẽ đạp xích lô''',
}
posts.insert_one(post)

all_posts = posts.find()
for post in all_posts:
    print(post)
