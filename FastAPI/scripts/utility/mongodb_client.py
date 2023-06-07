from pymongo import MongoClient
from scripts.constants.app_constants import Mongo

intern_client = MongoClient(Mongo.mongo_db)
intern_db = intern_client.interns_b2_23
course_list = intern_db.gokkul
