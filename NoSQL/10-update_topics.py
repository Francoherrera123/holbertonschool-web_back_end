#!/usr/bin/env python3
"""
Task 10
"""

def update_topics(mongo_collection, name, topics):
    """
    Inserts a new document in a collection 
    """
    myquery = {"name" : name}
    newquery = {"$set": {"topics": topics}}

    return mongo_collection.update_many(myquery, newquery)
