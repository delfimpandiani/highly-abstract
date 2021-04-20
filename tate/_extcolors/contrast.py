import cv2
import numpy as np


# the following algorithm is based on this: https://stackoverflow.com/questions/57256159/how-extract-contrast-level-of-a-photo-opencv
def get_avg_contrast(image_path):
    # read image
    img = cv2.imread(image_path)

    # convert to LAB color space
    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

    # separate channels
    L,A,B=cv2.split(lab)

    # compute minimum and maximum in 5x5 region using erode and dilate
    kernel = np.ones((5,5),np.uint8)
    min = cv2.erode(L,kernel,iterations = 1)
    max = cv2.dilate(L,kernel,iterations = 1)

    # convert min and max to floats
    min = min.astype(np.float64) 
    max = max.astype(np.float64) 

    # compute local contrast
    contrast = (max-min)/(max+min)

    # get average across whole image
    average_contrast = 100*np.mean(contrast)
    print(image_path + " has an average contrast of " + str(average_contrast)+"%")
    return average_contrast


hor_paths = ['795/T12473_9.jpg', '795/N00793_8.jpg', '795/T08438_8.jpg-palette.png', '795/N01609_9.jpg-palette.png', '795/T07709_8.jpg-palette.png', '795/N01609_9.jpg', '795/T15021_8.jpg-palette.png', '795/T00733_8.jpg-palette.png', '795/T12711_9.jpg', '795/N00793_8.jpg-palette.png', '795/N06005_8.jpg', '795/AR00085_8.jpg', '795/T14116_8.jpg-palette.png', '795/AR00085_8.jpg-palette.png', '795/T03975_9.jpg-palette.png', '795/T07707_8.jpg', '795/T15021_8.jpg', '795/N03357_9.jpg', '795/T12478_9.jpg-palette.png', '795/T07193_9.jpg', '795/N06183_9.jpg', '795/N06183_9.jpg-palette.png', '795/N03361_8.jpg-palette.png', '795/N01110_8.jpg-palette.png', '795/N01046_8.jpg', '795/T04141_9.jpg', '795/N01913_8.jpg-palette.png', '795/N01046_8.jpg-palette.png', '795/T00556_8.jpg-palette.png', '795/T05858_8.jpg', '795/A500503.png-palette.png', '795/N03357_9.jpg-palette.png', '795/T07193_9.jpg-palette.png', '795/N05774_8.jpg-palette.png', '795/T12478_9.jpg', '795/N01110_8.jpg', '795/T05870_8.jpg', '795/N01834_9.jpg-palette.png', '795/T13310_8.jpg', '795/T12373_9.jpg', '795/N01834_9.jpg', '795/N05736_8.jpg-palette.png', '795/N05774_8.jpg', '795/T00556_8.jpg', '795/T08442_8.jpg', '795/N06171_8.jpg-palette.png', '795/T14116_8.jpg', '795/T08438_8.jpg', '795/T07707_8.jpg-palette.png', '795/T03975_9.jpg', '795/N05061_8.jpg-palette.png', '795/T05870_8.jpg-palette.png', '795/T05858_8.jpg-palette.png', '795/A500503.png', '795/N03361_8.jpg', '795/T06961_9.jpg', '795/T04141_9.jpg-palette.png', '795/T12373_9.jpg-palette.png', '795/T00733_8.jpg', '795/T12711_9.jpg-palette.png', '795/T13272_8.jpg-palette.png', '795/T07709_8.jpg', '795/T06961_9.jpg-palette.png', '795/N06171_8.jpg', '795/T13310_8.jpg-palette.png', '795/N05736_8.jpg', '795/N01913_8.jpg', '795/T08441_9.jpg', '795/N05061_8.jpg', '795/T12473_9.jpg-palette.png', '795/T13272_8.jpg']
new_hor_paths = []
for path in hor_paths:
    if "palette" not in path:
        new_hor_paths.append(path)
print(new_hor_paths)




