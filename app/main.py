import utils
import read_csv
import charts
import pandas as pd

def run():
  # data = read_csv.read_csv('./data.csv')
  data  = pd.read_csv('./data.csv')

  country = input('Type country name: ')

  '''
  country_dict = utils.get_country(country, data)
  country_ft = utils.get_feature(country_dict, 'population')

  '''

  # To get a row whith pandas and specified country name
  country_row = data.loc[lambda df: df['Country/Territory'] == country.title()]
  population = country_row[[ft for ft in country_row.columns if ft.endswith('Population')]]

  if len(population) > 0:
    labels = population.columns.values
    ppl = [float(value) for value in population.values[0]]
    charts.bar_chart(labels,ppl,country_row['Country/Territory'].values[0])

#to run main as a script (when called in terminal)
if __name__ == '__main__':
  run()