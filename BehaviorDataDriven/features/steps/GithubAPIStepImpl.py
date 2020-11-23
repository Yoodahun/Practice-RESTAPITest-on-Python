from behave import *
from utilities.configurations import *
from utilities.resources import *
import requests


@given('I have github auth credential')
def step_impl(context):
    print("Github getUser--------")
    context.session = requests.session()
    context.session.auth = ('yoodahun', getConfig()['GITHUB']['token'])


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.session.get(APIResourses.GET_GITHUB_USER_URL)


@then('status code of response should be {status_code:d}')
def step_impl(context, status_code):
    print(context.response.text)
    print(context.response.status_code)
    assert context.response.status_code == status_code
