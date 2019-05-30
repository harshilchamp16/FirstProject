
from __future__ import print_function
import os
import random
import shutil
List=list()
path = 'Face_ID/facenet/dataset/Aligned/'
destination='Face_ID/facenet/dataset/trainingset/'
Destination='Face_ID/facenet/dataset/testingset/'

files = os.listdir(path)
for name in files:
    List.append(name)
print(List)

(random.shuffle(List))

split= int(0.8 * len(List)) 
print(split)

train_filenames = List[:split]
print(train_filenames)


for filename in train_filenames:
    if filename in os.listdir(path):

    	filename1= os.path.join(path,filename)
    	destination1 = os.path.join(destination,filename)
    	#print(filename)
    	#print(destination)
    	shutil.copytree(filename1, destination1)
    else:
        print("file does not exist:",filename)

test_filenames=List[split:]
print(test_filenames)

for filename in test_filenames:
    path1='Face_ID/facenet/dataset/Aligned/'+filename+'/'
    faces=os.listdir(path1)
    #print(faces)
    for face in faces:
        file= os.path.join(path1,face)
        #print(files)
        shutil.copy(file, Destination)




    
        
       
