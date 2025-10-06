import json
import pytest

def test_health_endpoint(client):
    """Test the health endpoint returns 200."""
    response = client.get("/health")
    assert response.status_code == 200
    assert json.loads(response.data)["status"] == "ok"

def test_get_users(client, reset_users):
    """Test the users endpoint returns user list."""
    response = client.get("/users")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "users" in data
    assert "admin" in data["users"]

class TestLoginEndpoint:
    def test_login_success(self, client, reset_users):
        """Test successful login endpoint."""
        response = client.post(
            "/login",
            json={"username": "admin", "password": "password123"}
        )
        assert response.status_code == 200
        assert "Login successful" in json.loads(response.data)["message"]

    def test_login_failure(self, client, reset_users):
        """Test failed login endpoint."""
        response = client.post(
            "/login",
            json={"username": "admin", "password": "wrongpass"}
        )
        assert response.status_code == 401
        assert "Invalid credentials" in json.loads(response.data)["message"]

    def test_login_missing_data(self, client):
        """Test login with missing data."""
        response = client.post("/login", json={})
        assert response.status_code == 400
