from behave import *
import requests
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):

    print(scenario)
    print(type(scenario))

    if "Library" in scenario.tags:
        print("Delete book information after execute BookAPI")
        response = requests.delete(getConfig()['API']['endpoint'] + APIResourses.DELETE_BOOK,
                                   json={
                                       "ID": context.bookID
                                   }
                                   )

        if response.status_code == 200:
            print("execute after_scenario hook successfully")
            print("book is successfully deleted")
        else:
            print("there is an issue")
            print(response.text)
