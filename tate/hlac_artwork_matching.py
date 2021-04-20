import json


def open_level2_hlac_dict():
    with open('output/hlac_hierarchy/level2_hlac_dict.json') as a: 
        data = a.read()
    level2_hlac_dict = json.loads(data) 
    return level2_hlac_dict


def get_artworks_and_tags():
    with open('output/artwork_details/all_artwork_tag_ids_dict.json') as b: 
        data = b.read()
    all_artwork_tag_ids_dict = json.loads(data) 
    return all_artwork_tag_ids_dict

# more information about each and all of the artworks (apart from tag ids) is found in 'output/artwork_details/all_artwork_details_dict.json'
def get_artworks_details_dict():
    with open('output/artwork_details/all_artwork_details_dict.json') as c: 
        data = c.read()
    all_artwork_details_dict = json.loads(data) 
    return all_artwork_details_dict


def get_hlac_artworks_dict():
    level2_hlac_dict = open_level2_hlac_dict()
    all_artwork_tag_ids_dict = get_artworks_and_tags()
# Returns and saves to an output file a dictionary with hlac_ids as keys and list of artwork_ids as values
    hlac_artworks_dict = {}
    # now I am looping throught the dictionary of 
    for concept_id, concept_name in level2_hlac_dict.items(): #'232': 'freedom'
        hlac_artworks_dict[concept_id] = []
        for key, value in all_artwork_tag_ids_dict.items():
            artwork_tags_list = value["concept_ids"]
            artwork_id = value["acno"]
            for tag in artwork_tags_list:
                if concept_id == str(tag):
                    hlac_artworks_dict[concept_id].append(artwork_id)
    with open('output/hlac_artworks_matches/hlac_artworks_dict.json', 'w') as file:
             file.write(json.dumps(hlac_artworks_dict))
    return hlac_artworks_dict


def get_number_of_matches():
    hlac_artworks_dict = get_hlac_artworks_dict()
    number_of_matches = {}
    for concept, list_of_artworks in hlac_artworks_dict.items():
        number_of_matches[concept] = len(list_of_artworks)
    with open('output/hlac_artworks_matches/number_of_matches.json', 'w') as file:
             file.write(json.dumps(number_of_matches))
    return number_of_matches

def sort_number_of_matches():
    number_of_matches = get_number_of_matches()
    sorted_matches = {k: v for k, v in sorted(number_of_matches.items(), key=lambda item: item[1], reverse=True)}
    with open('output/hlac_artworks_matches/sorted_number_of_matches.json', 'w') as file:
             file.write(json.dumps(sorted_matches))
    return sorted_matches


def get_name_number_matches():
    level2_hlac_dict = open_level2_hlac_dict()
    number_of_matches = get_number_of_matches()
    name_number_matches = {}
    for key in number_of_matches:
        for c_id, c_name in level2_hlac_dict.items():
            if str(c_id) == str(key):
                name_number_matches[str(c_name)] = number_of_matches[key]
    with open('output/hlac_artworks_matches/name_number_matches.json', 'w') as file:
        file.write(json.dumps(name_number_matches))
    return name_number_matches


def sort_name_number_of_matches():
    name_number_of_matches = get_name_number_matches()
    sorted_name_matches = {k: v for k, v in sorted(name_number_of_matches.items(), key=lambda item: item[1], reverse=True)}
    with open('output/hlac_artworks_matches/sorted_name_number_of_matches.json', 'w') as file:
             file.write(json.dumps(sorted_name_matches))
    return sorted_name_matches


