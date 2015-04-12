"""
Created on Apr 10, 2015

@author: chris
"""

from app.database import mongo_client


COLLECTION_NAME = 'users'

class UserMapper(object):
    
    @classmethod
    def get_count(cls):
        return UserMapper.get_collection().count()
    
    @classmethod
    def get_collection(cls):
        return mongo_client.db[COLLECTION_NAME]
    
    
    def to_hashmap(self):
        return self.__dict__


class StudentMapper(UserMapper):
    """Mapper class for students. Contains functions for database calls."""
    
    @classmethod
    def get(cls, query_dict):
        """Get Student based on query_dict"""
        return UserMapper.get_collection().find_one(query_dict)
    
    @staticmethod
    def insert(student):
        """Insert a new student into the collection"""
        pass
    
    @staticmethod
    def update(query_dict, update_dict):
        pass
    
    @staticmethod
    def delete(query_dict):
        pass
    

class InstructorMapper(UserMapper):
    
    def __init__(self):
        pass