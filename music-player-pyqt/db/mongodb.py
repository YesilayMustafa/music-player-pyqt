from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, db_name="deneme"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.users = self.db["kullanicilar"]

    def find_user(self, username, password):
        return self.users.find_one({"kullanici_adi": username, "sifre": password})

    def user_exists(self, username):
        return self.users.find_one({"kullanici_adi": username}) is not None

    def create_user(self, username, password):
        self.users.insert_one({"kullanici_adi": username, "sifre": password})
