# ________________________________________________________________
# This file provides functions to:
# -- convert the Tate subject data into an RDF file (.ttl)
# -- create Graphviz-style edges for later visualization
# -- use those edges with Graphviz to create pdfs of hierarchy of concepts
# ________________________________________________________________

import json
# ________________________________________________________________
# returns level2_hlac_dict, a dict with the id:name of the level2 chosen hlacs
# _______________________________________________________________
def open_level2_hlac_dict():
	with open('output/hlac_hierarchy/level2_hlac_dict.json') as a: 
	    data = a.read()
	level2_hlac_dict = json.loads(data) 
	return level2_hlac_dict

def create_urls():
	urls = []
	count = 0
	for key, value in level2_hlac_dict.items():
		url = "https://www.tate.org.uk/search?cleared=1&st=" + str(key) + "&type=object"
		urls.append(url)
		count += 1
	url_dict = {}
	url_dict["urls"] = urls
	with open('output/parsehub/urls.json', 'w') as file:
		file.write(json.dumps(url_dict))
	return url_dict

level2_hlac_dict = open_level2_hlac_dict()
url_dict = create_urls()
print(len(url_dict["urls"]))

