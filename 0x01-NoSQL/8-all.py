#!/usr/bin/env python3
""" Python script that lists all documents in mongodb"""


def list_all(mongo_collection):
    """ lists all documents """
    all_docs = [document for document in mongo_collection.find()]
    return all_docs
