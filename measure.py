from faker import Faker
from pymongo import MongoClient
from time import time

faker = Faker()
client = MongoClient('localhost', 27017)
db = client.wad


def timer(function, count = 0):
    timer = time()
    if count == 0:
        function()
    else:
        function(count)
    print(str(function)+" выполнилась за "+str(time()-timer))

def clear():
    db.users.drop()

def find():
    users = db.users.find({"username": "Matthew_Burke"})
    for user in users:
        print(user)

def inserting(count):
    db.users.insert_many([{"username": faker.name().replace(" ", "_"), "password": faker.name().replace(" ", "")} for _ in range(count)])

def indexCreatng():
    db.users.createIndex({"username" : 1})

counts = [100000, 1000000]
for count in counts:
    print("trying with "+str(count))
    timer(clear)
    timer(inserting, count)
    timer(find)
    input("create index, type enter")
    timer(find)
    print("\n\n")

#timer(find)
