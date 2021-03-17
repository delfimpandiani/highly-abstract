# OUTPUT: 2409 skos Concept entries

import timeit
from timeit import default_timer as timer
import json
from collections import OrderedDict

# ________________________________________________________________
# GOAL: get a dictionary that has all concept id:name pairs
# ________________________________________________________________
#open the three different level txt and make them dictionaries
with open('dict0.txt') as a: 
    data = a.read()
dict0 = json.loads(data) 
with open('dict1.txt') as b: 
    data = b.read()
dict1 = json.loads(data) 
with open('dict2.txt') as c:
    data = c.read()
dict2 = json.loads(data) 

#combine all three dictionaries into one with all id:name pairs
newdict = {**dict0, **dict1, **dict2} # dictionary of id:name pairs of all 15882 concepts of all levels

# save this new full dictionary as txt to have just in case
with open('newdict.txt', 'w') as file:
     file.write(json.dumps(newdict))

# ________________________________________________________________
# GOAL: get parent relationships
# ________________________________________________________________
# get the more complex lists of dics that specify parent relationships
# FOR LEVEL 1:
with open('level1list.txt') as x: #the list of dics for level 1 concepts that have parents
    datax = x.read()
level1list = json.loads(datax) # this is the list of 142 dictionaries specifying parent relationships of level 1 concepts
# FOR LEVEL 2:
with open('level2list.txt') as z: #the list of dics for level 2 concepts that have parents
    dataz = z.read()
level2list = json.loads(dataz) # this is the list of 2251 dictionaries specifying parent relationships of level 2 concepts

# ________________________________________________________________
# GOAL: get a list with the id's of the TopConcepts
# ________________________________________________________________
topConceptKeys = []
for key in dict0:
	topConceptKeys.append(key)

# ________________________________________________________________
# GOAL: print skos-style records for concepts that are part of the hierarchy, including their broader relationship
# OUTPUT: 2409 skos Concept entries
# ________________________________________________________________
#WARNING: if this code is run more than once, it will append the skos records again
# check that the code is only run once (i.e., that the output file does not exist yet)


# keys_examined = 0
# keys_skosed = 0

# start = timer()
# with open("output/skos_hierarchy_unordered.txt", "a") as f:
# 	print("Creating UNORDERED skos hierarchy document")
# 	for key, value in newdict.items():
# 		if key in topConceptKeys:
# 			print(':' + str(key), file=f)
# 			print('\t a skos:TopConcept ;', file=f)
# 			print('\t rdfs:label "' + str(value) + '" .', file=f)
# 			keys_skosed += 1
# 		else:
# 			for concept_dict in level1list:
# 				if int(key) == concept_dict["id"]:
# 					print(':' + str(key), file=f)
# 					print('\t a skos:Concept ;', file=f)
# 					print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=f)
# 					print('\t rdfs:label "' + str(value) + '" .', file=f)
# 					keys_skosed += 1
# 			for concept_dict in level2list:
# 				if int(key) == concept_dict["id"]:
# 					print(':' + str(key), file=f)
# 					print('\t a skos:Concept ;', file=f)
# 					print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=f)
# 					print('\t rdfs:label "' + str(value) + '" .', file=f)
# 					keys_skosed += 1
# 		keys_examined += 1
# 	print("Keys (concepts) examined: " + str(keys_examined))
# 	print("Keys (concepts) SKOS-ed: " + str(keys_skosed))
# end = timer()
# print("Time elapsed:", end - start)


# ________________________________________________________________
# GOAL: print skos-style records, for concepts that are part of the hierarchy, in chunks, ordered by TopConcept, including broader relationships
# OUTPUT: 2409 skos Concept entries
# ________________________________________________________________
#WARNING: if this code is run more than once, it will append the skos records again
# check that the code is only run once (i.e., that the output file does not exist yet)


# topkeys_examined = 0
# keys_skosed = 0

# start = timer()
# with open("output/skos_hierarchy_ordered.txt", "a") as s_k_o:
# 	print("Creating ORDERED skos hierarchy document")
# 	for x in topConceptKeys:
# 		for key, value in newdict.items():
# 			if key == x:
# 				print(':' + str(key), file=s_k_o)
# 				print('\t a skos:TopConcept ;', file=s_k_o)
# 				print('\t rdfs:label "' + str(value) + '" .', file=s_k_o)
# 				keys_skosed += 1
# 			else:
# 				for concept_dict in level1list:
# 					if str(concept_dict['parent0']) == x:
# 						if int(key) == concept_dict["id"]:
# 							print(':' + str(key), file=s_k_o)
# 							print('\t a skos:Concept ;', file=s_k_o)
# 							print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=s_k_o)
# 							print('\t rdfs:label "' + str(value) + '" .', file=s_k_o)
# 							keys_skosed += 1
# 				for concept_dict in level2list:
# 					if str(concept_dict['parent0']) == x:
# 						if int(key) == concept_dict["id"]:
# 							print(':' + str(key), file=s_k_o)
# 							print('\t a skos:Concept ;', file=s_k_o)
# 							print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=s_k_o)
# 							print('\t rdfs:label "' + str(value) + '" .', file=s_k_o)
# 							keys_skosed += 1
# 		topkeys_examined += 1
# 		print("TopConcepts examined: " + str(topkeys_examined))
# 		print("Keys (concepts) SKOS-ed: " + str(keys_skosed))
# end = timer()
# print("Time elapsed:", end - start)

# ________________________________________________________________
# GOAL: save graphviz-style edges in a file called edges.txt, ordered by the TopConcept they are connected to
# OUTPUT: 2393 graphviz style edge statements
# ________________________________________________________________

# edges_done = 0
# with open("output/edges.txt", "a") as e:
# 	print("Creating graphviz-style edges document ORDERED by TopConcept")
# 	for x, y in dict0.items():
# 		for key, value in newdict.items():
# 			if key != x:
# 				for concept_dict in level1list:
# 					if str(concept_dict['parent0']) == x:
# 						if int(key) == concept_dict["id"]:
# 							print('g.edge("' + concept_dict["name"] + '" , "' + y + '")', file=e)
# 							edges_done += 1
# 				for concept_dict in level2list:
# 					if str(concept_dict['parent0']) == x:
# 						if int(key) == concept_dict["id"]:
# 							(concept_dict['parent1'])
# 							print('g.edge("' + concept_dict["name"] + '" , "' + newdict[str(concept_dict['parent1'])] + '")', file=e)
# 							edges_done += 1
# 		print("TopConcept Done. Edges done: " + str(edges_done))
# 	print("All done. Edges done: " + str(edges_done)) #2393

# ________________________________________________________________


# ________________________________________________________________
# GOAL: save in different files graphviz-style edges for each TopConcept
# OUTPUT: 
# ________________________________________________________________

edges_done = 0
print("Creating graphviz-style edge statement documents for EACH TopConcept")
for x, y in dict0.items():
	with open("output/edges/" + str(x) + ".txt", "a") as e:
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

# ________________________________________________________________

