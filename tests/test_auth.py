import pytest
from app.auth import login, register_user, get_users_list

def test_login_success(reset_users):
    """Test successful login."""
    assert login("admin", "password123") is True

def test_login_failure_wrong_password(reset_users):
    """Test login with wrong password."""
    assert login("admin", "wrongpassword") is False

def test_login_failure_nonexistent_user(reset_users):
    """Test login with nonexistent user."""
    assert login("nonexistent", "password") is False

@pytest.mark.parametrize("username,password,expected", [
    (None, "password", False),
    ("username", None, False),
    (None, None, False),
])
def test_login_invalid_inputs(username, password, expected):
    """Test login with invalid inputs."""
    assert login(username, password) == expected

def test_register_new_user(reset_users):
    """Test registering a new user."""
    assert register_user("newuser", "password456") is True
    assert "newuser" in get_users_list()
    assert login("newuser", "password456") is True

def test_register_existing_user(reset_users):
    """Test registering an existing user."""
    assert register_user("admin", "newpassword") is False
    assert login("admin", "password123") is True  # Old password still works
