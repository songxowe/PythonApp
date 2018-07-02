import pymongo

word='课程顾问'
client = pymongo.MongoClient('127.0.0.1')
db = client['zhaopin']
table = db['机器学习']
table.remove({'zwmc': {'$regex': word}})
