from behave import *
from utilities.configurations import *
import requests


@given('I have github auth credential')
def step_impl(context):
    print("Github getUser--------")
    context.session = requests.session()
    context.session.auth = ('yoodahun', getConfig()['GITHUB']['token'])


@when('I hit getRepo API of github')
def step_impl(context):

    context.response = context.session.get(get_github_user_url)


@then('status code of response should be 200')
def step_impl(context):
    print(context.response.text)
    assert context.response.status_code == 200
