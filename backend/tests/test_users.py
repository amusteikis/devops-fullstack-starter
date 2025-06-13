def test_list_users_empty(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json, list)
