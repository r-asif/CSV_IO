import csv

with open('sample.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Color'] == 'blue':
            print(row['ID'] ,row ['Make'],row ['Color'])