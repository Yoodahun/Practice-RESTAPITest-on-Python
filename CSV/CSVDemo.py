import csv

# Open the file and read
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

name_sam_index = name.index('sam')
print(status[name_sam_index])

# Open the file write
with open('/Users/yoodahun/Documents/Github/Python/RestAPI-Testing-on-Python/utilities/practiceCSV.csv', 'a') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(["Bob", "rejected"])