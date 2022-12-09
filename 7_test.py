import os
from os.path import abspath, join, dirname
PROJECT_ROOT_PATH = abspath(join(dirname(abspath(__file__)), '..'))

print(os.path.exists(PROJECT_ROOT_PATH + '/analyse'))
print('File is gemaakt  ' + PROJECT_ROOT_PATH + '/analyse')