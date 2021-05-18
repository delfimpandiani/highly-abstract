# ________________________________________________________________
# This file provides the functions for:
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# PRE-PROCESSING TATE INPUTS
### create_newdict(): returns (and print out as json) a dictionary of all 15882 tags used by Tate, by id:name pairs
### get_topConcepts(): returns topConceptDict, a dict with the id:name of the 16 level 0 TopConcepts 
### get_parent_rels(): returns level1list, level2list; two lists of dicts that specify parent relationships
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# TATE TAXONOMY RECONSTRUCTION AND FORMALIZATION
### get_tatetaxonomy_ttl(): outputs tate_taxonomy.ttl (RDF), using MUSCO ontology to represent the Tate taxonomy (2409 taxonomy subjects are represented)
######### outputs tate_taxonomy.ttl
### get_all_edges(): outputs alledges.json, which declares all 2393 graphviz-style edges in the Tate taxonomy, ordered by TopConcept
######### outputs graphviz/alledges.json
### get_edges_tc(): outputs 16 different json files, each of which contains a TopConcept's graphviz-style edges.
######### outputs graphviz/edges_tc_TCID.json
### get_gv_pdf(): outputs graphs for all Tate hierarchy concepts
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# SOCIAL CONCEPT TATE TAXONOMY RECONSTRUCTION AND FORMALIZATION
### get_sc_list(): returns a list of social concepts (previously manually selected)
### get_sc_tate_taxonomy_ttl(): outputs sc_tate_taxonomy.ttl (RDF), using MUSCO ontology to represent the SCs from Tate taxonomy, and returns dict of social concepts 
######### outputs sc_tate_taxonomy.ttl
### get_sc_dict(): returns and outputs as sc_dict.json a dictionary of id:name pairs of all 183 selected Social Concepts
######### outputs sc_dict.json
### get_narrow_sc_dict(): returns and outputs as narrow_sc_dict.json a dictionary of id:name pairs of the 166 narrow Social Concepts
######### outputs narrow_sc_dict.json
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# GATHERING ARTWORK DETAILS
### get_artworks_csv(): opens and returns the artwork_data.csv from the Tate Collection repository
### get_one_filename(): takes as input a row of artwork_data.csv, and returns the filename of a single artwork in the form "collection/artworks/a/000/a00001-1035.json"
### get_artworks_filenames(): returns and outputs artworks_filenames.json, a list of all 69,201 Tate artworks filenames of the form "collection/artworks/a/000/a00001-1035.json"
######### outputs artworks_filenames.json
### yield_tag_ids(artwork_dict): takes as input the Tate dictionary holding data of one single artwork, collects and yields all the tag ids for that artwork
### yield_tag_names(artwork_dict): takes as input the Tate dictionary holding data of one single artwork, collects and yields all the tag names for that artwork
### get_artwork_tags(artwork_filename): takes as input the Tate artwork filename, and returns two lists, one with tag ids, one with tag names
### get_all_artworks_tags(): returns and outputs two dicts each with 69201 entries, first contains the tags ids, the second tag names, for all artworks
######### outputs artworks_tag_ids_dict.json and artworks_tag_names_dict.json
### get_artwork_details(artwork_filename): takes as input the Tate artwork filename, and returns a dict details (tag ids; tag names; acno/artists/classification/date/medium/thumbnailCR/thumbnailURL/title/URL)
### get_all_artworks_details(): returns and outputs a dict of 69201 dicts called artworks_details_dict.json, which contains the selected details for all artworks in the Tate
######### outputs artworks_details_dict.json
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# SC-ARTWORK MATCHING
### get_sc_artworks_dict(): outputs and returns a dictionary with SC as key and list of artwork acno's as value 
######### outputs sc_artwork_matching/sc_artworks_dict.json
### get_sc_n_matches_sorted(): outputs and returns a dictionary with SCs as keys and value is number of artwork matches (sorted from most matches to least)
######### outputs sc_artwork_matching/sc_n_matches_sorted_dict.json
### get_match_details(input_sc): outputs and returns a dictionary for a specific SC, with info about related matches, tags, and image urls 
######### outputs sc_artwork_matching/sc_match_details/SCID_match_details.json
### get_co_tag_id_freq(input_sc): returns a dictionary for a specific SC, with tag ids as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/sc_co_tags/SCID_sorted_tag_ids.json
### get_co_tag_name_freq(input_sc): returns a dictionary for a specific SC, with tag names as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/sc_co_tags/SCID_sorted_tag_names.json
### get_all_scs_tag_ids(): returns and outputs dictionary of 166 dicts for each SC, with tag ids as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/all_scs_tag_ids.json
### get_all_scs_tag_names(): returns and outputs dictionary of 166 dicts for each SC, with tag names as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/all_scs_tag_names.json
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# CO-OCCURRING TAG ANALYSES
### get_objects_and_actions_dict(input_sc): returns and outputs two dictionaries, one holding tag ids and frequencies of "physical object tags", and another for "actions"
######### outputs output/sc_artwork_matching/sc_tag_analysis/SCID_only_objects_dict.json and output/sc_artwork_matching/sc_tag_analysis/SCID_actions_dict.json
### get_names_objects_and_actions_dict(input_sc): returns and outputs two dictionaries, one holding tag names and frequencies of "physical object tags", and another for "actions"
######### outputs output/sc_artwork_matching/sc_tag_analysis/SCID_objects_names.json and output/sc_artwork_matching/sc_tag_analysis/SCID_actions_names.json
### get_co_stats(): outputs a csv file with match stats for all 166 SCs
######### outputs output/match_stats.csv
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# DOMINANT COLOR ANALYSES
### getListOfFiles(): preprocessing of images in directory
### get_dom_colors_terminal(): prints commands to be passed through terminal to get the color palettes
### get_dom_colors(): returns the RGB coordinates and pixel count of the most dominant colors in an image
### get_avg_contrast(): returns the average contrast value of an image
### get_avg_sc_contrast(): returns the average contrast value for all available images tagged with a SC
# _______________________________________________________________
# ________________________________________________________________
# ________________________________________________________________

