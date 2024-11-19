# Vehicle Management API

FastAPI-based REST API for managing vehicle information with SQLite database backend. This API provides endpoints for creating, reading, updating, and deleting vehicle records with data validation and error handling.

## Features

- Full CRUD operations for vehicle records
- Data validation for all inputs
- SQLite database with SQLAlchemy ORM
- Automatic VIN normalization (uppercase)
- Validation for:
  - Vehicle year (1900-2100)
  - Horsepower (must be > 0)
  - Purchase price (must be > 0)
  - VIN (17 characters)

## Technical Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/vehicle` | Retrieve all vehicles |
| POST | `/vehicle` | Create a new vehicle |
| GET | `/vehicle/{vin}` | Retrieve a specific vehicle by VIN |
| PUT | `/vehicle/{vin}` | Update a vehicle by VIN |
| DELETE | `/vehicle/{vin}` | Delete a vehicle by VIN |

## Data Storage Model

Vehicle records include the following fields:

- `vin` (String, Primary Key): Vehicle Identification Number
- `manufacturer_name` (String): Vehicle manufacturer
- `description` (String, Optional): Vehicle description
- `horse_power` (Integer): Engine horsepower
- `model_name` (String): Model name
- `model_year` (Integer): Year of manufacture
- `purchase_price` (Decimal): Purchase price
- `fuel_type` (String): Type of fuel used

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## Error Handling

The API includes comprehensive error handling for:
- Duplicate VIN entries
- Invalid data formats
- Resource not found cases
- Validation failures

## Example Usage

### Create a Vehicle

```sh
curl -X POST "http://127.0.0.1:8000/vehicle" ^ -H "Content-Type: application/json" ^ -d "{ \"vin\": \"1HGCM82633A123456\", \"manufacturer_name\": \"Honda\", \"description\": \"Sedan\", \"horse_power\": 200, \"model_name\": \"Civic\", \"model_year\": 2024, \"purchase_price\": 10000.0, \"fuel_type\": \"Gasoline\" }"
```

## Update a Vehicle

```sh
curl -X PUT "http://127.0.0.1:8000/vehicle/1HGCM82633A123456" ^-H "Content-Type: application/json" ^-d "{\"manufacturer_name\": \"Honda\",        \"description\": \"Sedan\",        \"horse_power\": 220,        \"model_name\": \"Accord\",        \"model_year\": 2024,        \"purchase_price\": 10500.0,        \"fuel_type\": \"Gasoline\"    }
```

# Get all Vehicles
```sh
curl -X GET "http://127.0.0.1:8000/vehicle" 
```

# Get all Vehicle by VIN
```sh
curl -X GET "http://127.0.0.1:8000/vehicle/1HGCM82633A123456"
```

# Delete a Vehicle by VIN 
```sh
curl -X DELETE "http://127.0.0.1:8000/vehicle/1"
```
