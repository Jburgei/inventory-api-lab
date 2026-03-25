import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pytest
from app import app
from data import inventory


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_all_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_inventory_item_found(client):
    response = client.get('/inventory/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert data["name"] == "Milk"


def test_get_single_inventory_item_not_found(client):
    response = client.get('/inventory/999')
    assert response.status_code == 404
    assert response.get_json()["error"] == "Item not found"


def test_post_inventory_item(client):
    response = client.post('/inventory', json={
        "name": "Sugar",
        "price": 180,
        "stock": 12
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Sugar"
    assert data["price"] == 180
    assert data["stock"] == 12


def test_patch_inventory_item(client):
    response = client.patch('/inventory/1', json={
        "price": 150
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert data["price"] == 150


def test_delete_inventory_item(client):
    client.post('/inventory', json={
        "name": "Tea",
        "price": 90,
        "stock": 8
    })

    response = client.delete('/inventory/3')
    assert response.status_code == 204