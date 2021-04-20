
# _________________________________________________________________________________
# THESE FUNCTIONS ARE TO CREATE THE LIST OF INITIAL HLACs FROM THE TATE COLLECTION
# _________________________________________________________________________________

import json

# _________________________________________________________________________________
# create a list from the chosen concepts with the TopConcept "emotions, concepts and ideas"
# _________________________________________________________________________________
nt = open('emo_hlacs.txt').readlines()
emo_hlacs_list = []
for concept in nt:
	concept = concept.strip()
	emo_hlacs_list.append(concept)

print(emo_hlacs_list)
print("Length of emotions, concepts, and ideas concepts list: ", len(emo_hlacs_list))




# _________________________________________________________________________________
# create a list from the chosen concepts with the TopConcept "society"
# _________________________________________________________________________________
nt = open('soc_hlacs.txt').readlines()
soc_hlacs_list = []
for concept in nt:
	concept = concept.strip()
	soc_hlacs_list.append(concept)

print(soc_hlacs_list)
print("Length of society concepts list: ", len(soc_hlacs_list))




# _________________________________________________________________________________
# create a list from the chosen concepts with the TopConcept "religion"
# _________________________________________________________________________________
nt = open('rel_hlacs.txt').readlines()
rel_hlacs_list = []
for concept in nt:
	concept = concept.strip()
	rel_hlacs_list.append(concept)

print(rel_hlacs_list)
print("Length of religion and belief concepts list: ", len(rel_hlacs_list))



# _________________________________________________________________________________
# create a list with all chosen HLACs
# _________________________________________________________________________________
all_hlacs_list = []
all_hlacs_list.extend(emo_hlacs_list)
all_hlacs_list.extend(soc_hlacs_list)
all_hlacs_list.extend(rel_hlacs_list)
print(all_hlacs_list)
print("Length of all HLAC concepts list: ", len(all_hlacs_list))
with open('all_hlacs_list.json', 'w') as file:
	file.write(json.dumps(all_hlacs_list))

