from behave import *
from utilities.configurations import *
from utilities.resources import *
from APIExample.PayLoad import *
import json
import requests


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.add_book_url = getConfig()['API']['endpoint'] + APIResourses.add_book
    query = "select * from books"
    context.payload = buildPayLoadFromDB(query)


@when('We execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.add_book_url,
                                     json=context.payload,
                                     headers={
                                         "Content-Type": "application/json"
                                     }
                                     )


@then('book is successfully added')
def step_impl(context):
    context.bookID = context.response.json()['ID']

    assert context.response.status_code == 200
    assert context.response.json()['Msg'] == "successfully added"


@given("the Book details with {isbn} and {aisle}")
def step_impl(context, isbn, aisle):
    """
    :type context: behave.runner.Context
    :type isbn: str
    :type aisle: str
    """
    print("start Scenario Outline")
    context.add_book_url = getConfig()['API']['endpoint'] + APIResourses.add_book
    context.payload = addBookPayLoad(isbn, aisle)