import json
import csv
import os
import extcolors
import PIL
import numpy as np
import cv2

# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# PRE-PROCESSING TATE INPUTS
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### create_newdict(): returns (and print out as json) a dictionary of all 15882 tags used by Tate, by id:name pairs
### ________________________________________________________________
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
	with open('newdict.json', 'w') as file:
	     file.write(json.dumps(newdict))
	return newdict

### ________________________________________________________________
### get_topConcepts(): returns topConceptDict, a dict with the id:name of the 16 level 0 TopConcepts 
### ________________________________________________________________
def get_topConcepts():
	with open('collection/processed/subjects/level0.json') as a: 
	    data = a.read()
	topConcepts = json.loads(data) 
	return topConcepts

### ________________________________________________________________
### get_parent_rels(): returns level1list, level2list; two lists of dicts that specify parent relationships
### ________________________________________________________________
def get_parent_rels():
	# FOR LEVEL 1:
	with open('collection/processed/subjects/level1list.json') as x: #the list of dics for level 1 concepts that have parents
	    datax = x.read()
	level1list = json.loads(datax) # this is the list of 142 dictionaries specifying parent relationships of level 1 concepts
	# FOR LEVEL 2:
	with open('collection/processed/subjects/level2list.json') as z: #the list of dics for level 2 concepts that have parents
	    dataz = z.read()
	level2list = json.loads(dataz) # this is the list of 2251 dictionaries specifying parent relationships of level 2 concepts
	return level1list, level2list


# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# TATE TAXONOMY RECONSTRUCTION AND FORMALIZATION
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### get_tatetaxonomy_ttl(): outputs tate_taxonomy.ttl (RDF), using MUSCO ontology to represent the Tate taxonomy. 
##### It checks all 15882 subject tags and represents only the 2409 which have hierarchical relations between them.
######### outputs tate_taxonomy.ttl
### ________________________________________________________________
def get_tatetaxonomy_ttl():
	topConcepts = get_topConcepts()
	newdict = create_newdict()
	level1list, level2list = get_parent_rels()
	keys_examined = 0
	keys_skosed = 0
	print("Outputting an RDF (.ttl) file representing the Tate taxonomy through MUSCO ontology.")
	with open("output/taxonomies/tate_taxonomy.ttl", "w") as f:
		print("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .", file=f)
		print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .', file=f)
		print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .', file=f)
		print('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .', file=f)
		print('@prefix : <https://w3id.org/musco/> .\n', file=f)
		print(':tate_taxonomy a :DataSetTaxonomy .\n', file=f)
		for key, value in newdict.items():
			if key in topConcepts:
				print(':tax_subject_' + str(key), file=f)
				print('\t a :TaxonomySubject ;', file=f)
				print('\t skos:inScheme :tate_taxonomy;', file=f)
				print('\t rdfs:label "' + str(value) + '" .', file=f)
				keys_skosed += 1
			else:
				for concept_dict in level1list:
					if int(key) == concept_dict["id"]:
						print(':tax_subject_' + str(key), file=f)
						print('\t a :TaxonomySubject ;', file=f)
						print('\t skos:inScheme :tate_taxonomy;', file=f)
						print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=f)
						print('\t rdfs:label "' + str(value) + '" .', file=f)
						keys_skosed += 1
				for concept_dict in level2list:
					if int(key) == concept_dict["id"]:
						print(':tax_subject_' + str(key), file=f)
						print('\t a :TaxonomySubject ;', file=f)
						print('\t skos:inScheme :tate_taxonomy;', file=f)
						print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=f)
						print('\t rdfs:label "' + str(value) + '" .', file=f)
						keys_skosed += 1
			keys_examined += 1
		print("Keys (concepts) examined: " + str(keys_examined))
		print("Keys (concepts) MUSCO-ed: " + str(keys_skosed))
	return

### ________________________________________________________________
### get_all_edges(): outputs alledges.json, which declares all 2393 graphviz-style edges in the Tate taxonomy, ordered by TopConcept
######### outputs graphviz/alledges.json
### ________________________________________________________________
def get_all_edges():
	topConcepts = get_topConcepts()
	newdict = create_newdict()
	level1list, level2list = get_parent_rels()
	edges_done = 0
	print("Outputting alledges.json, containing graphviz-edges for each TopConcept.")
	print("Number of TopConcepts to output edges for: " + str(len(topConcepts)))
	with open("output/graphviz/alledges.json", "w") as e:
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
			print("TopConcept '" + str(y) + "' done. Total edges done: " + str(edges_done))
		print("All done. Total edges done: " + str(edges_done)) #2393
	return e

### ________________________________________________________________
### get_edges_tc(): outputs 16 different json files, each of which contains a TopConcept's graphviz-style edges.
######### outputs graphviz/edges_tc_TCID.json
### ________________________________________________________________
def get_edges_tc():
	topConcepts = get_topConcepts()
	newdict = create_newdict()
	level1list, level2list = get_parent_rels()
	edges_done = 0
	print("Outputting individual edges_tc_TOPCONCEPTID.json files of graphviz-edges for each TopConcept")
	for x, y in topConcepts.items():
		print("Creating .json of edges relating to TopConcept " + str(x))
		with open("output/graphviz/edges_tc_" + str(x) + ".json", "w") as e:
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

### ________________________________________________________________
### get_gv_pdf(): outputs graphs for all Tate hierarchy concepts
### ________________________________________________________________
def get_gv_pdf(graphname, filename):
	g = Digraph('G', filename=str(graphname), engine='sfdp')
	g.attr(rankdir='LR', size='40,5', overlap='false')
	g.attr('edge', color='blue', arrowsize='.5')
	with open(filename) as f:
		content = f.readlines()
		for edge in content:
			edge
	g.view()
	return


# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# SOCIAL CONCEPT TATE TAXONOMY RECONSTRUCTION AND FORMALIZATION
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### get_sc_list(): returns a list of social concepts (previously manually selected)
### ________________________________________________________________
def get_sc_list():
	with open('input/sc_list.json') as a: 
	    data = a.read()
	sc_list = json.loads(data) 
	return sc_list

