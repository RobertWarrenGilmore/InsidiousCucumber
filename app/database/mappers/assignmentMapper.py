"""
Created on Apr 10, 2015

@author: chris
"""

from app.database import mongo_client


COLLECTION_NAME = 'assignments'

class AssignmentMapper(object):
    
    @classmethod
    def get_count(cls):
        return AssignmentMapper.get_collection().count()
    
    @classmethod
    def get_collection(cls):
        return mongo_client.db[COLLECTION_NAME]
    
    
    def to_hashmap(self):
        return self.__dict__


class DeliverableMapper(AssignmentMapper):
    
    @staticmethod
    def get(query_dict):
        return AssignmentMapper.get_collection().find_one(query_dict)
    
    @staticmethod
    def insert(student):
        return AssignmentMapper.get_collection().insert_one(student)
    
    @staticmethod
    def update(query_dict, update_dict):
        doc = AssignmentMapper.get_collection().update_one(query_dict, update_dict)
        
        if doc.modified_count == 1:
            return doc
        else:
            return None

    @staticmethod
    def delete(query_dict):
        doc = AssignmentMapper.get_collection().delete_one(query_dict)
        
        if doc.deleted_count == 1:
            return doc
        else:
            return None

class TaskMapper(AssignmentMapper):
    
    @staticmethod
    def get(query_dict):
        return AssignmentMapper.get_collection().find_one(query_dict)
    
    @staticmethod
    def insert(student):
        return AssignmentMapper.get_collection().insert_one(student)
    
    @staticmethod
    def update(query_dict, update_dict):
        doc = AssignmentMapper.get_collection().update_one(query_dict, update_dict)
        
        if doc.modified_count == 1:
            return doc
        else:
            return None

    @staticmethod
    def delete(query_dict):
        doc = AssignmentMapper.get_collection().delete_one(query_dict)
        
        if doc.deleted_count == 1:
            return doc
        else:
            return None