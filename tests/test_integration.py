import json


def test_register_then_login(client, reset_users):
    """Test registering a new user then logging in."""
    # Register a new user
    register_response = client.post(
        "/register",
        json={"username": "testuser", "password": "testpass"}
    )
    assert register_response.status_code == 201

    # Verify user appears in user list
    users_response = client.get("/users")
    users_data = json.loads(users_response.data)
    assert "testuser" in users_data["users"]

    # Login with the new user
    login_response = client.post(
        "/login",
        json={"username": "testuser", "password": "testpass"}
    )
    assert login_response.status_code == 200
    assert json.loads(login_response.data)["message"] == "Login successful"