### ________________________________________________________________
### get_sc_tate_taxonomy_ttl(): outputs sc_tate_taxonomy.ttl (RDF), using MUSCO ontology to represent the SCs from Tate taxonomy, and returns dict of social concepts 
######### outputs sc_tate_taxonomy.ttl
### ________________________________________________________________
def get_sc_tate_taxonomy_ttl():
	print("Outputting an RDF (.ttl) file representing only (166) Social Concepts from the Tate taxonomy through MUSCO ontology.")

	try:
		with open("newdict.json") as a: 
			data = a.read()
			newdict = json.loads(data)
	except:
		newdict = create_newdict()

	topConcepts = get_topConcepts()
	level1list, level2list = get_parent_rels()
	sc_list = get_sc_list()
	keys_examined = 0
	keys_skosed = 0
	sc_dict = {}
	with open("output/taxonomies/sc_tate_taxonomy.ttl", "w") as f:
		print("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .", file=f)
		print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .', file=f)
		print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .', file=f)
		print('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .', file=f)
		print('@prefix : <https://w3id.org/musco/> .\n', file=f)
		print(':tate_taxonomy a :DataSetTaxonomy .\n', file=f)
		for key, value in newdict.items():
			if value in sc_list:
				if key in topConcepts:
					print(':tax_subject_' + str(key), file=f)
					print('\t a :TaxonomySubject ;', file=f)
					print('\t skos:inScheme :tate_taxonomy;', file=f)
					print('\t rdfs:label "' + str(value) + '" .', file=f)
					keys_skosed += 1
					sc_dict[key] = value 
				else:
					for concept_dict in level1list:
						if int(key) == concept_dict["id"]:
							if str(concept_dict['parent0']) == "29" or str(concept_dict['parent0']) == "132" or str(concept_dict['parent0']) =="145":
							# if the parent is the Top Concept "emotions, concepts, and ideas" or "religion and belief" or "society"
								print(':tax_subject_' + str(key), file=f)
								print('\t a :TaxonomySubject ;', file=f)
								print('\t skos:inScheme :tate_taxonomy;', file=f)
								print('\t skos:broader :' + str(concept_dict['parent0']) + ' ;', file=f)
								print('\t rdfs:label "' + str(value) + '" .', file=f)
								keys_skosed += 1
								sc_dict[key] = value 
					for concept_dict in level2list:
						if int(key) == concept_dict["id"]:
							if str(concept_dict['parent0']) == "29" or str(concept_dict['parent0']) == "132" or str(concept_dict['parent0']) == "145":
								print(':tax_subject_' + str(key), file=f)
								print('\t a :TaxonomySubject ;', file=f)
								print('\t skos:inScheme :tate_taxonomy;', file=f)
								print('\t skos:broader :' + str(concept_dict['parent1']) + ' ;', file=f)
								print('\t rdfs:label "' + str(value) + '" .', file=f)
								keys_skosed += 1
								sc_dict[key] = value
			keys_examined += 1
		print("Keys (concepts) examined: " + str(keys_examined))
		print("Keys (concepts) MUSCO-ed: " + str(keys_skosed))
	return sc_dict

### ________________________________________________________________
### get_sc_dict(): returns and outputs as sc_dict.json a dictionary of id:name pairs of all 183 selected Social Concepts
######### outputs sc_dict.json
### ________________________________________________________________
def get_sc_dict():
	sc_dict = get_sc_tate_taxonomy_ttl()
	print("Outputting sc_dict.json file, a dictionary of id:name pairs of all 183 selected SCs")
	with open('output/sc_dict.json', 'w') as t:
	    t.write(json.dumps(sc_dict))
	return sc_dict

### ________________________________________________________________
### get_narrow_sc_dict(): returns and outputs as narrow_sc_dict.json a dictionary of id:name pairs of the 166 narrow Social Concepts
######### outputs narrow_sc_dict.json
### ________________________________________________________________
def get_narrow_sc_dict():
	print("Outputting narrow_sc_dict.json file, a dictionary of id:name pairs of the 166 narrow selected SCs")

	try:
		with open("newdict.json") as a: 
			data = a.read()
			newdict = json.loads(data)
	except:
		newdict = create_newdict()
	try:
		with open("output/sc_dict.json.json") as a: 
			data = a.read()
			sc_list = json.loads(data)
	except:
		sc_list = get_sc_list()

	topConcepts = get_topConcepts()
	level1list, level2list = get_parent_rels()

	narrow_sc_dict = {}
	for key, value in newdict.items():
		if value in sc_list:
			for concept_dict in level2list:
				if int(key) == concept_dict["id"]:
					if str(concept_dict['parent0']) == "29" or str(concept_dict['parent0']) == "132" or str(concept_dict['parent0']) == "145":
						narrow_sc_dict[key] = value
	with open('output/narrow_sc_dict.json', 'w') as q:
	     q.write(json.dumps(narrow_sc_dict))
	return narrow_sc_dict


# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# GATHERING ARTWORK DETAILS
# ________________________________________________________________
# _______________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### get_artworks_csv(): opens and returns the artwork_data.csv from the Tate Collection repository
### ________________________________________________________________
def get_artworks_csv():
	tate = "collection"
	artworks = []
	c = 0
	with open(tate + '/artwork_data.csv', 'r') as csvfile: 
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in reader:
			c+=1
			if c == 1:
				continue
			try:
				artworks.append(row)
			except (ValueError, TypeError):
				continue
	return artworks

### ________________________________________________________________
### get_one_filename(): takes as input a row of artwork_data.csv, and returns the filename of a single artwork in the form "collection/artworks/a/000/a00001-1035.json"
### ________________________________________________________________
def get_one_filename(a_row):
    if a_row[1][0:2] == "AR":
        filename = "ar/" + a_row[1][2:5] + "/" + a_row[1] + "-" + a_row[0]
    else:
        filename = a_row[1][0:1] + "/" + a_row[1][1:4] + "/" + a_row[1] + "-" + a_row[0]
    filename = ("collection/artworks/" + filename + ".json").lower()
    return filename

