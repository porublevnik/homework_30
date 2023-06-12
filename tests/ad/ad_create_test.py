import pytest
from rest_framework import status

@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        'author': user.pk,
        'category': category.pk,
        'name': 'Стол из слэба',
        'price': 7677
    }
    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Стол из слэба",
        "price": 7677,
        "description": None,
        "image": None,
        "author": user.pk,
        "category": category.pk
    }

    response = client.post(f'/ad/', data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data

