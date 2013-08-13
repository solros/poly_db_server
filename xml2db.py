#!/usr/bin/python

# This script inserts data into a MongoDB database. It should be run on the polymake server (or potentially any other database server).
# It should be run as xml2db.py database_name collection_name contributor FILES


#from elementtree import ElementTree
import xml.etree.cElementTree as ElementTree
import sys
import array
import string
import pymongo
import datetime
import time

import db_properties

def poly2dict(file, db_name, collection_name, contrib, date): 
	start()		
	tree = ElementTree.parse(file)
	root = tree.getroot()

	mt('parse')
	
	name = root.attrib['name']
	
	start()
	dict = {}
	
	dict['_id'] = name
	dict['date'] = date
	dict['contributor'] = contrib

	simple_properties = db_properties.simple_p(collection_name)
	vector_properties = db_properties.vector_p(collection_name)
	matrix_properties = db_properties.matrix_p(collection_name)

	for p in root.findall('{http://www.math.tu-berlin.de/polymake/#3}property'):
		key = p.attrib['name']
		if key in simple_properties:
			val = parse_simple(p)
			dict[key] = val
		elif key in vector_properties:
			val = parse_vector(p[0])
			dict[key] = val
		elif key in matrix_properties:
			val = parse_matrix(p[0])
			dict[key] = val
	mt('dict')
	return dict


def parse_simple(p):
	val = p.attrib['value']
	if val == 'false': 
		val = 0
	elif val == 'true':
		val = 1
	else:
		val = int(val)
	return val

def parse_vector(p):
	x = p.text
	val = x.split(' ')
	return val

def parse_matrix(p):
	val = []
 	for v in p:
 		val.append(parse_vector(v))
	
	return val
	

def poly2json(dict):
	return make_json_string(dict)

def make_json_simple(key, value):
	return ''.join(['"',key,'": "',value,'"'])

def make_json_string(dict):
	s = "{\n" +	string.join((make_json_simple(k,v) for k,v in dict.iteritems()), ',\n') + "\n}"
	return s
	
	

def add_to_db(db_name, collection, contrib, obj):
	mongo = pymongo.MongoClient("localhost", 27017)
	db = mongo[db_name]
	db[collection].insert(poly2dict(obj, db_name, collection, contrib, datetime.datetime.now().strftime("%Y-%m-%d")))


def add_list_to_db(db_name, collection, contrib, objects):
	mongo = pymongo.MongoClient("localhost", 27017)
	db = mongo[db_name]
	date = datetime.datetime.now().strftime("%Y-%m-%d")
	docs = []
	for obj in objects:
		docs.append(poly2dict(obj, db_name, collection, contrib, date))
	start()
	db[collection].insert(docs)
	mt('db')

def pt(s):
	print s
	print time.time()-starting_time


def start():
	global clock
	clock = time.time()
	

def mt(x):
	global parsetime
	global dicttime
	global dbtime
	dur = time.time()-clock
	if x == 'parse':
		parsetime += dur
	if x == 'dict':
		dicttime += dur
	if x == 'db':
		dbtime += dur

def printtime():
	print "parsing: " + repr(parsetime)
	print "dictionary: " + repr(dicttime)
	print "db: " + repr(dbtime)

		
clock = 0	
parsetime = 0
dicttime = 0
dbtime = 0
starting_time = time.time()

#db_name = "LatticePolytopes"
#collection = "SmoothReflexive"
#contrib = "Andreas Paffenholz"
date = datetime.datetime.now().strftime("%Y-%m-%d")

db_name = sys.argv[1]
collection = sys.argv[2]
contrib = sys.argv[3]

add_list_to_db(db_name, collection, contrib, sys.argv[4:])
printtime()

#poly2dict(sys.argv[1],contrib,date)