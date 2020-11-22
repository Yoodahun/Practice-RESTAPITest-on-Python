from behave import *
from utilities.configurations import *
from utilities.resources import *
from APIExample.PayLoad import *
import json
import requests


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.add_book_url = getConfig()['API']['endpoint'] + APIResourses.add_book
    context.query = "select * from books"


@when('We execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.add_book_url,
                                     json=buildPayLoadFromDB(context.query),
                                     headers={
                                         "Content-Type": "application/json"
                                     }
                                     )


@then('book is successfully added')
def step_impl(context):
    bookID = context.response.json()['ID']

    requests.delete(getConfig()['API']['endpoint'] + APIResourses.delete_book,
                    json={
                        "ID": bookID
                    })

    assert context.response.status_code == 200
    assert context.response.json()['Msg'] == "successfully added"
