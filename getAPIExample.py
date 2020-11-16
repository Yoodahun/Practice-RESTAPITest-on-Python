import requests
import json
import configparser
from utilities.configurations import *
from utilities.resources import *

get_book_url = getConfig()['API']['endpoint'] + APIResourses.get_book
response = requests.get(get_book_url,
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
        assert expectedBook == res  # assertion also can each object other
        break


#-----------------------
#Github getUser
print("Github getUser")
get_github_user_url = "https://api.github.com/user"
response = requests.get(get_github_user_url, auth=('yoodahun', ''))
print(response.status_code)
print(response.text)