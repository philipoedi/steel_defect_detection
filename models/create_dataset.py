from os import listdir
import re

def create_line(file,out): 
    f = open(file,"r")
    name = file.split(".")[0].split("/")[-1]
    d = {i:0 for i in range(1,7)}
    for line in f:
        d_type = int(line.split()[-1])
        d[d_type] += 1
    out.write("{},{},{},{},{},{},{}\n".format(name,d[1],d[2],d[3],d[4],d[5],d[6]))
    f.close()
    
folders = listdir("data")
folders.remove("trainval.txt")
folders.remove("test.txt")
output = open("defect_count.csv","w+")
r = re.compile(".*not")

for folder in folders:
    sub_folders = listdir("data/{}".format(folder))
    sub_folders = list(filter(r.match,sub_folders))
    for sub_folder in sub_folders:
        files = listdir("data/{}/{}".format(folder,sub_folder))
        for file in files:
            print("Writing data for {}: {}\n".format(sub_folder,file))
            create_line("data/{}/{}/{}".format(folder,sub_folder,file),output)    
    
output.close()