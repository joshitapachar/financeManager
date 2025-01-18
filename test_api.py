import requests

BASE_URL = "http://127.0.0.1:5000"

# 1. Register a User
response = requests.post(
    f"{BASE_URL}/register",
    json={
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "securepassword",
    },
)
print("Register Response:", response.json())

# 2. Login
response = requests.post(
    f"{BASE_URL}/login",
    json={"email": "john.doe@example.com", "password": "securepassword"},
)
print("Login Response:", response.json())

# Extract user_id from the login response
user_id = response.json().get("user_id")

# 3. Add a Transaction
response = requests.post(
    f"{BASE_URL}/transactions",
    json={
        "user_id": user_id,
        "amount": 100.0,
        "date": "2025-01-15",
        "category": "Food",
        "description": "Lunch with friends",
    },
)
print("Add Transaction Response:", response.json())

# 4. Get Transactions
response = requests.get(f"{BASE_URL}/transactions/{user_id}")
print("Get Transactions Response:", response.json())

# 5. Add a Category
response = requests.post(
    f"{BASE_URL}/categories", json={"user_id": user_id, "name": "Utilities"}
)
print("Add Category Response:", response.json())

# 6. Get Categories
response = requests.get(f"{BASE_URL}/categories/{user_id}")
print("Get Categories Response:", response.json())
