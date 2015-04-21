from app.database import mongo_client
from pydoc import Doc

#Kaity was here.

COLLECTION_NAME = 'messages'

class BasicMessageMapper(object):
	@classmethod
	def get_count(cls):
        return BasicMessageMapper.get_collection().count()
    
	@classmethod
	def get_collection(cls):
		return mongo_client.db[COLLECTION_NAME]
    
    
    def to_hashmap(self):
        return self.__dict__
		
class UserMessageMapper(BasicMessageMapper):
    """Mapper class for UserMessage. Contains functions for database calls."""
    
    @staticmethod
    def get(query_dict):
        """Get Message based on query_dict"""
        return BasicMessageMapper.get_collection().find_one(query_dict)
    
    @staticmethod
    def insert(message):
        """Insert a new user message into the collection"""
        return BasicMessageMapper.get_collection().insert_one(message)
    
    @staticmethod
    def update(query_dict, update_dict):
        doc = BasicMessageMapper.get_collection().update_one(query_dict, update_dict)
        
        if doc.modified_count == 1:
            return doc
        else:
            return None

    @staticmethod
    def delete(query_dict):
        doc = BasicMessageMapper.get_collection().delete_one(query_dict)
        
        if doc.deleted_count == 1:
            return doc
        else:
            return None
			
class TeamMessageMapper(BasicMessageMapper):
    """Mapper class for UserMessage. Contains functions for database calls."""
    
    @staticmethod
    def get(query_dict):
        """Get Message based on query_dict"""
        return BasicMessageMapper.get_collection().find_one(query_dict)
    
    @staticmethod
    def insert(message):
        """Insert a new user message into the collection"""
        return BasicMessageMapper.get_collection().insert_one(message)
    
    @staticmethod
    def update(query_dict, update_dict):
        doc = BasicMessageMapper.get_collection().update_one(query_dict, update_dict)
        
        if doc.modified_count == 1:
            return doc
        else:
            return None

    @staticmethod
    def delete(query_dict):
        doc = BasicMessageMapper.get_collection().delete_one(query_dict)
        
        if doc.deleted_count == 1:
            return doc
        else:
            return None