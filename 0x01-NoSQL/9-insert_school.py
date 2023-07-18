#!/usr/bin/env python3
""" Python script for mongodb"""


def insert_school(mongo_collection, **kwargs):
    """ Insert new document in a collection based on kwargs"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
