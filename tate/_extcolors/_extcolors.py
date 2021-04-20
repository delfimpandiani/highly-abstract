import os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
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

# # get the palettes of the energy images, saved in the specific medium folders
# energy_by_folder = getListOfFiles("572_energy_61")
# for filename in energy_by_folder:
#     print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")


# # get the palettes of the energy images, all together
all_energy = getListOfFiles("572")
# for filename in all_energy:
#     print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")


# # get the palettes of the consumerism images, saved in the specific medium folders
# cons_by_folder = getListOfFiles("4063_consumerism_96")
# for filename in cons_by_folder:
#     print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")


# # get the palettes of the energy images, all together
all_cons = getListOfFiles("4063")
# for filename in all_cons:
#     print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")

# # get the palettes of the horror images, saved in the specific medium folders
# horr_by_folder = getListOfFiles("795_horror_37")
# for filename in horr_by_folder:
#     print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")


# get the palettes of the energy images, all together
all_horr = getListOfFiles("795")
# for filename in all_horr:
#     print("! extcolors " + str(filename) + " -l5 --image " + str(filename) + "-palette")

# print(all_horr)
print(all_cons)
# print(all_energy)



