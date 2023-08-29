import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')

  country = input('Type country name: ')
  
  country_dict = utils.get_country(country, data)
  country_ft = utils.get_feature(country_dict, 'population')


  if len(country_ft) > 0:
    charts.bar_chart(country_ft.keys(),country_ft.values(),country_dict['Country/Territory'])

#to run main as a script (when called in terminal)
if __name__ == '__main__':
  run()