### ________________________________________________________________
### get_artworks_filenames(): returns and outputs artworks_filenames.json, a list of all 69,201 Tate artworks filenames of the form "collection/artworks/a/000/a00001-1035.json"
######### outputs artworks_filenames.json
### ________________________________________________________________
def get_artworks_filenames():
	print("Outputting artworks_filenames.json file, a list of all artwork filenames in the Tate dataset")

	artworks = get_artworks_csv()
	artworks_filenames = []
	for artwork in artworks:
		artworks_filenames.append(get_one_filename(artwork))
	with open('output/artworks_filenames.json', 'w') as file:
		file.write(json.dumps(artworks_filenames))
	print("Length of the artworks_filenames list is", len(artworks_filenames))
	return artworks_filenames

### ________________________________________________________________
### yield_tag_ids(artwork_dict): takes as input the Tate dictionary holding data of one single artwork, collects and yields all the tag ids for that artwork
### ________________________________________________________________
def yield_tag_ids(artwork_dict):
    if 'id' in artwork_dict:
        yield artwork_dict['id']
    for k in artwork_dict:
        if isinstance(artwork_dict[k], list):
            for i in artwork_dict[k]:
                for j in yield_tag_ids(i):
                    yield j

### ________________________________________________________________
### yield_tag_names(artwork_dict): takes as input the Tate dictionary holding data of one single artwork, collects and yields all the tag names for that artwork
### ________________________________________________________________
def yield_tag_names(artwork_dict):
    if 'name' in artwork_dict:
        yield artwork_dict['name']
    for k in artwork_dict:
        if isinstance(artwork_dict[k], list):
            for i in artwork_dict[k]:
                for j in yield_tag_names(i):
                    yield j

### ________________________________________________________________
### get_artwork_tags(artwork_filename): takes as input the Tate artwork filename, and returns two lists, one with tag ids, one with tag names
### ________________________________________________________________
def get_artwork_tags(artwork_filename):
    d = {}
    artwork_tag_ids = []
    artwork_tag_names = []
    with open(artwork_filename) as a: 
        data = a.read()
    artwork_dict = json.loads(data)
    artwork_acno = artwork_dict["acno"]
    for k, v in artwork_dict.items():
        if k == "subjects":
            d = v
        artwork_tag_ids = list(yield_tag_ids(d))
        artwork_tag_names = list(yield_tag_names(d))
    return artwork_acno, artwork_tag_ids, artwork_tag_names

### ________________________________________________________________
### get_all_artworks_tags(): returns and outputs two dicts each with 69201 entries, first contains the tags ids, the second tag names, for all artworks
######### outputs artworks_tag_ids_dict.json and artworks_tag_names_dict.json
### ________________________________________________________________
def get_all_artworks_tags():
	print("Outputting two files: artworks_tag_ids_dict.json and artworks_tag_names_dict.json, dicts containing all tags for all artworks in the Tate dataset")

	try:
		with open("output/artworks_filenames.json") as a: 
			data = a.read()
			artworks_filenames = json.loads(data)
	except:
		artworks_filenames = get_artworks_filenames()

	artworks_tag_ids_dict = {}
	artworks_tag_names_dict = {}
	for artwork_filename in artworks_filenames:
		artwork_acno, artwork_tag_ids, artwork_tag_names = get_artwork_tags(artwork_filename)
		artworks_tag_ids_dict[artwork_acno] = artwork_tag_ids
		artworks_tag_names_dict[artwork_acno] = artwork_tag_names
	with open('output/artworks_tag_ids_dict.json', 'w') as file:
		file.write(json.dumps(artworks_tag_ids_dict))
	with open('output/artworks_tag_names_dict.json', 'w') as file:
		file.write(json.dumps(artworks_tag_names_dict))
	print("Number of keys in artworks_tag_ids_dict is", len(artworks_tag_ids_dict))
	print("Number of keys in artworks_tag_names_dict is", len(artworks_tag_names_dict))
	return artworks_tag_ids_dict, artworks_tag_names_dict

### ________________________________________________________________
### get_artwork_details(artwork_filename): takes as input the Tate artwork filename, and returns a dict details (tag ids; tag names; acno/artists/classification/date/medium/thumbnailCR/thumbnailURL/title/URL)
### ________________________________________________________________
def get_artwork_details(artwork_filename):
    d = {}
    artwork_details = {}
    with open(artwork_filename) as a: 
        data = a.read()
    artwork_dict = json.loads(data)
    for k, v in artwork_dict.items():
        if k == "subjects":
            d = v
        artwork_details["concept_ids"] = list(yield_tag_ids(d))
        artwork_details["concept_names"] = list(yield_tag_names(d))
    artwork_details["acno"] = artwork_dict["acno"]
    artwork_details["all_artists"] = artwork_dict["all_artists"]
    artwork_details["classification"] = artwork_dict["classification"]
    artwork_details["dateText"] = artwork_dict["dateText"]
    artwork_details["medium"] = artwork_dict["medium"]
    artwork_details["thumbnailCopyright"] = artwork_dict["thumbnailCopyright"]
    artwork_details["thumbnailUrl"] = artwork_dict["thumbnailUrl"]
    artwork_details["title"] = artwork_dict["title"]
    artwork_details["url"] = artwork_dict["url"]
    return artwork_details

### ________________________________________________________________
### get_all_artworks_details(): returns and outputs a dict of 69201 dicts called artworks_details_dict.json, which contains the selected details for all artworks in the Tate
######### outputs artworks_details_dict.json
### ________________________________________________________________
def get_all_artworks_details():  
	print("Outputting artworks_details_dict.json, a dict containing specific details for all artworks in the Tate dataset")

	try:
		with open("output/artworks_filenames.json") as a: 
			data = a.read()
			artworks_filenames = json.loads(data)
	except:
		artworks_filenames = get_artworks_filenames()

	artworks_details_dict = {}
	for artwork_filename in artworks_filenames:
		artworks_details_dict[artwork_filename] = get_artwork_details(artwork_filename)
	with open('output/artworks_details_dict.json', 'w') as file:
		file.write(json.dumps(artworks_details_dict))
	print("Number of keys in artworks_details_dict is", len(artworks_details_dict))
	return artworks_details_dict


# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# SC-ARTWORK MATCHING
# ________________________________________________________________
# _______________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### get_sc_artworks_dict(): outputs and returns a dictionary with SC as key and list of artwork acno's as value 
######### outputs sc_artworks_dict.json
### ________________________________________________________________
def get_sc_artworks_dict():
	print("Outputting artworks_details_dict.json, a dict containing specific detials for all artworks in the Tate dataset")

	try:
		with open("output/narrow_sc_dict.json") as a: 
			data = a.read()
			narrow_sc_dict = json.loads(data)
	except:
		narrow_sc_dict = get_narrow_sc_dict()
	try:
		with open("output/artworks_tag_ids_dict.json") as a: 
			data = a.read()
			artworks_tag_ids_dict = json.loads(data)
	except:
		artworks_tag_ids_dict, artworks_tag_names_dict = get_all_artworks_tags()

	sc_artworks_dict = {}
	for sc_id, sc_name in narrow_sc_dict.items(): #'232': 'freedom'
		sc_artworks_dict[sc_id] = []
		for acno, list_of_tags in artworks_tag_ids_dict.items(): #A0001": [1, 91, 92, 1050, 272, 897]
			for tag in list_of_tags:
				if sc_id == str(tag):
					sc_artworks_dict[sc_id].append(acno)
	with open('output/sc_artwork_matching/sc_artworks_dict.json', 'w') as file:
		file.write(json.dumps(sc_artworks_dict))
	return sc_artworks_dict # {"232": ["A0001", "A0241", "A0671", "A0206"], ...}

### ________________________________________________________________
### get_sc_n_matches_sorted(): outputs and returns a dictionary with SCs as keys and value is number of artwork matches (sorted from most matches to least)
######### outputs sc_n_matches_sorted_dict.json
### ________________________________________________________________
def get_sc_n_matches_sorted():
	print("Outputting sc_artwork_matching/sc_n_matches_sorted_dict.json, a dictionary with SCs as keys and value is number of artwork matches (sorted from most matches to least)")

	try:
		with open("output/sc_artwork_matching/sc_artworks_dict.json") as a: 
			data = a.read()
			sc_artworks_dict = json.loads(data)
	except:
		sc_artworks_dict = get_sc_artworks_dict() # {"232": ["A0001", "A0241", "A0671", "A0206"]. ...}

	sc_n_matches_sorted_dict = {}
	for sc_id, list_of_artworks in sc_artworks_dict.items():
		sc_n_matches_sorted_dict[sc_id] = len(list_of_artworks)
	sc_n_matches_sorted_dict = {k: v for k, v in sorted(sc_n_matches_sorted_dict.items(), key=lambda item: item[1], reverse=True)}
	with open('output/sc_artwork_matching/sc_n_matches_sorted_dict.json', 'w') as file:
		file.write(json.dumps(sc_n_matches_sorted_dict))
	return sc_n_matches_sorted_dict # {"722" : 368, "1715": 262, }

### ________________________________________________________________
### get_match_details(input_sc): outputs and returns a dictionary for a specific SC, with info about related matches, tags, and image urls 
######### outputs sc_artwork_matching/sc_match_details/SCID_match_details.json
### ________________________________________________________________
def get_match_details(input_sc):
	print("Outputting sc_artwork_matching/sc_match_details/" + str(input_sc) + "_match_details.json, a dictionary for that SC with info about related matches, tags, image urls")

	try:
		with open("output/sc_artwork_matching/sc_artworks_dict.json") as a: 
			data = a.read()
			sc_artworks_dict = json.loads(data)
	except:
		sc_artworks_dict = get_sc_artworks_dict() #"232": ["A0001", "A0241", "A0671", "A0206"]
	try:
		with open("output/artworks_details_dict.json") as a: 
			data = a.read()
			artworks_details_dict = json.loads(data)
	except:
		artworks_details_dict = get_all_artworks_details() # {"collection/artworks/a/000/a00001-1035.json": {"concept_ids": [1, 91, 92, 1050, 272, 694, 95, 195, 1134, 132, 5731, 5734], "concept_names": ["subject", "people", "actions: postures and motions", "arm/arms raised", "kneeling", "sitting", "adults", "man", "man, old", "religion and belief", "universal religious imagery", "blessing"], "acno": "A00001", "url": "http://www.tate.org.uk/art/artworks/blake-a-figure-bowing-before-a-seated-old-man-with-his-arm-outstretched-in-benediction-a00001", "thumbnailCopyright": null, "thumbnailUrl": "http://www.tate.org.uk/art/images/work/A/A00/A00001_8.jpg"}, ... }
	try:
		with open("output/narrow_sc_dict.json") as a: 
			data = a.read()
			narrow_sc_dict = json.loads(data)
	except:
		narrow_sc_dict = get_narrow_sc_dict() # {'232': 'freedom', '553': 'flirtation', '554': 'morality', '572': 'energy', '647': 'isolation', …}

	sc_match_details = {}
	for sc_id, list_of_artworks in sc_artworks_dict.items(): # "232": ["A0001", "A0241", "A0671", "A0206"]
		if sc_id == str(input_sc): 
			sc_match_details["sc_name"] = narrow_sc_dict[sc_id]
			sc_match_details["n_matches"] = len(list_of_artworks)
			sc_match_details["artwork_matches"] = list_of_artworks

			sc_match_details["related_tag_ids"] = {}
			sc_match_details["related_tag_names"] = {}
			sc_match_details["related_image_urls"] = {}
			for artwork in list_of_artworks:
				for artwork_path, artwork_details in artworks_details_dict.items():
					if artwork_details["acno"] ==  artwork:
						sc_match_details["related_tag_ids"][artwork] = artwork_details["concept_ids"]
						sc_match_details["related_tag_names"][artwork] = artwork_details["concept_names"]
						sc_match_details["related_image_urls"][artwork] = artwork_details["thumbnailUrl"]
	with open("output/sc_artwork_matching/sc_match_details/" + str(input_sc) + "_match_details.json", 'w') as file:
		file.write(json.dumps(sc_match_details))
	return sc_match_details

