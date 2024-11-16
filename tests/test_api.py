import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

# Test Case 1: Create a new vehicle (POST /vehicle)
def test_create_vehicle():
    data = {
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "Sedan",
        "horse_power": 200,
        "model_name": "Civic",
        "model_year": 2024,
        "purchase_price": 10000,
        "fuel_type": "Gasoline"
    }
    print(json.dumps(data))

    response = requests.post(f"{BASE_URL}/vehicle", json=data)
    print(f"Create Vehicle Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_get_vehicles():
    response = requests.get(f"{BASE_URL}/vehicle")
    print(f"Get All Vehicles Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_get_vehicle():
    vin = "1HGCM82633A123456"
    response = requests.get(f"{BASE_URL}/vehicle/{vin}")
    print(f"Get Vehicle Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_update_vehicle():
    vin = "1HGCM82633A123456"
    data = {
        "manufacturer_name": "Honda",
        "description": "Updated Accord Sedan",
        "horse_power": 200,
        "model_name": "Accord",
        "model_year": 2024,
        "purchase_price": 31999.99,
        "fuel_type": "Gasoline"
    }
    response = requests.put(f"{BASE_URL}/vehicle/{vin}", json=data)
    print(f"Update Vehicle Status: {response.status_code}")
    print(f"Response: {response.json()}")

# Test Case 5: Delete vehicle (DELETE /vehicle/{vin})
def test_delete_vehicle():
    vin = "1HGCM82633A123456"
    response = requests.delete(f"{BASE_URL}/vehicle/{vin}")
    print(f"Delete Vehicle Status: {response.status_code}")

# Test Case 6: Invalid VIN format (POST /vehicle)
def test_invalid_vin():
    data = {
        "vin": "INVALID",  # Too short
        "manufacturer_name": "Honda",
        "description": "Accord Sedan",
        "horse_power": 192,
        "model_name": "Accord",
        "model_year": 2024,
        "purchase_price": 29999.99,
        "fuel_type": "Gasoline"
    }
    response = requests.post(f"{BASE_URL}/vehicle", json=data)
    print(f"Invalid VIN Status: {response.status_code}")
    print(f"Response: {response.json()}")

# Test Case 7: Invalid horse power (POST /vehicle)
def test_invalid_horsepower():
    data = {
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "Accord Sedan",
        "horse_power": -192,  # Negative value
        "model_name": "Accord",
        "model_year": 2024,
        "purchase_price": 29999.99,
        "fuel_type": "Gasoline"
    }
    response = requests.post(f"{BASE_URL}/vehicle", json=data)
    print(f"Invalid Horsepower Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    # Run all tests
    print("Running test cases...")
    test_create_vehicle()
    test_get_vehicles()
    test_get_vehicle()
    test_update_vehicle()
    test_delete_vehicle()
    test_invalid_vin()
    test_invalid_horsepower()