import pymongo
from pymongo import MongoClient

MyClient = MongoClient()

#database
db = MyClient.mydb

#table aka collection 'user table'
users = db.users
# print(users)

#inser one data
# user1 = {"username":"nick","password":"mypass","favourite_number":445,"hobbies":["python","games","pizza"]}

# inserted_one_data = users.insert_one(user1)
# print(inserted_one_data.inserted_id)


#insert many data
# user_list = [{"username":"shamu","pass":"123"},{"username":"ramu","pass":"234"}]

# insert_many = users.insert_many(user_list)
# print(insert_many,insert_many.inserted_ids)


#counting

print(users.find().count())
print(users.find({"favourite_number":445}).count())
print(users.find({"username":"shamu"}).count())




