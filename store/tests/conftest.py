from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate

@pytest.fixture
def create_object(api_client):
    def do_create_object(endpoint ,object):
        return api_client.post(f'/store/{endpoint}/', object)
    return do_create_object