import pymongo
import ConfigParser

#DB Setup
__client = None
__db = None
cfg = open('./app/database/mongo-conf.cfg','r')
cfg_parser = ConfigParser.RawConfigParser()
cfg_parser.readfp(cfg)
__client = pymongo.MongoClient(cfg_parser.get('mongo-client','connection-string'))
__db = __client[cfg_parser.get('mongo-client','db-name')]
cfg.close()

def insert_to(coll,item):
	collection = __db[coll]
	item_id = collection.insert(item).__str__()
	return item_id
	
def get_from(coll,id):
	collection = __db[coll]
	query = {}
	query['id']=id
	item = collection.find_one(query)
	return item
	
def delete_from(coll,id):
	collection = __db[coll]
	query = {}
	query['id']=id
	collection.remove(query)
	
def update(coll,query,new_document):
	collection = __db[coll]
	collection.update(query,new_document,upsert=True,multi=False)