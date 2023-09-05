#!/usr/bin/env python3
"""
Task 12
"""
from pymongo import MongoClient

list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    get = nginx_collection.count_documents({"methods": "GET"})
    print(f"\tmethod GET: {get}")
    get = nginx_collection.count_documents({"methods": "POST"})
    print(f"\tmethod POST: {get}")
    get = nginx_collection.count_documents({"methods": "PUT"})
    print(f"\tmethod PUT: {get}")
    get = nginx_collection.count_documents({"methods": "PATCH"})
    print(f"\tmethod PATCH: {get}")
    get = nginx_collection.count_documents({"methods": "DELETE"})
    print(f"\tmethod DELETE: {get}")
    get = nginx_collection.count_documents({"methods": "GET", "path": "/status"})
    print(f"{get} status check")
