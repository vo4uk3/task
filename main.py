import pytest
import requests
import random

from settings import BASE_URL,VERSION

@pytest.fixture
def create_user(url):
    id = random.randint(1, 1000)
    test_user = ''.join(['user_test', id])
    data = {
         "id": random.randint(1, 1000),
         "name":''.join(['user_test', id]),
         "email":f"{test_user}@synthetic.com",
         "gender":"male",
      },

    user = requests.post(''.join([BASE_URL, VERSION, '/public/v1/users']),data=data )
    assert user.ok

def test_user_creation_no_data(url):
    data = {

      },
    user = requests.post(''.join([BASE_URL, VERSION, '/public/v1/users']),data=data )
    assert not user.ok

def test_user_details_are_correct():
    pass

def test_user_comments():
    pass
