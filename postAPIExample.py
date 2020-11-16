import requests
import json
from payLoad import *


## Add
response = requests.post("http://216.10.245.166/Library/Addbook.php",
                        json=addBookPayLoad(isbn="awer"),
                        headers={
                            "Content-Type" : "application/json"
                            }
                         )

bookID = response.json()['ID']
print(response.json()['ID'])
print(response.json())

## Delete
delete_response = requests.delete("http://216.10.245.166/Library/DeleteBook.php",
                           json={
                               "ID" : bookID
                           })
print(delete_response.text)
assert delete_response.status_code == 200
assert delete_response.json()['msg'] == "book is successfully deleted"