cons_paths = ['4063/P07241_9.jpg-palette.png', '4063/AR00729_9.jpg-palette.png', '4063/T13780_9.jpg-palette.png', '4063/P07044_9.jpg-palette.png', '4063/T00855_9.jpg', '4063/P80117_9.jpg', '4063/P11974_9.jpg-palette.png', '4063/T07212_9.jpg-palette.png', '4063/P80101_9.jpg-palette.png', '4063/P11358_9.jpg', '4063/T13772_9.jpg', '4063/L02962_9.jpg-palette.png', '4063/P02034_9.jpg', '4063/T06935_9.jpg', '4063/T03093.png', '4063/P07241_9.jpg', '4063/T12301_9.jpg-palette.png', '4063/T01459_9.jpg', '4063/T00855_9.jpg-palette.png', '4063/T13769_9.jpg', '4063/AR00729_9.jpg', '4063/T12837_9.jpg-palette.png', '4063/P80104_9.jpg-palette.png', '4063/T01460_9.jpg-palette.png', '4063/P07044_9.jpg', '4063/T01199_9.jpg-palette.png', '4063/P78371_9.jpg', '4063/P80111_9.jpg', '4063/P04253_9.jpg', '4063/P02053_9.jpg', '4063/T07210_9.jpg', '4063/AR00078_9.jpg', '4063/T13779_9.jpg-palette.png', '4063/P11975_9.jpg-palette.png', '4063/T01460_9.jpg', '4063/T13765_9.jpg-palette.png', '4063/P80100_9.jpg-palette.png', '4063/P02032_9.jpg', '4063/P80108_9.jpg', '4063/T13774_9.jpg', '4063/T07209_9.jpg', '4063/P02045_9.jpg-palette.png', '4063/T03093.png-palette.png', '4063/P02030_9.jpg', '4063/T01462_9.jpg', '4063/P80119_9.jpg-palette.png', '4063/T06991_9.jpg-palette.png', '4063/T07212_9.jpg', '4063/T07766_9.jpg', '4063/P80105_9.jpg-palette.png', '4063/P77924_9.jpg', '4063/P02029_9.jpg', '4063/T13408_9.jpg', '4063/T13771_9.jpg', '4063/T03973_9.jpg-palette.png', '4063/T13766_9.jpg-palette.png', '4063/P80103_9.jpg-palette.png', '4063/T07210_9.jpg-palette.png', '4063/L03203_9.jpg-palette.png', '4063/P79798_9.jpg', '4063/T13768_9.jpg', '4063/T12301_9.jpg', '4063/P80116_9.jpg', '4063/P04253_9.jpg-palette.png', '4063/P80098_9.jpg-palette.png', '4063/T07209_9.jpg-palette.png', '4063/T06934_9.jpg', '4063/P80106_9.jpg-palette.png', '4063/P11973_9.jpg-palette.png', '4063/T13773_9.jpg', '4063/AR00078_9.jpg-palette.png', '4063/T01462_9.jpg-palette.png', '4063/T07667_9.jpg', '4063/P02031_9.jpg', '4063/T01463_9.jpg', '4063/T12941_9.jpg', '4063/P13173_9.jpg', '4063/T13767_9.jpg-palette.png', '4063/T07211_9.jpg-palette.png', '4063/T06991_9.jpg', '4063/P02047_9.jpg-palette.png', '4063/L02961_9.jpg-palette.png', '4063/AR00079_9.jpg', '4063/P11358_9.jpg-palette.png', '4063/T07211_9.jpg', '4063/P80099_9.jpg-palette.png', '4063/P79798_9.jpg-palette.png', '4063/T07208_9.jpg-palette.png', '4063/P77927_9.jpg', '4063/P80110_9.jpg', '4063/T07208_9.jpg', '4063/P80107_9.jpg-palette.png', '4063/T01190_9.jpg', '4063/P11972_9.jpg-palette.png', '4063/P80109_9.jpg', '4063/T01463_9.jpg-palette.png', '4063/AR00079_9.jpg-palette.png', '4063/T13775_9.jpg', '4063/T07766_9.jpg-palette.png', '4063/T13779_9.jpg', '4063/P02031_9.jpg-palette.png', '4063/AL00331_9.jpg', '4063/P80105_9.jpg', '4063/P11974_9.jpg', '4063/T06904_9.jpg-palette.png', '4063/P07937_9.jpg', '4063/P02047_9.jpg', '4063/T13408_9.jpg-palette.png', '4063/T08400_9.jpg-palette.png', '4063/AL00330_9.jpg-palette.png', '4063/T03354_9.jpg-palette.png', '4063/L02962_9.jpg', '4063/AR00077_9.jpg', '4063/T06532_9.jpg', '4063/T03354_9.jpg', '4063/T13772_9.jpg-palette.png', '4063/P02034_9.jpg-palette.png', '4063/P80117_9.jpg-palette.png', '4063/T07906_9.jpg-palette.png', '4063/AL00329_9.jpg-palette.png', '4063/T03973_9.jpg', '4063/P02045_9.jpg', '4063/T06935_9.jpg-palette.png', '4063/AL00335_9.jpg-palette.png', '4063/AL00333_9.jpg', '4063/P80107_9.jpg', '4063/P02030_9.jpg-palette.png', '4063/P11972_9.jpg', '4063/P80103_9.jpg', '4063/AL00331_9.jpg-palette.png', '4063/P07937_9.jpg-palette.png', '4063/T07667_9.jpg-palette.png', '4063/T13766_9.jpg', '4063/P13173_9.jpg-palette.png', '4063/P77927_9.jpg-palette.png', '4063/P80116_9.jpg-palette.png', '4063/T13773_9.jpg-palette.png', '4063/T05217_9.jpg-palette.png', '4063/P02053_9.jpg-palette.png', '4063/T12837_9.jpg', '4063/P80125_9.jpg', '4063/T06934_9.jpg-palette.png', '4063/P79771_9.jpg-palette.png', '4063/AL00335_9.jpg', '4063/P80101_9.jpg', '4063/AL00334_9.jpg-palette.png', '4063/T13780_9.jpg', '4063/T06532_9.jpg-palette.png', '4063/P02029_9.jpg-palette.png', '4063/P80099_9.jpg', '4063/T13775_9.jpg-palette.png', '4063/P80110_9.jpg-palette.png', '4063/P78371_9.jpg-palette.png', '4063/L02961_9.jpg', '4063/AL00332_9.jpg-palette.png', '4063/P80124_9.jpg-palette.png', '4063/AL00332_9.jpg', '4063/P80106_9.jpg', '4063/T13769_9.jpg-palette.png', '4063/P77924_9.jpg-palette.png', '4063/T01459_9.jpg-palette.png', '4063/T08400_9.jpg', '4063/P11975_9.jpg', '4063/AL00330_9.jpg', '4063/P80104_9.jpg', '4063/AR00077_9.jpg-palette.png', '4063/P80109_9.jpg-palette.png', '4063/AL00329_9.jpg', '4063/P02032_9.jpg-palette.png', '4063/P80111_9.jpg-palette.png', '4063/T13774_9.jpg-palette.png', '4063/P80124_9.jpg', '4063/T05217_9.jpg', '4063/P80119_9.jpg', '4063/T13765_9.jpg', '4063/P80125_9.jpg-palette.png', '4063/AL00333_9.jpg-palette.png', '4063/P80098_9.jpg', '4063/T07906_9.jpg', '4063/P79771_9.jpg', '4063/T01199_9.jpg', '4063/T01190_9.jpg-palette.png', '4063/AL00334_9.jpg', '4063/P80100_9.jpg', '4063/T13768_9.jpg-palette.png', '4063/T13771_9.jpg-palette.png', '4063/P11973_9.jpg', '4063/L03203_9.jpg', '4063/T06904_9.jpg', '4063/T13767_9.jpg', '4063/P80108_9.jpg-palette.png', '4063/T12941_9.jpg-palette.png']
new_cons_paths = []
for path in cons_paths:
    if "palette" not in path:
        new_cons_paths.append(path)
print(new_cons_paths)




def get_avg_hlac_contrast(hlac, paths):
    n = 0
    count = 0
    for image_path in paths:
        c = get_avg_contrast(image_path).tolist()
        if np.isnan(c) == False:
            x = float(c)
            n += 1
            count = count + x
    total = count/n
    print(str(hlac) + " HAS AN AVG CONTRAST OF " + str(total))
    return

get_avg_hlac_contrast("horror", new_hor_paths) #horror HAS AN AVG CONTRAST OF 17.303676338171474
get_avg_hlac_contrast("consumerism", new_cons_paths) # consumerism HAS AN AVG CONTRAST OF 13.348331188252795

# I COULD also check the relative luminance of the top 5 colors...
# with this tool here: https://planetcalc.com/7779/

