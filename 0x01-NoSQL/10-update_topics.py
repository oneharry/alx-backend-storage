#!/usr/bin/env python3
""" Python script on mongodb"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document"""
    '''school_document = mongo_collection.find_one({'name': name})'''

    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
