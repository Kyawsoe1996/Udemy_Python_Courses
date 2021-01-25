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

# print(users.find().count())
# print(users.find({"favourite_number":445}).count())
# print(users.find({"username":"shamu"}).count())
# print(users.find({"username":"ramu"}).count())


#Multiple Find Conditions
print(users.find({"username":"nick","favourite_number":445}).count())

#Datetime and keywords

import datetime

current_date = datetime.datetime.now()
print(current_date)
old_date = datetime.datetime(2019,11,24)
print(old_date)

#insert users with date
# uid = users.insert({"username":"bishnu", "date":current_date})
# print(uid)
#after insert users with the date, find query

#gte => greater than or equal , lte => Less than or equal
print(users.find({"date":{"$gte":old_date}}).count())
print(users.find({"date":{"$lte":old_date}}).count())

#this is for the date column existing lists
print(users.find({"date":{"$exists":False}}).count())

#$ne => Not Equal to

#User table mr "shamu" so tat username net ma tu tat count
print(users.find({"username":{"$ne":"shamu"}}).count())


#Indexes => When having multiple query output for userlists, it will improve query speed

index_created = db.users.create_index([('username',pymongo.ASCENDING)])
print(index_created)

#After that find related query. If there will have multiple users record
print(users.find({"username":"nick"}))
print(users.find({"username":"nick"}).count() == 2)
print(users.find({"username":"john"}).count())



