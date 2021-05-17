import json


def opentoclean():
    with open('TOCLEAN.json') as a: 
        data = a.read()
    toclean_dict = json.loads(data) 
    return toclean_dict

def open_level2_hlac_dict():
    with open('output/hlac_hierarchy/level2_hlac_dict.json') as a: 
        data = a.read()
    level2_hlac_dict = json.loads(data) 
    return level2_hlac_dict


def get_hlac_names():
    toclean_dict = opentoclean()
    hlacs_results_n = {}
    d = {}
    for k, v in toclean_dict.items():
        if k == "subject_term":
            hlacs_results_n['subject_term'] = v # "Subject term: 232" = {}
        if k == "n_results":
            hlacs_results_n["n of results"] = v
        if k == "links":
            
    return hlacs_results_n




# def get_results_n(hlac):
#     toclean_dict = opentoclean()
#     level2_hlac_dict = open_level2_hlac_dict()
#     hlacs_results_n = {}
#     d = {}

#     for hlac_id, hlac_name in level2_hlac_dict.items():
#         for k, v in toclean_dict.items():
#             if k == "subject_term":
#                 hlacs_results_n[v] = {} # "Subject term: 232" = {}
#                 d = v
#                 hlacs_results_n[v]["n of results"] = 
#             hlacs_results_n[hlac_id] = 


toclean_dict = opentoclean()
print(len(toclean_dict))
print(toclean_dict.keys())
print(get_hlac_names())




# def get_just_artwork_tag_ids(artwork):
#     d = {}
#     artwork_tag_ids = {}
#     with open(artwork) as a: 
#         data = a.read()
#     artwork_dict = json.loads(data)
#     for k, v in artwork_dict.items():
#         if k == "subjects":
#             d = v
#         artwork_tag_ids["concept_ids"] = list(get_concept_ids(d))
#     artwork_tag_ids["acno"] = artwork_dict["acno"]
#     return artwork_tag_ids
