import requests

authToken = ''

def test_sign_up():
    url = "http://localhost:5000/auth/sign-up"
    requestData = {
        "email": "test@gmail.com",
        "password": "testing@123",
        "re_password": "testing@123"
    }
    response = requests.post(url, json=requestData, headers={"Content-Type": "application/json"})

    # Verify status code
    authToken = response.json()
    if response.status_code == 409:
        print("User already exists")
    if response.status_code == 200:
        assert response.status_code == 200 

autoToken = ''

def test_sign_in():
    url = "http://localhost:5000/auth/sign-in"
    requestData = {
        "email": "test@gmail.com",
        "password": "test@123"
    }
    response = requests.post(url, json=requestData, headers={"Content-Type": "application/json"})

    # Verify status code
    global authToken
    authToken = response.json().get('token')
    assert response.status_code == 200

# inventory
def test_store_inventory():
    url = "http://localhost:5000/inventory"
    requestData = {
        "item_name": "product 2322222",
        "category": "category d 001",
        "supplier": "supplier A",
        "quantity": 10,
        "unit_price": 500,
        "location": "aranthangi"
    }
    
    response = requests.post(url, json=requestData, headers={"Content-Type": "application/json", 'Authorization': f'Bearer {authToken}'})

    # Verify status code
    data = response.json()
    print(data)
    if response.status_code == 409:
        print("Item already exists")
        assert response.status_code == 409
    if response.status_code == 201:
        print("Item added successfully")
        assert response.status_code == 201 

def test_get_inventory():
    url = "http://localhost:5000/inventory"

    response = requests.get(url, json={}, headers={"Content-Type": "application/json", 'Authorization': f'Bearer {authToken}'})

    # Verify status code
    assert response.status_code == 200

def test_one_inventory():
    url = "http://localhost:5000/inventory/1"

    response = requests.get(url, json={}, headers={"Content-Type": "application/json", 'Authorization': f'Bearer {authToken}'})

    # Verify status code
    if response.status_code == 404:
        print("Item not found")
        assert response.status_code == 404

    if response.status_code == 200:
        print("Item found")
        assert response.status_code == 200 

def test_update_inventory():
    url = "http://localhost:5000/inventory/1"
    requestData = {
        "item_name": "product 3322 (updated)",
        "category": "category d 001",
        "supplier": "supplier A",
        "quantity": 10,
        "unit_price": 500,
        "location": "aranthangi"
    }
    response = requests.post(url, json=requestData, headers={"Content-Type": "application/json", 'Authorization': f'Bearer {authToken}'})

    if response.status_code == 404:
        print("Item not found")
        assert response.status_code == 404

    if response.status_code == 200:
        print("Item updated successfully")
        assert response.status_code == 200 

def test_delete_inventory():
    url = "http://localhost:5000/inventory/1"
    requestData = {}
    response = requests.delete(url, json=requestData, headers={"Content-Type": "application/json", 'Authorization': f'Bearer {authToken}'})

    # Verify status code
    if response.status_code == 404:
        print("Item not found")
        assert response.status_code == 404

    if response.status_code == 200:
        print("Item deleted successfully")
        assert response.status_code == 200