### ________________________________________________________________
### get_co_tag_id_freq(input_sc): returns and outputs dictionary for a specific SC, with tag ids as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/sc_co_tags/SCID_sorted_tag_ids.json
### ________________________________________________________________
def get_co_tag_id_freq(input_sc):
	print("Outputting sc_artwork_matching/sc_co_tags/" + str(input_sc) + "_sorted_tag_ids.json, a dictionary for that SC with freq of CO tag ids")

	try:
		with open("output/sc_artwork_matching/sc_match_details/" + str(input_sc) + "_match_details.json") as a: 
			data = a.read()
			sc_match_details = json.loads(data)
	except:
		sc_match_details = get_match_details(input_sc)

	co_tag_id_freq = {}
	related_tag_ids = sc_match_details["related_tag_ids"]
	for acno, tag_list in related_tag_ids.items():
		for tag_id in tag_list:
			if tag_id in co_tag_id_freq:
				co_tag_id_freq[tag_id] += 1
			else:
				co_tag_id_freq[tag_id] = 1
	sorted_tag_ids = {k: v for k, v in sorted(co_tag_id_freq.items(), key=lambda item: item[1], reverse=True)}
	with open("output/sc_artwork_matching/sc_co_tags/" + str(input_sc) + "_sorted_tag_ids.json", 'w') as file:
		file.write(json.dumps(sorted_tag_ids))
	return sorted_tag_ids # {1: 57, 29: 57, 30: 57, 572: 57, 184: 38, ...}

### ________________________________________________________________
### get_co_tag_name_freq(input_sc): returns and outputs dictionary for a specific SC, with tag names as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/sc_co_tags/SCID_sorted_tag_names.json
### ________________________________________________________________
def get_co_tag_name_freq(input_sc):
	print("Outputting sc_artwork_matching/sc_co_tags/" + str(input_sc) + "_sorted_tag_names.json, a dictionary for that SC with freq of CO tag names")

	try:
		with open("output/sc_artwork_matching/sc_match_details/" + str(input_sc) + "_match_details.json") as a: 
			data = a.read()
			sc_match_details = json.loads(data)
	except:
		sc_match_details = get_match_details(input_sc)

	co_tag_name_freq = {}
	related_tag_names = sc_match_details["related_tag_names"]
	for acno, tag_list in related_tag_names.items():
		for tag_name in tag_list:
			if tag_name in co_tag_name_freq:
				co_tag_name_freq[tag_name] += 1
			else:
				co_tag_name_freq[tag_name] = 1
	sorted_tag_names = {k: v for k, v in sorted(co_tag_name_freq.items(), key=lambda item: item[1], reverse=True)}
	with open("output/sc_artwork_matching/sc_co_tags/" + str(input_sc) + "_sorted_tag_names.json", 'w') as file:
		file.write(json.dumps(sorted_tag_names))
	return sorted_tag_names # {1: 57, 29: 57, 30: 57, 572: 57, 184: 38, ...}

### ________________________________________________________________
### get_all_scs_tag_ids(): returns and outputs dictionary of 166 dicts for each SC, with tag ids as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/all_scs_tag_ids.json
### ________________________________________________________________
def get_all_scs_tag_ids():
	print("Outputting sc_artwork_matching/all_scs_tag_ids.json, a dictionary of 166 dicts for each SC, with tag ids as keys and frequency of co-occurrence as values")

	try:
		with open("output/sc_artwork_matching/sc_n_matches_sorted_dict.json") as a: 
			data = a.read()
			sc_n_matches_sorted_dict = json.loads(data)
	except:
		sc_n_matches_sorted_dict = get_sc_n_matches_sorted()

	scs = sc_n_matches_sorted_dict.keys()
	count = 0
	all_scs_tag_ids = {}
	for sc in scs:
		all_scs_tag_ids[sc] = get_co_tag_id_freq(sc)
		print(str(sc) + " done!")
		count += 1
		print(count)
	with open("output/sc_artwork_matching/all_scs_tag_ids.json", 'w') as file:
		file.write(json.dumps(all_scs_tag_ids))
	print("Done with all " + str(count) + " SCs! Collected all their related tag ids and relative frequencies.")
	return all_scs_tag_ids

### ________________________________________________________________
### get_all_scs_tag_names(): returns and outputs dictionary of 166 dicts for each SC, with tag names as keys and frequency of co-occurrence as values
######### outputs sc_artwork_matching/all_scs_tag_names.json
### ________________________________________________________________
def get_all_scs_tag_names():
	print("Outputting sc_artwork_matching/all_scs_tag_names.json, a dictionary of 166 dicts for each SC, with tag names as keys and frequency of co-occurrence as values")

	try:
		with open("output/sc_artwork_matching/sc_n_matches_sorted_dict.json") as a: 
			data = a.read()
			sc_n_matches_sorted_dict = json.loads(data)
	except:
		sc_n_matches_sorted_dict = get_sc_n_matches_sorted()
	scs = sc_n_matches_sorted_dict.keys()
	count = 0
	all_scs_tag_names = {}
	for sc in scs:
		all_scs_tag_names[sc] = get_co_tag_name_freq(sc)
		print(str(sc) + " done!")
		count += 1
		print(count)
	with open("output/sc_artwork_matching/all_scs_tag_names.json", 'w') as file:
		file.write(json.dumps(all_scs_tag_names))
	print("Done with all " + str(count) + " SCs! Collected all their related tag names and relative frequencies.")
	return all_scs_tag_names


