import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch, Mock
import cli


@patch("builtins.input", side_effect=["1"])
@patch("builtins.print")
def test_show_menu_and_choose_option(mock_print, mock_input):
    with patch("cli.view_all_inventory") as mock_view:
        with patch("cli.show_menu"):
            choice = input("Choose an option: ")
            if choice == "1":
                cli.view_all_inventory()

            mock_view.assert_called_once()


@patch("cli.requests.get")
@patch("builtins.print")
def test_view_all_inventory(mock_print, mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [
        {"id": 1, "name": "Milk", "price": 120, "stock": 10}
    ]
    mock_get.return_value = mock_response

    cli.view_all_inventory()

    mock_get.assert_called_once_with("http://127.0.0.1:5000/inventory")
    mock_print.assert_called_once()