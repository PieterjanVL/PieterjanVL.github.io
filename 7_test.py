import os

from os.path import abspath, join, dirname
PROJECT_ROOT_PATH = abspath(join(dirname(abspath(__file__)), '..'))
print(PROJECT_ROOT_PATH)
parent_dir = os.getcwd() + '/analyse'

directory = 'test'

path = os.path.join(parent_dir, directory) 
print(parent_dir)

print('ik maak file')
os.mkdir(path) 
print('File is gemaakt')