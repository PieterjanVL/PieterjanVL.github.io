import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd

print(os.path.exists(os.getcwd()))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/test6')

print(os.path.exists(os.getcwd() + '/analyse/test6'))
print('File is gemaakt' + os.getcwd() + '/analyse/test4')

f= open(os.getcwd() + '/analyse/ok/ok.txt',"w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))