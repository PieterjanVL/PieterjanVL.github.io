import os

parent_dir = os.getcwd() + '/analyse'

directory = 'test'

path = os.path.join(parent_dir, directory) 
print(parent_dir)

print('ik maak file')
os.mkdir(path) 
print('File is gemaakt')