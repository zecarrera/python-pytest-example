import requests

# Example hardcoded database to allow for experimenting with mocking in our tests
database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)

# Example API call to opensource API
def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError("Failed to retrieve users from JsonPlaceholder")