import csv
 
with open('udemy_python_mid_advanced_mobilo/Section9-Iterators/data1.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break
print('All data was processed')