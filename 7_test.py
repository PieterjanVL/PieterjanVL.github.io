import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d %H_%M_%S")

print(os.path.exists(os.getcwd()))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/' + dt_string)

print(os.path.exists(os.getcwd() + '/analyse/' + dt_string))



f= open(os.getcwd() + '/analyse/' + dt_string + '/ok.txt',"w+")
for i in range(60):
     f.write("This is line %d\r\n" % (i+1))