from flask_pymongo import PyMongo
from auth import app

app.config["MONGO_URI"] = "mongodb://localhost:27017/wad"
mongo = PyMongo(app)

def user_exist(login, password):
    user = list(mongo.db.users.find({"username":login.lower(), "password":password}).limit(1))
    if user:
        return True
    else:
        return False


def create_user(login, password):
    user = list(mongo.db.users.find({"username":login.lower()}).limit(1))
    if user:
        return True
    else:
        mongo.db.users.insert({"username":login.lower(),"password":password})
        return True

def showAllUsers():
    users = mongo.db.users.find({})
    return users


def change_pass(username, old_password, new_password):
    if user_exist(username, old_password):
        mongo.db.users.update({"username":username.lower()},{"username":username.lower(),"password":new_password})
        return True
    else:
        return False
