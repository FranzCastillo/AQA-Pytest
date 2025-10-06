# Simple in-memory user database for demo purposes
users = {
    "admin": "password123"
}

def login(username, password):
    """Authenticate a user with username and password."""
    if not username or not password:
        return False
    return username in users and users[username] == password

def register_user(username, password):
    """Register a new user."""
    if username in users:
        return False
    users[username] = password
    return True

def get_users_list():
    """Return a list of registered usernames."""
    return list(users.keys())
