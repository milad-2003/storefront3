from rest_framework import status
from store.models import Collection
from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_return_401(self, create_object):
        response = create_object('products', {
            'title': 'a',
            'slug': 'a',
            'description': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': 1
        })

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_admin_return_403(self, authenticate, create_object):
        authenticate()

        response = create_object('products', {
            'title': 'a',
            'slug': 'a',
            'description': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': 1
        })

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_400(self, authenticate, create_object):
        authenticate(True)

        response = create_object('products', {
            'title': '',
            'slug': 'a',
            'description': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': 1
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, authenticate, create_object):
        authenticate(True)
        collection = baker.make(Collection)
        
        response = create_object('products', {
            'title': 'a',
            'slug': 'a',
            'description': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': collection.id
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        