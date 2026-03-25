import requests

BASE_URL = "http://127.0.0.1:5000"


def show_menu():
    print("\nInventory Management CLI")
    print("1. View all inventory")
    print("2. View item by ID")
    print("3. Add new item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Search external product by barcode")
    print("7. Exit")


def view_all_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())


def view_item_by_id():
    item_id = input("Enter item ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())


def add_new_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))

    payload = {
        "name": name,
        "price": price,
        "stock": stock
    }

    response = requests.post(f"{BASE_URL}/inventory", json=payload)
    print(response.json())


def update_item():
    item_id = input("Enter item ID to update: ")

    print("Leave blank if you don’t want to update a field.")
    name = input("New name: ")
    price = input("New price: ")
    stock = input("New stock: ")

    payload = {}

    if name:
        payload["name"] = name
    if price:
        payload["price"] = float(price)
    if stock:
        payload["stock"] = int(stock)

    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=payload)
    print(response.json())


def delete_item():
    item_id = input("Enter item ID to delete: ")
    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 204:
        print({"message": "Item deleted successfully"})
    else:
        print(response.json())


def search_external_product():
    barcode = input("Enter barcode: ")
    response = requests.get(f"{BASE_URL}/external/barcode/{barcode}")
    print(response.json())


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_all_inventory()
        elif choice == "2":
            view_item_by_id()
        elif choice == "3":
            add_new_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            search_external_product()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()