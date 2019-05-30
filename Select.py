import os
import random
import shutil
import numpy as np
List=list()
List1=list()

path = 'Face_ID/facenet/dataset/trainingset/'
destination='Face_ID/facenet/dataset/trainingset1/'

files = os.listdir(path)
for name in files:
    List.append(name)
#print(List)


for i in List:
	#print(i)
	filepath='Face_ID/facenet/dataset/trainingset/' + i +'/'
	#print(filepath)
	faces=os.listdir(filepath)
	
	np.random.shuffle(faces)
	two_faces = faces[:2]
	training_faces= faces[2:]

	for face in two_faces:
		shutil.move(filepath + str(face), destination)
	
























