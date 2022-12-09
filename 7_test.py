import os

print(os.path.exists(os.getcwd()))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/test')

print(os.path.exists(os.getcwd() + '/analyse/test'))
print('File is gemaakt' + os.getcwd() + '/analyse/test')