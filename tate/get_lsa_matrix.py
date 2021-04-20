
import json
import nltk


def open_all_hlacs_tags_dict():
    with open('output/hlac_artworks_matches/all_hlacs_tags_dict.json') as a: 
        data = a.read()
    all_hlacs_tags_dict = json.loads(data) 
    return all_hlacs_tags_dict


def get_list_of_terms(): 
    # outputs a list of 5810 unique terms (related tags to the 166 HLACs)
    list_of_terms = []
    all_hlacs_tags_dict = open_all_hlacs_tags_dict()
    for k, v in all_hlacs_tags_dict.items():
        for concept_key in v:
            if concept_key not in list_of_terms:
                list_of_terms.append(concept_key)
    print("length of list (n of unique concepts) is: ", len(list_of_terms))
    print ("first five terms are: ", list_of_terms[:5])
    # check if the list has duplicates:
    contains_duplicates = any(list_of_terms.count(element) > 1 for element in list_of_terms)
    print("Does the list have duplicates?", contains_duplicates)
    with open('output/list_of_terms.json', 'w') as file:
             file.write(json.dumps(list_of_terms))
    return list_of_terms

def get_len_list_of_terms():
    list_of_terms = get_list_of_terms()
    return len(list_of_terms)

def get_hlac_bag_of_words(hlac_id):
    all_hlacs_tags_dict = open_all_hlacs_tags_dict()
    bag_of_words = []
    for hlac_idd, tag_dict in all_hlacs_tags_dict.items():
        if hlac_idd == str(hlac_id):
            for tag in tag_dict:
                bag_of_words.append(tag)
    with open("output/hlacs_bags_of_words/" + str(hlac_id) + "_bag_of_words.json", 'w') as file:
        file.write(json.dumps(bag_of_words))
    print("length of the bag of words for the concept ", hlac_id, " is ", len(bag_of_words))
    return bag_of_words


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def get_binary_values(hlac_id): 
    # outputs a list of 5810 values (each a 0 or a 1) to say whether or not each tag is related to the hlac of interest
    len_of_values_list = get_len_list_of_terms() #first check how long the output list should be
    binary_values_list = zerolistmaker(len_of_values_list) # then create a list of that length full of zeroes (starting assumption is that the HLAC is NOT related to any of the tags)
    # print(len(binary_values_list)) # to check that the list is the same length of the list_of_terms
    
    bag_of_words = get_hlac_bag_of_words(hlac_id)
    list_of_terms = get_list_of_terms()
    count = 0


    for term in list_of_terms:
        if term in bag_of_words:
            index = list_of_terms.index(term)
            binary_values_list[index] = 1
            count += 1
    with open("output/hlacs_binary_values/" + str(hlac_id) + "_binary_values.json", 'w') as file:
        file.write(json.dumps(binary_values_list))
    print("number of 1s added to the bag of words of concept ", hlac_id, " is ", count)
    return binary_values_list



def create_matrix_list(a, b, c, d, e, f):
    matrix_list = []
    for index in range(5810):
        matrix_list.append(a[index])
        matrix_list.append(b[index])
        matrix_list.append(c[index])
        matrix_list.append(d[index])
        matrix_list.append(e[index])
        matrix_list.append(f[index])
    print("length of this matrix should be 34,860, and it is ", len(matrix_list))
    with open("output/hlacs_binary_values/attempta_t_matrix.json", 'w') as file:
        file.write(json.dumps(matrix_list))
    return matrix_list



def get_this_example_total_list():
    a = (get_hlac_bag_of_words(232)) #freedom
    b = (get_hlac_bag_of_words(940)) #happiness
    c = (get_hlac_bag_of_words(6709)) #triumph
    d = (get_hlac_bag_of_words(3991)) #slavery
    e = (get_hlac_bag_of_words(647)) #isolation
    f = (get_hlac_bag_of_words(6921)) #enclosure

    ex_list_of_terms = list(set().union(a, b, c, d))
    return ex_list_of_terms


ex_list_of_terms = get_this_example_total_list()
print(len(ex_list_of_terms))
# a = (get_binary_values(232)) #freedom
# b = (get_binary_values(940)) #happiness
# c = (get_binary_values(6709)) #triumph
# d = (get_binary_values(3991)) #slavery
# e = (get_binary_values(647)) #isolation
# f = (get_binary_values(6921)) #enclosure




# create_matrix_list(a, b, c, d, e, f)



# def clean_up_list_of_terms():
#     list_of_terms = get_list_of_terms()
#     # stemming of words
#     from nltk.stem.porter import PorterStemmer
#     porter = PorterStemmer()
#     stemmed = [porter.stem(word) for word in list_of_terms]
#     print(stemmed[:100])
#     print("the length of the original list of terms is ",len(list_of_terms))
#     print("the length of the stemmed list is ", len(stemmed))

#     contains_duplicates = any(stemmed.count(element) > 1 for element in stemmed)
#     print("Does the stemmed list have duplicates? ", contains_duplicates)

#     stemm_unique_list = list(dict.fromkeys(stemmed))
#     print("the length of the stemmed, cleaned list is ", len(stemm_unique_list))

#     check = any(stemm_unique_list.count(element) > 1 for element in stemm_unique_list)
#     print("Does the stemmed, cleaned list have duplicates?", check)
#     return stemm_unique_list # 5745 instead of 5810 terms... not good enough