from utilities.configurations import *

def addBookPayLoad(isbn, aisle):
    payload = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }

    return payload


def buildPayLoadFromDB(query):
    addBody = {}

    result_data = getQuery(query)
    addBody['name'] = result_data[0]
    addBody['isbn'] = result_data[1]
    addBody['aisle'] = result_data[2]
    addBody['author'] = result_data[3]

    return addBody