import pymongo
import json
from pymongo import MongoClient, InsertOne
import os
from utils import logger
import config_parser

client = pymongo.MongoClient(config_parser.get_config()['mongo_client'])

db = client.bds_crawl_db
collection = db.bds
root_dir = r"C:\Users\dinh\PycharmProjects\bds_scrapy\output"

def get_all_file_names():
    file_set = set()
    # for dir_, _, files in os.walk(root_dir):
    #     for file_name in files:
    #         rel_dir = os.path.relpath(dir_, root_dir)
    #         rel_file = os.path.join(rel_dir, file_name)
    #         file_set.add(rel_file)
    # return file_set
    for file_name in os.listdir(root_dir):
        full_path = os.path.join(root_dir, file_name)
        if os.path.isfile(full_path):
            file_set.add(full_path)
    return file_set

if __name__ == '__main__':
    logger.get_logger().info(f'Start get file name in {root_dir}')
    file_set = get_all_file_names()

    logger.get_logger().info('Start build request')
    requesting = []
    for file in file_set:
        with open(file, encoding="utf8") as f:
            for jsonObj in f:
                myDict = json.loads(jsonObj)
                requesting.append(InsertOne(myDict))
                # result = collection.bulk_write([InsertOne(myDict)])
    result = collection.bulk_write(requesting)
    client.close()
    logger.get_logger().info('Pushed to Mongodb')