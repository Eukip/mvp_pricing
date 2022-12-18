# todo написать коннектор монго pymongo
# todo написать логгер в монго по каждой стратегии
import os
from pymongo import MongoClient


client = MongoClient(host=os.environ.get("MONGO_INITDB_HOST", "mongodb"),
                     port=os.environ.get("MONGO_INTIDB_PORT", 27015),
                     username=os.environ.get("MONGO_INITDB_ROOT_USERNAME", "root"),
                     password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD", "admin"))
                     
mongo_db = client[os.environ.get("MONGO_INITDB_DATABASE", "mvp_pricing")]
