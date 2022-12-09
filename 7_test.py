import os

print(os.path.exists(os.getcwd()))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse'))
print('File is gemaakt' + os.getcwd() + '/analyse')
