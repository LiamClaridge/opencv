import os
import string
import re
import sys

pos_img_file_dir=sys.arv[1]
pos_annotation_file_dir=sys.argv[2]


for filename in os.listdir(pos_img_file_dir):
    count=0
    file=open(pos_annotation_file_dir + os.path.splitext(filename)[0] + ".txt","r")
    for line in file:
        count+=1
        if count == 2:
            line_2=line
            print pos_img_file_dir + filename + ' ' + ' '.join(re.findall(r'\d+', line_2))        