import pytest
from app.auth import login, register_user, get_users_list

# Custom marker for authentication tests
pytest.mark.auth = pytest.mark.usefixtures("reset_users")


# Module-level fixture for a more efficient setup
@pytest.fixture(scope="module")
def module_level_users():
    """Reset user database once per module."""
    from app.auth import users
    original_users = users.copy()
    yield
    # Restore original users after all tests in the module
    users.clear()
    users.update(original_users)


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


@pytest.mark.xfail(reason="Demonstration of expected failure")
def test_expected_to_fail():
    """This test is expected to fail for demonstration purposes."""
    assert login("admin", "wrong_on_purpose") is True


@pytest.mark.skip(reason="Skipped for demonstration purposes")
def test_skipped_test():
    """This test is skipped and won't be executed."""
    assert False  # This would fail if executed


@pytest.mark.auth
def test_with_custom_marker():
    """Test using a custom marker that applies reset_users fixture."""
    assert "admin" in get_users_list()



@pytest.mark.parametrize("test_input,expected", [
    ("admin", True),
    ("unknown", False),
], ids=["existing-user", "non-existing-user"])
def test_user_exists(test_input, expected, reset_users):
    """Test checking if users exist in the database."""
    assert (test_input in get_users_list()) == expected
