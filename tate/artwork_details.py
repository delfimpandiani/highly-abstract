import json
import csv
 # by the end of this, I get a json dumped final_dict.json dict that holds all the artworks (And their tags, tag ids, and whether they have a thumbnail url)

def get_artworks_csv():
# Opens the artwork_data.csv from the Tate
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

def get_filename(a_row):
# Input: a row of the artwork_data.csv
# Returns the filename of a single artwork in the form "collection/artworks/a/000/a00001-1035.json"
    if a_row[1][0:2] == "AR":
        filename = "ar/" + a_row[1][2:5] + "/" + a_row[1] + "-" + a_row[0]
    else:
        filename = a_row[1][0:1] + "/" + a_row[1][1:4] + "/" + a_row[1] + "-" + a_row[0]
    filename = ("collection/artworks/" + filename + ".json").lower()
    return filename

def get_all_artwork_filenames_list():
# Reuses the function get_filename(a_row)
# Returns and saves to an output file highly-abstract/tate/output/artwork_details/artwork_filenames_list.json
    artworks = get_artworks_csv()
    artwork_filenames_list = []
    for artwork in artworks:
        artwork_filenames_list.append(get_filename(artwork))
    with open('output/artwork_details/artwork_filenames_list.json', 'w') as file:
        file.write(json.dumps(artwork_filenames_list))
    # OUTPUT: JSON file holding a list of all 69,201 filenames of the form "collection/artworks/a/000/a00001-1035.json"
    return artwork_filenames_list

def get_concept_ids(d):
# Input is the Tate dictionary of data for a single artwork
# Collects the tag ids for a single artwork
    if 'id' in d:
        yield d['id']
    for k in d:
        if isinstance(d[k], list):
            for i in d[k]:
                for j in get_concept_ids(i):
                    yield j

def get_concept_names(d):
# Input is the Tate dictionary of data for a single artwork
# Collects the tag names for a single artwork
    if 'name' in d:
        yield d['name']
    for k in d:
        if isinstance(d[k], list):
            for i in d[k]:
                for j in get_concept_names(i):
                    yield j

def get_artwork_details(artwork):
# Reuses the function (get_concept_ids(d)
# Reuses the function (get_concept_names(d)
# Returns a dictionary of specific details for a single artwork (concept ids in that artwork, 
# the concept names, the acno (id) of the artwork, the url of the artwork, the thumbnail copyright, 
# and the thumbnailUrl)
    d = {}
    artwork_details = {}
    with open(artwork) as a: 
        data = a.read()
    artwork_dict = json.loads(data)
    for k, v in artwork_dict.items():
        if k == "subjects":
            d = v
        artwork_details["concept_ids"] = list(get_concept_ids(d))
        artwork_details["concept_names"] = list(get_concept_names(d))
    artwork_details["acno"] = artwork_dict["acno"]
    artwork_details["url"] = artwork_dict["url"]
    artwork_details["thumbnailCopyright"] = artwork_dict["thumbnailCopyright"]
    artwork_details["thumbnailUrl"] = artwork_dict["thumbnailUrl"]
    return artwork_details


def get_all_artworks_details(artwork_filenames_list):  
# Returns and saves to an output file highly-abstract/tate/output/artwork_details/all_artwork_details_dict.json
    all_artworks_details_dict = {}
    for artwork in artwork_filenames_list:
        all_artworks_details_dict[artwork] = get_artwork_details(artwork)
    with open('output/artwork_details/all_artwork_details_dict.json', 'w') as file:
        file.write(json.dumps(all_artworks_details_dict))
    # OUTPUT: JSON dict of dicts, each key is an artwork filename whose value is itself a dict 
    # containing information regarding the concept ids in that artwork, the concept names, 
    # the acno (id) of the artwork, the url of the artwork, the thumbnail copyright, 
    # and the thumbnailUrl 
    return all_artworks_details_dict


def get_just_artwork_tag_ids(artwork):
#Input is an artwork in the form "collection/artworks/a/000/a00001-1035.json"
# Reuses the function (get_concept_ids(d)
# Returns a dictionary with two entries for a single artwork (concept ids in that artwork, 
# the concept names, the acno (id) of the artwork, the url of the artwork, the thumbnail copyright, 
# and the thumbnailUrl)
    d = {}
    artwork_tag_ids = {}
    with open(artwork) as a: 
        data = a.read()
    artwork_dict = json.loads(data)
    for k, v in artwork_dict.items():
        if k == "subjects":
            d = v
        artwork_tag_ids["concept_ids"] = list(get_concept_ids(d))
    artwork_tag_ids["acno"] = artwork_dict["acno"]
    return artwork_tag_ids


def get_all_artworks_tag_ids(artwork_filenames_list): 
# Input is the list, such as ["collection/artworks/a/000/a00001-1035.json", "collection/artworks/a/000/a00002-1036.json", ...] 
# Reuses the function (get_just_artwork_tag_ids(artwork)   
# JSON dict of dicts, each key is an artwork filename whose value is itself a dict containing information regarding the concept ids in that artwork and the acno (id) of the artwork
    all_artworks_tag_ids_dict = {}
    for artwork in artwork_filenames_list:
        all_artworks_tag_ids_dict[artwork] = get_just_artwork_tag_ids(artwork)
    with open('output/artwork_details/all_artwork_tag_ids_dict.json', 'w') as file:
        file.write(json.dumps(all_artworks_tag_ids_dict))
    return all_artworks_tag_ids_dict


artwork_filenames_list = get_all_artwork_filenames_list()
print("length of the final dict is", len(get_all_artworks_details(artwork_filenames_list)))
print("length of the final tag ids dict is", len(get_all_artworks_tag_ids(artwork_filenames_list)))
