# ________________________________________________________________
# This file provides functions to:
# -- convert the Tate subject data into an RDF file (.ttl)
# -- create Graphviz-style edges for later visualization
# -- use those edges with Graphviz to create pdfs of hierarchy of concepts
# ________________________________________________________________

import json
# import graphviz
# from graphviz import Digraph

# ________________________________________________________________
# returns newdict, a dictionary of all id:name pairs, and prints out to a newdict.json file
# ________________________________________________________________
def create_newdict():
	with open('collection/processed/subjects/level0.json') as a: 
	    data = a.read()
	dict0 = json.loads(data) 
	with open('collection/processed/subjects/level1.json') as b: 
	    data = b.read()
	dict1 = json.loads(data) 
	with open('collection/processed/subjects/level2.json') as c:
	    data = c.read()
	dict2 = json.loads(data) 
	#combine all three dictionaries into one with all id:name pairs
	newdict = {**dict0, **dict1, **dict2} # dictionary of id:name pairs of all 15882 concepts of all levels
	# save this new full dictionary as txt to have just in case
	with open('newdict.json', 'w') as file:
	     file.write(json.dumps(newdict))
	print('New dict created!')
	return newdict

# ________________________________________________________________
# returns topConceptDict, a dict with the id:name of the TopConcepts
# ________________________________________________________________
def get_topConcepts():
	with open('collection/processed/subjects/level0.json') as a: 
	    data = a.read()
	topConcepts = json.loads(data) 
	return topConcepts

# ________________________________________________________________
# returns level1list, level2list : two lists of dicts that specify parent relationships
# ________________________________________________________________
def get_parent_rels():
	# FOR LEVEL 1:
	with open('collection/processed/subjects/level1list.json') as x: #the list of dics for level 1 concepts that have parents
	    datax = x.read()
	level1list = json.loads(datax) # this is the list of 142 dictionaries specifying parent relationships of level 1 concepts
	# FOR LEVEL 2:
	with open('collection/processed/subjects/level2list.json') as z: #the list of dics for level 2 concepts that have parents
	    dataz = z.read()
	level2list = json.loads(dataz) # this is the list of 2251 dictionaries specifying parent relationships of level 2 concepts
	print('Parent relationships acquired!')
	return level1list, level2list