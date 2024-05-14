#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name:
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that changes all topics of a school document based on the name:
    """
    
    result = mongo_collection.find({"topics": topic})
    return list(result)
