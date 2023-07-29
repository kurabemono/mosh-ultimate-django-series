from rest_framework import status
import pytest
from model_bakery import baker
from store.models import Collection, Product


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        collection = baker.make(Collection)
        product = {
            'title': 'a',
            'slug': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': collection.pk
        }

        response = create_product(product)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_product):
        collection = baker.make(Collection)
        product = {
            'title': 'a',
            'slug': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': collection.pk
        }
        authenticate()

        response = create_product(product)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_product):
        collection = baker.make(Collection)
        product = {
            'title': 'a',
            'slug': 'a',
            'unit_price': 1,
            'inventory': -1,
            'collection': collection.pk
        }
        authenticate(is_staff=True)

        response = create_product(product)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['inventory'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_product):
        collection = baker.make(Collection)
        product = {
            'title': 'a',
            'slug': 'a',
            'unit_price': 1,
            'inventory': 1,
            'collection': collection.pk
        }
        authenticate(is_staff=True)

        response = create_product(product)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == product.id
        assert response.data['title'] == product.title

    def test_if_product_does_not_exist_returns_404(self, api_client):
        response = api_client.get('/store/products/1/')

        assert response.status_code == status.HTTP_404_NOT_FOUND
