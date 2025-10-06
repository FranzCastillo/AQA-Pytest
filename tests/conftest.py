import pytest
from app import create_app
from app.auth import users

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app({
        'TESTING': True,
        'SECRET_KEY': 'test-key'
    })
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def reset_users():
    """Reset user database to known state before tests."""
    users.clear()
    users.update({"admin": "password123"})
    yield
    users.clear()
    users.update({"admin": "password123"})
