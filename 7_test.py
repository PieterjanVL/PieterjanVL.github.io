import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")

save_grafiek = os.getcwd()+'/analyse/' + str(dt_string)

print(os.path.exists(os.getcwd()))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/' + dt_string)

print(os.path.exists(os.getcwd() + '/analyse/' + dt_string))

df = pd.read_csv(os.getcwd() + '/data.csv').drop_duplicates()
print(df)

#Datum omzetten:
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%d/%m/%y %H:%M:%S')
print(df)

#Algemene plot maken dat graden en bezetting bekijkt:
eerste_plot = df.pivot_table(index='graden', columns='facilityName', values='bezetting%', aggfunc='mean')
print(eerste_plot)
eerste_plot.plot(title='Invloed temperatuur bezetting fietsenstalling', xlabel='graden celsius', ylabel='bezetting in %')
plt.savefig(save_grafiek+'/grafiek1')

#Algemene plot maken dat datum en bezetting bekijkt:
tweede_plot = df.pivot_table(index='time', columns='facilityName', values='bezetting%', aggfunc='mean')
print(tweede_plot)
tweede_plot.plot(title='Tijdsaanduiding wanneer data is opgenomen en hun bezetting', xlabel='datum', ylabel='bezetting in %')
plt.savefig(save_grafiek+'/grafiek2')

#Mean plot maken dat graden en bezetting bekijkt:
derde_plot = df.pivot_table(index='time',values='bezetting%', aggfunc='mean')
print(derde_plot)
derde_plot.plot(title='Gemiddelde tijdsaanduiding wanneer data is opgenomen en hun bezetting', xlabel='datum', ylabel='bezetting in %', legend='test')
plt.savefig(save_grafiek+'/grafiek3')

#Algemene plot maken dat datum en bezetting bekijkt:
derde_plot = df.pivot_table(index='graden',values='bezetting%', aggfunc='mean')
print(derde_plot)
derde_plot.plot(title='Gemiddelde tijdsaanduiding wanneer data is opgenomen en hun bezetting', xlabel='graden', ylabel='bezetting in %')
plt.savefig(save_grafiek+'/grafiek4')

f= open(os.getcwd() + '/analyse/' + dt_string + '/ok.txt',"w+")
for i in range(60):
     f.write("This is line %d\r\n" % (i+1))
