#!/usr/bin/env python3
"""
Task 8
"""

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.
    """
    return [i for i in mongo_collection.find()]
