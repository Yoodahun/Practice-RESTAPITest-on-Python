import json


courses = '{"name" : "TestTest","languages": ["java","python"]}'

#Loads method parse json string and it returns dictionary.

jsonDictionary = json.loads(courses)
print(type(jsonDictionary))
print(jsonDictionary["languages"][1])

###########
#parse content in json file into dictionary

with open("exampleJson.json") as reader:
    jsonFile_Dictionary = json.load(reader)
    print(type(jsonFile_Dictionary))
    print(jsonFile_Dictionary)

print(jsonFile_Dictionary['courses'][0]['title'])

##price of course 'RPA'
print(jsonFile_Dictionary['courses'][2]['price'])

for course in jsonFile_Dictionary['courses']:
    print(course)

    if course['title'] == "RPA":
        print(course['title'])
        assert course['price'] == 45

