import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd

df = pd.read_csv(os.getcwd() + '/data.csv').drop_duplicates()
print(df)

#Datum omzetten:
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%d/%m/%y %H:%M:%S')
print(df)

#Algemene plot maken dat graden en bezetting bekijkt:
eerste_plot = df.pivot_table(index='graden', columns='facilityName', values='bezetting%', aggfunc='mean')
print(eerste_plot)
eerste_plot.plot(title='Invloed temperatuur bezetting fietsenstalling', xlabel='graden celsius', ylabel='bezetting in %')
plt.savefig(os.getcwd()+'/grafiek1')


print(os.path.exists(os.getcwd() + '/grafiek1'))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/test')

print(os.path.exists(os.getcwd() + '/analyse/test'))
print('File is gemaakt' + os.getcwd() + '/analyse/test')