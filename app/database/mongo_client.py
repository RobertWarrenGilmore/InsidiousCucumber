import pymongo
import ConfigParser

__client = None
__db = None
cfg = open('./mongo-conf.cfg','r')
cfg_parser = ConfigParser.RawConfigParser()
cfg_parser.readfp(cfg)
__client = pymongo.MongoClient(cfg_parser.get('mongo-client','connection-string'))
__db = __client[cfg_parser.get('mongo-client','db-name')]
cfg.close()

def insert_to(coll,object):
	collection = __db[coll]
	object_id = collection.insert(object).__str__()
	return object_id
	
def get_from(coll,id):
	collection = __db[coll]
	query = {}
	query['id']=id
	object = collection.find_one(query)
	return object
	
def update(coll,query,new_document):
	collection = __db[coll]
	collection.update(query,new_document,upsert=True,multi=False)