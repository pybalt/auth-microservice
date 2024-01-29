import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from utils.logger import logger

mongo_client = MongoClient(os.environ.get('MONGO_URL'))

"name_database = mongo_client[name_database]"

try:
    mongo_client.admin.command('ping')
    logger.info('MongoDB is up.')
except ServerSelectionTimeoutError:
    logger.error('MongoDB is down.')
    exit(1)