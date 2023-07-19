#!/usr/bin/env python3
""" Python script for mongodb """


def schools_by_topic(mongo_collection, topic):
    """Return list of scools with specifictoic"""
    schools_with_topic = mongo_collection.find({'topics': topic})
    return list(schools_with_topic)
