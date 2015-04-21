"""
Created on Apr 10, 2015

@author: chris
"""

from app.database import mongo_client


COLLECTION_NAME = 'teams'

class TeamMapper(object):
    
    @classmethod
    def get_count(cls):
        return TeamMapper.get_collection().count()
    
    @classmethod
    def get_collection(cls):
        return mongo_client.db[COLLECTION_NAME]
    
    
    def to_hashmap(self):
        return self.__dict__
    
    @staticmethod
    def get(query_dict):
        return TeamMapper.get_collection().find_one(query_dict)
    
    @staticmethod
    def insert(student):
        return TeamMapper.get_collection().insert_one(student)
    
    @staticmethod
    def update(query_dict, update_dict):
        doc = TeamMapper.get_collection().update_one(query_dict, update_dict)
        
        if doc.modified_count == 1:
            return doc
        else:
            return None

    @staticmethod
    def delete(query_dict):
        doc = TeamMapper.get_collection().delete_one(query_dict)
        
        if doc.deleted_count == 1:
            return doc
        else:
            return None