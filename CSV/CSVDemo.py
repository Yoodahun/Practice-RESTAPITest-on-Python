import csv

# Open the file
with open('/Users/yoodahun/Documents/Github/Python/RestAPI-Testing-on-Python/utilities/practiceCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # print(csv_reader)
    # print(dict(csv_reader))

    name = []
    status = []

    for row in list(csv_reader):
        name.append(row[0])
        status.append(row[1])

print(name)
print(status)