import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch, Mock
from services import fetch_product_by_barcode


@patch("services.requests.get")
def test_fetch_product_by_barcode_found(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Product",
            "brands": "Test Brand",
            "ingredients_text": "Sugar, Water"
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_product_by_barcode("123456789")

    assert result["barcode"] == "123456789"
    assert result["product_name"] == "Test Product"
    assert result["brand"] == "Test Brand"
    assert result["ingredients"] == "Sugar, Water"


@patch("services.requests.get")
def test_fetch_product_by_barcode_not_found(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "status": 0
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_product_by_barcode("000000000")

    assert result is None