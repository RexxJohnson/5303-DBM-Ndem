import csv, json

csvFilePath = '/Users/emmanuelndem/Desktop/data.csv'
jsonFilePath = '/Users/emmanuelndem/Desktop/data.json'

#read
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows
        

#create json
with open(jsonFilePath, 'w') as jsonFile:

    jsonFile.write(json.dumps(data, indent=4))