import requests
import json
import configparser

config = configparser.ConfigParser().read('utilities/properties.ini')
response = requests.get(config['API']['endpoint'] + "/Library/GetBook.php",
                        params={
                            'AuthorName': 'Rahul Shetty'
                        },
                        )

print(response.text)
print(type(response.text))

response_string = response.text
response_json = response.json()

print(response_json)
print(type(response_json))

assert response.status_code == 200
print(response.headers['Content-Type'])
print(type(response.headers))

## Retrieve the book details with ISBN RGHCC

expectedBook = {'book_name': 'Learn API Automation with RestAssured', 'isbn': 'RGHCC', 'aisle': '12239'}

for res in response_json:
    if res["isbn"] == "RGHCC":
        assert expectedBook == res #assertion also can each object other
        break

