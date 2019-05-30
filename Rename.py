import os


List = list()
path = 'Facenet/VGG_Female'
files = os.listdir(path)

for folder in files:
	List.append(folder)

for i in List:
	path1 = os.path.join(path, i)
	for face in os.listdir(path1):
		dst = i +'_'+ face
		src = os.path.join(path1, face)
		dst = os.path.join(path1, dst)
		
		os.rename(src, dst)