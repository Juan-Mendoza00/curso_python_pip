import csv


#define a function to read the csv file and to transform it into a list of dictionaries so we can acces to the items. Using zip() method to build key:value pairs with headers:rows, iterating with next() because a file is an iterable
def read_csv(path):
  with open(path, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    headers = next(reader)
    data = []
    for row in reader:
      iterable = zip(headers, row)
      country_dict = {head: data for (head, data) in iterable}
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(data)
