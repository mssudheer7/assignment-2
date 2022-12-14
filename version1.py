"""importing the required libraries"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def readFile(link): 
  """function for reading csv file"""
  data = pd.read_csv(link)
  years = ['1971','1981','1991','2001','2011'] # Considering 5 different years
  countries = ['Afghanistan','Bangladesh','Brazil','Canada','China','Germany','United Kingdom','India','Italy','Japan'] # Considering 10 different Countries
  for i in range(len(data['Country Name'])):
    if data['Country Name'][i] not in countries:
      data = data.drop([i])
  for i in data:
    if i not in years:
      del data[i]
  countries = pd.DataFrame(countries, columns = ['Country Name'])
  return countries, data # returns 2 data frames - countries and years


def mean_growth(countries,year):
  """calculating the mean and standard deviation"""
  countries = countries['Country Name'].tolist()
  year_mean = list(year_data_frame.mean(axis = 1))
  year_std = list(year_data_frame.std(axis = 1))
  l = [countries,year_mean,year_std]
  df = pd.DataFrame(l).transpose()
  df.columns = ['Country Name','Mean Growth','Standard Deviation']
  tot_mean = df['Mean Growth'].mean()
  tot_std = df['Standard Deviation'].std()
  print("\n\nMean Growth of Urban Population for every country: ")
  display(df)
  print("\nOverall Mean Growth of population : ",tot_mean)
  print("\nOverall Standard Deviation of population : ",tot_std)


def bar_graph(countries,year):
  """drawing the bar graph"""
  print("\n\nBar plot")
  plt.figure(figsize=(20, 8))
  x = np.arange(len(countries['Country Name']))
  w = 0.1
  plt.bar(x,year['1971'],width=w,label=1971)
  x = x+w
  plt.bar(x,year['1981'],width=w,label=1981)
  x = x+w
  plt.bar(x,year['1991'],width=w,label=1991)
  x = x+w
  plt.bar(x,year['2001'],width=w,label=2001)
  x = x+w
  plt.bar(x,year['2011'],width=w,label=2011)
  plt.xticks(x-0.2,countries['Country Name'])
  plt.legend()
  plt.xlabel('Country Name', size='18')
  plt.ylabel('Population Growth',size='18')
  plt.title('URBAN POPULATION GROWTH OVER DECADES',size='24')
  plt.show()
  plt.close()

def correlarion_graph():
  """correlations between indicators"""
  data = pd.read_csv('/content/canada.csv')
  del data['Year']
  cormat = data.corr()
  plt.title("Correlation between few indicators for the country CANADA\n\n")
  display(cormat)
  


link = "/content/urban_population_growth.csv"
countries_data_frame, year_data_frame = readFile(link) # reading csv file

print("\nCountries Data Frame")
display(countries_data_frame)

print("\n\nYears Data Frame\n\n")
display(year_data_frame)

mean_growth(countries_data_frame,year_data_frame)

bar_graph(countries_data_frame,year_data_frame)
print()

correlarion_graph()