import numpy as np
import cv2
from os import listdir

def model():
    return None

def load_data(path,full_dataset = True):
    folders = listdir("data")
    folders.remove("trainval.txt")
    folders.remove("test.txt")
    data = np.zeros((3001,96,96))
    metadata = np.zeros((3001,6))
    metadata_dict = dict()
    id_2_index = dict()
    index_2_id = dict()
    for f in open("defect_count.csv","r"):
        line = f.split(",",1)
        metadata_dict[line[0]] = line[1][:-1].split(",")
    i = 0
    for folder in folders:
        sub_folders = listdir("data/{}".format(folder))
        sub_folders = list(filter(lambda x: "not" not in x,sub_folders))
        for sub_folder in sub_folders:
            files = listdir("data/{}/{}".format(folder,sub_folder))
            for file in files:
                img = cv2.imread("data/{}/{}/{}".format(folder,sub_folder,file),0)
                img = cv2.resize(img,(96,96))
                data[i] = img
                test_temp = file.split("_")
                if "temp" in test_temp[-1]:
                    metadata[i] = [0,0,0,0,0,0]
                else:
                    metadata[i] = metadata_dict[test_temp[0]]                    
                id_2_index[i] = test_temp[0]
                index_2_id[test_temp[0]] = i
                i += 1
    data = data/255.
    data = data.reshape((3001,96,96,1))
    return data,metadata,index_2_id,id_2_index
                
                
                
       #         create_line("data/{}/{}/{}".format(folder,sub_folder,file),output) 

    
#    img = cv2.imread(path,0)
#    img = cv2.resize(img,(96,96))
#    data[0] = img
#    print(data[0])
#    print(data[0].shape)

#https://www.tensorflow.org/tutorials/load_data/images
def get_label():
    return None
    
data,metadata,index_2_id,id_2_index = load_data("00041000_temp.jpg")
