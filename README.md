# Inventory API Lab

A Flask-based Inventory Management System that supports CRUD operations, external API integration with OpenFoodFacts, a command-line interface (CLI), and automated tests using pytest.

## Features

- View all inventory items
- View a single inventory item by ID
- Add a new inventory item
- Update an inventory item
- Delete an inventory item
- Search external product information by barcode using OpenFoodFacts
- Interact with the API using a CLI
- Run automated tests with pytest

## Project Structure

inventory-api-lab/
- app.py
- data.py
- services.py
- cli.py
- requirements.txt
- README.md
- .gitignore
- tests/
  - test_app.py
  - test_cli.py
  - test_services.py

## Technologies Used

- Python
- Flask
- Requests
- Pytest

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Jburgei/inventory-api-lab
cd inventory-api-lab
''''

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the Flask application

```bash
python3 app.py

### 5. Run the CLI 

Open a second terminal 
source bin/venv/activate
python3 cli.py

### 6. Run tests

pytest -v