#________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# CO-OCCURRING TAG ANALYSIS
# ________________________________________________________________
# _______________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### get_objects_and_actions_dict(input_sc): returns and outputs two dictionaries, one holding tag ids and frequencies of "physical object tags", and another for "actions"
######### outputs output/sc_artwork_matching/sc_tag_analysis/SCID_only_objects_dict.json and output/sc_artwork_matching/sc_tag_analysis/SCID_actions_dict.json
### ________________________________________________________________
def get_objects_and_actions_dict(input_sc):
	print("Outputting sc_tag_analysis/" + str(input_sc) + "_po_act_dict.json, a dictionary for that SC with...")

	try:
		with open("newdict.json") as a: 
			data = a.read()
			newdict = json.loads(data)
	except:
		newdict = create_newdict()
	try:
		with open("output/sc_artwork_matching/sc_co_tags/" + str(input_sc) + "_sorted_tag_ids.json") as a: 
			data = a.read()
			related_tag_ids = json.loads(data)
	except:
		related_tag_ids = get_co_tag_id_freq(input_sc)

	topConcepts = get_topConcepts() # {"4":"group/movement","13":"architecture", ...}
	level1list, level2list = get_parent_rels()
	only_objects_dict = {} # will include objects, people, nature (animals, plants and flowers, trees, water, astronomy, seascapes and coasts)
	not_objects_dict = {}
	actions_dict = {}
	for tag_id, freq in related_tag_ids.items(): # 1, 40
		if str(tag_id) in topConcepts:
			not_objects_dict[str(tag_id)] = freq
		else:
			for concept_dict in level1list: # {"id":5731,"name":"universal religious imagery","parent0":132,"parent1":"none"}
				if int(tag_id) == concept_dict["id"]:  # if 1 == 5731
					if str(concept_dict['parent0']) == "78": # if super parent is object
						only_objects_dict[str(tag_id)] = freq
					else:
						not_objects_dict[str(tag_id)] = freq
			for concept_dict in level2list: # [{"id":5734,"name":"blessing","parent0":132,"parent1":5731}, ...]
				if int(tag_id) == concept_dict["id"]:  # if 1 == 5731
					if str(concept_dict['parent0']) == "78": # if super parent is object
						only_objects_dict[str(tag_id)] = freq
					if str(concept_dict['parent0']) == "91": # if super parent is people
						if str(concept_dict['parent1']) == "92" or str(concept_dict['parent1']) == "175" or str(concept_dict['parent1']) == "177":
							actions_dict[str(tag_id)] = freq 
						elif str(concept_dict['parent1']) == "94" or str(concept_dict['parent1']) == "95" or str(concept_dict['parent1']) == "98":
							only_objects_dict[str(tag_id)] = freq
					if str(concept_dict['parent0']) == "60": # if super parent is nature 
						if str(concept_dict['parent1']) == "61":
							actions_dict[str(tag_id)] = freq
						else:
							only_objects_dict[str(tag_id)] = freq
					else:
						not_objects_dict[str(tag_id)] = freq
	with open("output/sc_artwork_matching/sc_tag_analysis/" + str(input_sc) + "_only_objects_dict.json", 'w') as file:
		file.write(json.dumps(only_objects_dict))
	with open("output/sc_artwork_matching/sc_tag_analysis/" + str(input_sc) + "_actions_dict.json", 'w') as file:
		file.write(json.dumps(actions_dict))
	return only_objects_dict, actions_dict

### ________________________________________________________________
### get_names_objects_and_actions_dict(input_sc): returns and outputs two dictionaries, one holding tag names and frequencies of "physical object tags", and another for "actions"
######### outputs output/sc_artwork_matching/sc_tag_analysis/SCID_objects_names.json and output/sc_artwork_matching/sc_tag_analysis/SCID_actions_names.json
### ________________________________________________________________
def get_names_objects_and_actions_dict(input_sc):
	print("Outputting sc_tag_analysis/" + str(input_sc) + "_po_act_dict.json, a dictionary for that SC with...")

	try:
		with open("newdict.json") as a: 
			data = a.read()
			newdict = json.loads(data)
	except:
		newdict = create_newdict()
	only_objects_dict, actions_dict = get_objects_and_actions_dict(input_sc)
	objects_names = {}
	actions_names = {}
	for tag_id, freq in only_objects_dict.items():
		for key, value in newdict.items():
			if tag_id == key:
				objects_names[value] = freq
	for tag_id, freq in actions_dict.items():
		for key, value in newdict.items():
			if tag_id == key:
				actions_names[value] = freq
	with open("output/sc_artwork_matching/sc_tag_analysis/" + str(input_sc) + "_objects_names.json", 'w') as file:
		file.write(json.dumps(objects_names))
	with open("output/sc_artwork_matching/sc_tag_analysis/" + str(input_sc) + "_actions_names.json", 'w') as file:
		file.write(json.dumps(actions_names))
	return objects_names, actions_names

