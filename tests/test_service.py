import json

import pytest
import requests

import source.service as service
# We'll use unittest (which comes with python) together with pytest
import unittest.mock as mock

import tests.utils.helpers as helpers

# mock needs to specify the function we are mocking
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    # arrange
    # defining what is returned from the mock
    mock_get_user_from_db.return_value = "Mocked Alice"

    # act
    # actual call to service's function
    user_name = service.get_user_from_db(1)

    # assert
    assert user_name == "Mocked Alice"

# mocking only the requests.get API call, still validating the function
@mock.patch("requests.get")
def test_get_users(mock_get):
    # arrange
    # defining what is returned from the mock
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = helpers.load_json('test_data/users.json')

    mock_get.return_value = mock_response

    # act
    # actual call to service's function
    data = service.get_users()

    # assert
    assert data == helpers.load_json('test_data/users.json')
    assert data[0]["name"] == "Leanne Graham"
    assert len(data) == 2

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    # arrange
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    # act and assert
    with pytest.raises(requests.HTTPError):
        service.get_users()
