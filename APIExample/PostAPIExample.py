import requests
from APIExample.PayLoad import *
from utilities.configurations import *
from utilities.resources import *

## Add
add_book_url = getConfig()['API']['endpoint'] + APIResourses.ADD_BOOK
query = "select * from books"
response = requests.post(add_book_url,
                         json=buildPayLoadFromDB(query),
                         headers={
                             "Content-Type": "application/json"
                         }
                         )
print(response.text)
bookID = response.json()['ID']
print(response.json()['ID'])
print(response.json())

## Delete
delete_book_url = getConfig()['API']['endpoint'] + APIResourses.DELETE_BOOK
delete_response = requests.delete(getConfig()['API']['endpoint'] + "/Library/DeleteBook.php",
                                  json={
                                      "ID": bookID
                                  })
print(delete_response.text)
assert delete_response.status_code == 200
assert delete_response.json()['msg'] == "book is successfully deleted"
