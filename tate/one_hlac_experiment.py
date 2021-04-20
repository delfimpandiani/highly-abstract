import json
import json
from cleaninput import create_newdict, get_topConcepts, get_parent_rels

def get_newdict():
    with open('newdict.json') as a: 
        data = a.read()
    newdict = json.loads(data) 
    return newdict

def get_match_details(hlac_id):
    with open("output/hlac_artworks_matches/hlacs_match_details/" + str(hlac_id) + "_hlac_details.json") as a: 
        data = a.read()
    match_details = json.loads(data) 
    return match_details

def get_related_tags(hlac_id):
    with open("output/hlac_artworks_matches/hlacs_related_tags/" + str(hlac_id) + "_sorted_tags.json") as a: 
        data = a.read()
    related_tags = json.loads(data) 
    return related_tags # {"society": 41, "subject": 40, "social comment": 40, "freedom": 40, "people": 28, ...}

def get_related_tag_ids(hlac_id):
    with open("output/hlac_artworks_matches/hlacs_related_tag_ids/" + str(hlac_id) + "_sorted_tag_ids.json") as a: 
        data = a.read()
    related_tag_ids = json.loads(data) 
    return related_tag_ids # {1: 40, 145: 40, 158: 40, 232: 40, 91: 28, 95: 25, ...}

def get_objects_and_actions_dict(hlac_id):
    # this function goes through all tags for an hlac and determines whether they are objects or actions, or neither
    related_tag_ids = get_related_tag_ids(hlac_id)
    topConcepts = get_topConcepts() # {"4":"group/movement","13":"architecture", ...}
    newdict = create_newdict()
    level1list, level2list = get_parent_rels()
    # level1list [{"id":5731,"name":"universal religious imagery","parent0":132,"parent1":"none"}, ...]
    # level2list [{"id":5734,"name":"blessing","parent0":132,"parent1":5731}, ...]
    
    only_objects_dict = {} # will include objects, people, nature (animals, plants and flowers, trees, water, astronomy, seascapes and coasts)
    not_objects_dict = {}
    actions_dict = {}
    
    for tag_id, freq in related_tag_ids.items(): # 1, 40
        if str(tag_id) in topConcepts: # if "1" in the keys of {"4":"group/movement","13":"architecture", ...}
            print("this tag is a topconcept")
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
                            # ^ if parent is actions:postures and motions, or actions:processes and functions, or actions:expresive
                            actions_dict[str(tag_id)] = freq 
                        elif str(concept_dict['parent1']) == "94" or str(concept_dict['parent1']) == "95" or str(concept_dict['parent1']) == "98":
                            # ^ if parent is children, adults, or nude
                            only_objects_dict[str(tag_id)] = freq
                    if str(concept_dict['parent0']) == "60": # if super parent is nature 
                        if str(concept_dict['parent1']) == "61":
                            # ^ if parent is anoinmals:actions
                            actions_dict[str(tag_id)] = freq
                        else:
                            only_objects_dict[str(tag_id)] = freq
                    else:
                        not_objects_dict[str(tag_id)] = freq
    with open("one_hlac_experiment/" + str(hlac_id) + "_only_objects_dict.json", 'w') as file:
             file.write(json.dumps(only_objects_dict))
    with open("one_hlac_experiment/" + str(hlac_id) + "_actions_dict.json", 'w') as file:
             file.write(json.dumps(actions_dict))
    print("number of tags for this hlac: " + str(len(related_tag_ids)))
    print("number of tags for this hlac that are objects: " + str(len(only_objects_dict)))
    print("number of tags for this hlac that are actions: " + str(len(actions_dict)))
    print("number of tags for this hlac that are not objects: " + str(len(not_objects_dict)))

    return only_objects_dict, actions_dict

def get_names_objects_and_actions_dict(hlac_id):
    newdict = get_newdict()
    # {"4": "group/movement", "13": "architecture", ...}
    only_objects_dict, actions_dict = get_objects_and_actions_dict(hlac_id)
    # only_objects_dict {'174': 68, '1286': 67, '90': 7, '86': 6, '88': 5, ...}
    # actions_dict {'565': 2, '4876': 2, '1503': 1, '544': 1, ...}
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
    with open("one_hlac_experiment/" + str(hlac_id) + "_objects_names.json", 'w') as file:
             file.write(json.dumps(objects_names))
    with open("one_hlac_experiment/" + str(hlac_id) + "_actions_names.json", 'w') as file:
             file.write(json.dumps(actions_names))
    return objects_names, actions_names




hola = get_names_objects_and_actions_dict(795)
print(hola)
