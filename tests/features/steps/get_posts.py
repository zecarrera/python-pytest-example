import requests
from behave import *
URL = "https://jsonplaceholder.typicode.com/"

@given('API service is running')
def step_impl(context):
    response = requests.get(URL)
    assert response.status_code == 200


@when('retrieving posts')
def step_impl(context):
    context.response = requests.get(f"{URL}posts")
    assert context.response.status_code == 200

@when('retrieving post with ID {text}')
def step_impl(context, text):
    print(URL + "posts/" + text)
    context.response = requests.get(f"{URL}posts/{text}")
    assert context.response.status_code == 200

@then('list of posts is not empty')
def step_impl(context):
    assert len(context.response.json()) > 0

@then('only post with ID {text} is retrieved')
def step_impl(context, text):
    data = context.response.json()
    assert data["id"] == int(text)
    assert len(data["title"]) > 0
    assert len(data["body"]) > 0