### ________________________________________________________________
### get_match_stats(): outputs a csv file with match stats for all 166 SCs
######### outputs output/match_stats.csv
### ________________________________________________________________
def get_match_stats():
    with open('output/sc_artwork_matching/all_scs_tag_ids.json') as a: 
        data = a.read()
    all_scs_tag_ids = json.loads(data) 
    narrow_sc_dict = get_narrow_sc_dict()
    sc_n_matches_sorted_dict = get_sc_n_matches_sorted()
    with open("output/match_stats.csv", "w") as f:
	    print("Social Concept,Concept ID,# Artwork Matches,# Related Tags,Avg. Freq. of Related Tags,# CO Objects,# CO Actions,Top 10 Objects,Avg_Freq_Top_Objects,Top 10 Actions,Avg_Freq_Top_Actions", file=f) 
	    for sc, tags_dict in all_scs_tag_ids.items(): # "722": {"1": 368, "145": 350, ...}
		    matches = sc_n_matches_sorted_dict[sc] # print("n of ARTWORKS MATCHED TO THAT SC ", matches)
		    sc_tag_n = len(tags_dict) # number of related tags # print("n of RELATED TAGS TO THAT HLAC ", hlac_tag_n)
		    values = tags_dict.values() # the numbers
		    total = sum(values) #total number of times all related tags appear
		    avfr = total/sc_tag_n #average number of times a related tags co-occurs with that hlac
		    # print("avg FREQ OF co-occurence with related tags of THAT HLAC ", avfr)
		    if os.path.exists("output/sc_artwork_matching/sc_co_tags/" + str(sc) + "_sorted_tag_ids.json"):
		        objects, actions = get_names_objects_and_actions_dict(sc)
		        n_co_ob = len(objects)
		        n_co_ac = len(actions)
		        top_actions_list = list(actions.items())[:10]
		        top_objects_list = list(objects.items())[:10]
		        top_objects = [item[0] for item in top_objects_list]
		        top_objects_pp = ' '.join(word for word in top_objects)
		        top_objects_pp = top_objects_pp.replace(',', '')
		        top_actions = [item[0] for item in top_actions_list]
		        top_actions_pp = ' '.join(word for word in top_actions)
		        top_actions_pp = top_actions_pp.replace(',', '')
		        if sum(item[1] for item in top_objects_list) != 0:
		        	top_ob_fr = sum(item[1] for item in top_objects_list)/len(top_objects)
		        if sum(item[1] for item in top_actions_list) != 0:
		            top_ac_fr = sum(item[1] for item in top_actions_list)/len(top_actions)
		        else:
		            top_ac_fr = 0
		    for sc_id, name in narrow_sc_dict.items():
		        if sc == sc_id:
		            sc_name = name
		    print(sc_name, ",", sc, ",", matches, ",",sc_tag_n,",", avfr,",", n_co_ob,",", n_co_ac,",", top_objects_pp,",", top_ob_fr,",", top_actions_pp,",", top_ac_fr, file=f)


#________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# DOMINANT COLOR ANALYSES
# ________________________________________________________________
# _______________________________________________________________
# ________________________________________________________________
### ________________________________________________________________
### getListOfFiles(): preprocessing of images in directory
### ________________________________________________________________
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath) 
    return allFiles

### ________________________________________________________________
### get_dom_colors_terminal(): prints commands to be passed through terminal to get the color palettes
### ________________________________________________________________
def get_dom_colors_terminal():
	consumerism_imgs = getListOfFiles("input/4063_paintings_prints")
	for filename in consumerism_imgs:
		print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")

	horror_images = getListOfFiles("input/795_paintings_prints")
	for filename in horror_images:
		print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")
	return

### ________________________________________________________________
### get_dom_colors(): returns the RGB coordinates and pixel count of the most dominant colors in an image
### ________________________________________________________________
def get_dom_colors():
	consumerism_imgs = getListOfFiles("input/4063_paintings_prints")
	for filename in consumerism_imgs:
		colors, pixel_count = extcolors.extract_from_path(filename)
		print(colors, pixel_count)

	horror_images = getListOfFiles("input/795_paintings_prints")
	for filename in horror_images:
		colors, pixel_count = extcolors.extract_from_path(filename)
		print(colors, pixel_count)
	return


### ________________________________________________________________
### get_avg_contrast(): returns the average contrast value of an image
###### the algorithm is based on this: https://stackoverflow.com/questions/57256159/how-extract-contrast-level-of-a-photo-opencv
### ________________________________________________________________
def get_avg_contrast(image_path):
    img = cv2.imread(image_path) # read image
    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB) # convert to LAB color space
    L,A,B=cv2.split(lab) # separate channels
    kernel = np.ones((5,5),np.uint8) # compute minimum and maximum in 5x5 region using erode and dilate
    min = cv2.erode(L,kernel,iterations = 1)
    max = cv2.dilate(L,kernel,iterations = 1)
    min = min.astype(np.float64) # convert min and max to floats
    max = max.astype(np.float64) # convert min and max to floats
    contrast = (max-min)/(max+min) # compute local contrast
    average_contrast = 100*np.mean(contrast) # get average across whole image
    print(image_path + " has an average contrast of " + str(average_contrast)+"%")
    return average_contrast

### ________________________________________________________________
### get_avg_sc_contrast(): returns the average contrast value for all available images tagged with a SC
###### the algorithm is based on this: https://stackoverflow.com/questions/57256159/how-extract-contrast-level-of-a-photo-opencv
### ________________________________________________________________
def get_avg_sc_contrast(sc):
    n = 0
    count = 0
    paths = "input/" + str(sc) + "_paintings_prints"
    sc_imgs = getListOfFiles(paths)
    for image_path in sc_imgs:
    	c = get_avg_contrast(image_path).tolist()
    	if np.isnan(c) == False:
    		x = float(c)
    		n += 1
    		count = count + x
    total = count/n
    print(str(sc) + " has an average contrast of " + str(total))
    return




# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# FUNCTION EXECUTION CHECK
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# TATE TAXONOMY RECONSTRUCTION AND FORMALIZATION
# get_tatetaxonomy_ttl()
# get_all_edges()
# get_edges_tc()
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# SOCIAL CONCEPT TATE TAXONOMY RECONSTRUCTION AND FORMALIZATION
# get_sc_tate_taxonomy_ttl()
# get_sc_dict()
# get_narrow_sc_dict()
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# GATHERING ARTWORK DETAILS
# get_artworks_filenames()
# print(get_artwork_tags("collection/artworks/a/000/a00001-1035.json"))
# get_all_artworks_tags()
# print(get_artwork_details("collection/artworks/a/000/a00001-1035.json"))
# get_all_artworks_details()
# ________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# SC-ARTWORK MATCHING
# get_sc_artworks_dict()
# get_sc_n_matches_sorted()
# get_match_details(572)
# get_co_tag_id_freq(572)
# get_co_tag_name_freq(572)
# get_all_scs_tag_ids()
# get_all_scs_tag_names()
#________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# CO TAG ANALYSIS
get_objects_and_actions_dict(572)
# get_names_objects_and_actions_dict(795)
# get_match_stats()
#________________________________________________________________
# ________________________________________________________________
# ________________________________________________________________
# DOMINANT COLOR ANALYSES
# get_dom_colors_terminal()
# get_dom_colors()
# get_avg_contrast("input/795_paintings_prints/N01110_8.jpg")
# get_avg_sc_contrast(795)

