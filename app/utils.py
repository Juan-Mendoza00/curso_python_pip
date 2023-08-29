def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def popl_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

# -----------------------------------------------
# Functions remade for a broader usability
# -----------------------------------------------

# Returns a row from dataset specified. Brings out the information of the country specified.
def get_country(name, data):
  name = name.title()
  country_dict = list(filter(lambda country: country['Country/Territory'] == name, data))
  return country_dict[0]

# Also returns a dict from the specific country with the input feature. Has to be well spelled
def get_feature(country, feature): 
  feature = feature.title()
  n = {key: (float(value) if value.isnumeric() else value) for (key, value) in country.items() if (key.endswith(feature))}
  return n

def get_column(data, value):
  value = value.title()
  column = {item['Country/Territory']: item[value] for item in data}
  return column