# ________________________________________________________________
# This file provides functions to:
# -- convert the Tate subject data into an RDF file (.ttl)
# -- create Graphviz-style edges for later visualization
# -- use those edges with Graphviz to create pdfs of hierarchy of concepts
# ________________________________________________________________

import json
from cleaninput import create_newdict, get_topConcepts, get_parent_rels
# import graphviz
# from graphviz import Digraph

# ________________________________________________________________
# GOAL: print skos-based .ttl records for concepts that are part of the hierarchy, including their broader relationship
# outputs a .ttl file with the records of all 2409 subjects that are part of the hierarchy
# WARNING: if this code is run more than once, it will append the skos records again
# check that the code is only run once (i.e., that output/skos_unordered.ttl does not exist yet)
# ________________________________________________________________
def get_skosed_unordered(newdict, topConcepts, level1list, level2list):
	print("Creating UNORDERED skos hierarchy .ttl file")
	keys_examined = 0
	keys_skosed = 0
	with open("output/complete_hierarchy/skosed_unordered.ttl", "a") as f:
		print("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .", file=f)
		print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .', file=f)
		print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .', file=f)
		print('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .', file=f)
		print('@prefix : <https://w3id.org/hlac/> .\n', file=f)
		for key, value in newdict.items():
			if key in topConcepts:
				print(':' + str(key), file=f)
				print('\t a skos:TopConcept ;', file=f)
				print('\t rdfs:label "' + str(value) + '" .', file=f)
				keys_skosed += 1
			else:
				for concept_dict in level1list:
					if int(key) == concept_dict["id"]:
						print(':' + str(key), file=f)
						print('\t a skos:Concept ;', file=f)
						print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=f)
						print('\t rdfs:label "' + str(value) + '" .', file=f)
						keys_skosed += 1
				for concept_dict in level2list:
					if int(key) == concept_dict["id"]:
						print(':' + str(key), file=f)
						print('\t a skos:Concept ;', file=f)
						print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=f)
						print('\t rdfs:label "' + str(value) + '" .', file=f)
						keys_skosed += 1
			keys_examined += 1
		print("Keys (concepts) examined: " + str(keys_examined))
		print("Keys (concepts) SKOS-ed: " + str(keys_skosed))
	return

# ________________________________________________________________
# GOAL: print, ordered by TopConcept, skos-based .ttl records for concepts that are part of the hierarchy, including their broader relationship
# outputs a .ttl file with the records of all 2409 subjects that are part of the hierarchy
# WARNING: if this code is run more than once, it will append the skos records again
# check that the code is only run once (i.e., that output/skos_ordered.ttl does not exist yet)
# ________________________________________________________________
def get_skosed_ordered(newdict, topConcepts, level1list, level2list):
	print("Creating ORDERED skos hierarchy .ttl file")
	topkeys_examined = 0
	keys_skosed = 0
	with open("output/complete_hierarchy/skosed_ordered.ttl", "a") as g:
		print("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .", file=g)
		print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .', file=g)
		print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .', file=g)
		print('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .', file=g)
		print('@prefix : <https://w3id.org/hlac/> .\n', file=g)
		for x in topConcepts:
			for key, value in newdict.items():
				if key == x:
					print(':' + str(key), file=g)
					print('\t a skos:TopConcept ;', file=g)
					print('\t rdfs:label "' + str(value) + '" .', file=g)
					keys_skosed += 1
				else:
					for concept_dict in level1list:
						if str(concept_dict['parent0']) == x:
							if int(key) == concept_dict["id"]:
								print(':' + str(key), file=g)
								print('\t a skos:Concept ;', file=g)
								print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=g)
								print('\t rdfs:label "' + str(value) + '" .', file=g)
								keys_skosed += 1
					for concept_dict in level2list:
						if str(concept_dict['parent0']) == x:
							if int(key) == concept_dict["id"]:
								print(':' + str(key), file=g)
								print('\t a skos:Concept ;', file=g)
								print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=g)
								print('\t rdfs:label "' + str(value) + '" .', file=g)
								keys_skosed += 1
			topkeys_examined += 1
			print("TopConcepts examined: " + str(topkeys_examined))
			print("Keys (concepts) SKOS-ed: " + str(keys_skosed))
		return

# ________________________________________________________________
# outputs a .json file that declares all 2393 graphviz-style edges, ordered by the TopConcept
# ________________________________________________________________

def get_all_edges(topConcepts, newdict, level1list, level2list):
	edges_done = 0
	with open("output/complete_hierarchy/alledges.json", "a") as e:
		print("Creating ordered graphviz-style edges for all concepts in the hierarchy")
		for x, y in topConcepts.items():
			for key, value in newdict.items():
				if key != x:
					for concept_dict in level1list:
						if str(concept_dict['parent0']) == x:
							if int(key) == concept_dict["id"]:
								print('g.edge("' + concept_dict["name"] + '" , "' + y + '")', file=e)
								edges_done += 1
					for concept_dict in level2list:
						if str(concept_dict['parent0']) == x:
							if int(key) == concept_dict["id"]:
								(concept_dict['parent1'])
								print('g.edge("' + concept_dict["name"] + '" , "' + newdict[str(concept_dict['parent1'])] + '")', file=e)
								edges_done += 1
			print("TopConcept '" + str(y) + "' done. Edges done: " + str(edges_done))
		print("All done. Edges done: " + str(edges_done)) #2393
	return e


# ________________________________________________________________
# outputs save in different files graphviz-style edges for each TopConcept
# ________________________________________________________________
def get_edges_tc(topConcepts, newdict, level1list, level2list):
	edges_done = 0
	for x, y in topConcepts.items():
		print("Creating .json of edges relating to TopConcept " + str(x))
		with open("output/complete_hierarchy/edges/" + str(x) + ".json", "a") as e:
			for key, value in newdict.items():
				if key != x:
					for concept_dict in level1list:
						if str(concept_dict['parent0']) == x:
							if int(key) == concept_dict["id"]:
								print('g.edge("' + concept_dict["name"] + '" , "' + y + '")', file=e)
								edges_done += 1
					for concept_dict in level2list:
						if str(concept_dict['parent0']) == x:
							if int(key) == concept_dict["id"]:
								(concept_dict['parent1'])
								print('g.edge("' + concept_dict["name"] + '" , "' + newdict[str(concept_dict['parent1'])] + '")', file=e)
								edges_done += 1
			print("TopConcept '" + str(y) + "' done. Edges done: " + str(edges_done))
			print("All done. Edges done: " + str(edges_done)) #2393
	return e

# ________________________________________________________________
# outputs graphviz-based pdf for all the concepts
# ________________________________________________________________
# def get_gv_pdf(graphname, filename):
# 	g = Digraph('G', filename=str(graphname), engine='sfdp')
# 	g.attr(rankdir='LR', size='40,5', overlap='false')
# 	g.attr('edge', color='blue', arrowsize='.5')
# 	with open(filename) as f:
# 		content = f.readlines()
# 		for edge in content:
# 			edge
# 	g.view()
# 	return
# ________________________________________________________________







topConcepts = get_topConcepts()
newdict = create_newdict()
level1list, level2list = get_parent_rels()
get_skosed_unordered(newdict, topConcepts, level1list, level2list)
get_skosed_ordered(newdict, topConcepts, level1list, level2list)
get_all_edges(topConcepts, newdict, level1list, level2list)
get_edges_tc(topConcepts, newdict, level1list, level2list)
# # allgraphedges = get_all_edges()
# # get_gv_pdf(alledges.gv, allgraphedges)
# print("hi")