def get_match_details(hlac_id):
    hlac_artworks_dict = get_hlac_artworks_dict() 
    # ^ {"232": ["A01061", "A01062", "A01063", "AR0028", ...], "535": [...]}
    all_artwork_details_dict = get_artworks_details_dict()
    # ^ {"collection/artworks/a/000/a00001-1035.json": {"concept_ids": [1, 91, 92, 1050, 272, 694, 95, 195, 1134, 132, 5731, 5734], "concept_names": ["subject", "people", "actions: postures and motions", "arm/arms raised", "kneeling", "sitting", "adults", "man", "man, old", "religion and belief", "universal religious imagery", "blessing"], "acno": "A00001", "url": "http://www.tate.org.uk/art/artworks/blake-a-figure-bowing-before-a-seated-old-man-with-his-arm-outstretched-in-benediction-a00001", "thumbnailCopyright": null, "thumbnailUrl": "http://www.tate.org.uk/art/images/work/A/A00/A00001_8.jpg"}, ... }
    level2_hlac_dict = open_level2_hlac_dict()
    # ^ {'232': 'freedom', '553': 'flirtation', '554': 'morality', '572': 'energy', '647': 'isolation', …}
    hlac_match_details = {}
    for c_id, list_of_artworks in hlac_artworks_dict.items():
        if c_id == str(hlac_id):
            hlac_match_details["hlac name"] = level2_hlac_dict[c_id]
            hlac_match_details["n of artworks tagged with it"] = len(list_of_artworks)
            hlac_match_details["artworks tagged with it"] = list_of_artworks
            hlac_match_details["tagged_artworks_dict"] = {}
            for artwork in list_of_artworks:
                for artwork_path, artwork_details in all_artwork_details_dict.items():
                    if artwork_details["acno"] ==  artwork:
                        hlac_match_details["tagged_artworks_dict"][artwork] = {}
                        hlac_match_details["tagged_artworks_dict"][artwork]["url"] = artwork_details["url"]
                        hlac_match_details["tagged_artworks_dict"][artwork]["thumbnailUrl"] = artwork_details["thumbnailUrl"]
                        hlac_match_details["tagged_artworks_dict"][artwork]["thumbnailCopyright"] = artwork_details["thumbnailCopyright"]
                        hlac_match_details["tagged_artworks_dict"][artwork]["concept_names"] = artwork_details["concept_names"]
                        hlac_match_details["tagged_artworks_dict"][artwork]["concept_ids"] = artwork_details["concept_ids"]                        
    with open("output/hlac_artworks_matches/hlacs_match_details/" + str(hlac_id) + "_hlac_details.json", 'w') as file:
             file.write(json.dumps(hlac_match_details))
    return hlac_match_details


def get_hlac_related_tags(hlac_id):
    match_details = get_match_details(hlac_id)
    hlac_related_tags = {}
    artworks = match_details["tagged_artworks_dict"]
    for artwork, artwork_details in artworks.items():
        subjects = artwork_details["concept_names"] #subjects becomes a list of strings
        for tag in subjects:
            if tag in hlac_related_tags:
                hlac_related_tags[tag] += 1
            else:
                hlac_related_tags[tag] = 1
    sorted_tags = {k: v for k, v in sorted(hlac_related_tags.items(), key=lambda item: item[1], reverse=True)}
    with open("output/hlac_artworks_matches/hlacs_related_tags/" + str(hlac_id) + "_sorted_tags.json", 'w') as file:
         file.write(json.dumps(sorted_tags))
    return sorted_tags

def get_hlac_related_tags_ids(hlac_id):
    match_details = get_match_details(hlac_id)
    hlac_related_tag_ids = {}
    artworks = match_details["tagged_artworks_dict"]
    for artwork, artwork_details in artworks.items():
        subject_ids = artwork_details["concept_ids"] #subjects becomes a list of strings
        for tag_id in subject_ids:
            if tag_id in hlac_related_tag_ids:
                hlac_related_tag_ids[tag_id] += 1
            else:
                hlac_related_tag_ids[tag_id] = 1
    sorted_tag_ids = {k: v for k, v in sorted(hlac_related_tag_ids.items(), key=lambda item: item[1], reverse=True)}
    with open("output/hlac_artworks_matches/hlacs_related_tag_ids/" + str(hlac_id) + "_sorted_tag_ids.json", 'w') as file:
         file.write(json.dumps(sorted_tag_ids))
    return sorted_tag_ids


def get_all_hlacs_tags():
    sorted_matches = sort_number_of_matches()
    hlacs = sorted_matches.keys()
    count = 0
    all_hlacs_tags_dict = {}
    for hlac_id in hlacs:
        all_hlacs_tags_dict[hlac_id] = get_hlac_related_tags(int(hlac_id))
        print(str(hlac_id) + " done!")
        count += 1
        print(count)
    with open("output/hlac_artworks_matches/all_hlacs_tags_dict.json", 'w') as file:
         file.write(json.dumps(all_hlacs_tags_dict))
    print("Done with all " + str(count) + " HLACs! Collected all their related tags and relative frequencies.")
    return all_hlacs_tags_dict

def get_all_hlacs_tag_ids():
    sorted_matches = sort_number_of_matches()
    hlacs = sorted_matches.keys()
    count = 0
    all_hlacs_tag_ids_dict = {}
    for hlac_id in hlacs:
        all_hlacs_tag_ids_dict[hlac_id] = get_hlac_related_tags_ids(int(hlac_id))
        print(str(hlac_id) + " done!")
        count += 1
        print(count)
    with open("output/hlac_artworks_matches/all_hlacs_tag_ids_dict.json", 'w') as file:
         file.write(json.dumps(all_hlacs_tag_ids_dict))
    print("Done with all " + str(count) + " HLACs! Collected all their related tag ids and relative frequencies.")
    return all_hlacs_tag_ids_dict


hola = get_all_hlacs_tag_ids()


