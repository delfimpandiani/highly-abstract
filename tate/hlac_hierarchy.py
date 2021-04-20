# ________________________________________________________________
# This file provides functions to:
# -- convert the Tate subject data into an RDF file (.ttl)
# -- create Graphviz-style edges for later visualization
# -- use those edges with Graphviz to create pdfs of hierarchy of concepts
# ________________________________________________________________

import json
from cleaninput import create_newdict, get_topConcepts, get_parent_rels

# ________________________________________________________________
# returns topConceptDict, a dict with the id:name of the TopConcepts
# _______________________________________________________________
def get_all_hlacs():
	with open('chosen_hlacs/all_hlacs_list.json') as a: 
	    data = a.read()
	all_hlacs_list = json.loads(data) 
	return all_hlacs_list

# ________________________________________________________________
# outputs 2 files:
# ---.ttl file with skos entries for all hlacs (and their parents)
# ---.json dictionary of id-name pairs for all hlacs (and their parents)
# returns the hlac_dict ^
# ________________________________________________________________
def get_hlacs_skosed(newdict, topConcepts, level1list, level2list, all_hlacs_list):
	print("Creating ALL HLACs skos hierarchy .ttl file")
	keys_examined = 0
	keys_skosed = 0
	hlac_dict = {}
	with open("output/hlac_hierarchy/hlacs_skosed.ttl", "w") as f:
		print("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .", file=f)
		print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .', file=f)
		print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .', file=f)
		print('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .', file=f)
		print('@prefix : <https://w3id.org/hlac/> .\n', file=f)
		for key, value in newdict.items():
			if value in all_hlacs_list:
				if key in topConcepts:
					print(':' + str(key), file=f)
					print('\t a skos:TopConcept ;', file=f)
					print('\t rdfs:label "' + str(value) + '" .', file=f)
					keys_skosed += 1
					hlac_dict[key] = value 
				else:
					for concept_dict in level1list:
						if int(key) == concept_dict["id"]:
							if str(concept_dict['parent0']) == "29" or str(concept_dict['parent0']) == "132" or str(concept_dict['parent0']) =="145":
								print(':' + str(key), file=f)
								print('\t a skos:Concept ;', file=f)
								print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=f)
								print('\t rdfs:label "' + str(value) + '" .', file=f)
								keys_skosed += 1
								hlac_dict[key] = value 
					for concept_dict in level2list:
						if int(key) == concept_dict["id"]:
							if str(concept_dict['parent0']) == "29" or str(concept_dict['parent0']) == "132" or str(concept_dict['parent0']) == "145":
								print(':' + str(key), file=f)
								print('\t a skos:Concept ;', file=f)
								print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=f)
								print('\t rdfs:label "' + str(value) + '" .', file=f)
								keys_skosed += 1
								hlac_dict[key] = value
			keys_examined += 1
		print("Keys (concepts) examined: " + str(keys_examined))
		print("Keys (concepts) SKOS-ed: " + str(keys_skosed))
	with open('output/hlac_hierarchy/hlac_dict.json', 'w') as t:
	    t.write(json.dumps(hlac_dict))
	return hlac_dict

# ________________________________________________________________
# returns a dictinary with id:label for each of the level 2 (most specific) hlacs
# ________________________________________________________________
def get_level2_hlac_dict(newdict, topConcepts, level1list, level2list, all_hlacs_list):
	print("Creating LEVEL 2 HLACs skos hierarchy dictionary file")
	level2_hlac_dict = {}
	for key, value in newdict.items():
		if value in all_hlacs_list:
			for concept_dict in level2list:
				if int(key) == concept_dict["id"]:
					if str(concept_dict['parent0']) == "29" or str(concept_dict['parent0']) == "132" or str(concept_dict['parent0']) == "145":
						level2_hlac_dict[key] = value
	with open('output/hlac_hierarchy/level2_hlac_dict.json', 'w') as q:
	     q.write(json.dumps(level2_hlac_dict))
	return level2_hlac_dict







topConcepts = get_topConcepts()
newdict = create_newdict()
level1list, level2list = get_parent_rels()
all_hlacs_list = get_all_hlacs()
print(type(all_hlacs_list))
print(all_hlacs_list)
hlac_dict = get_hlacs_skosed(newdict, topConcepts, level1list, level2list, all_hlacs_list)
level2_hlac_dict = get_level2_hlac_dict(newdict, topConcepts, level1list, level2list, all_hlacs_list)
print("length of all hlac dict is ", len(hlac_dict))
print("length of level 2 dict is ", len(level2_hlac_dict))
