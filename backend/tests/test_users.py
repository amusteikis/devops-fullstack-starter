def test_list_users_empty(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_user(client):
    response = client.post("/users", json={"name": "Juan"})
    assert response.status_code == 201
    assert "message" in response.json
    assert "ID" in response.json["message"]

def test_create_user_without_name(client):
    response = client.post("/users", json={})
    assert response.status_code == 400
    assert response.json["error"] == "El nombre es obligatorio"

def test_update_user(client):
    response_create = client.post("/users", json={"name": "Ana"})
    assert response_create.status_code == 201
    user_id = int(response_create.json["message"].split("ID")[-1].strip())

    response_update = client.put(f"/users/{user_id}", json={"name": "Ana Actualizada"})
    assert response_update.status_code == 200
    assert f"{user_id}" in response_update.json["message"]
    assert "Ana Actualizada" in response_update.json["message"]


def test_update_nonexistent_user(client):
    response = client.put("/users/9999", json={"name": "Nuevo Nombre"})
    assert response.status_code == 404
    assert response.json["error"] == "Usuario no encontrado"


def test_delete_user(client):
    response = client.post("/users", json={"name": "Usuario a eliminar"})
    assert response.status_code == 201
    user_id = response.json["message"].split("ID ")[-1]
    user_id = int(user_id)

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json["message"] == f"Usuario con ID {user_id} eliminado correctamente"


def test_delete_nonexistent_user(client):
    response = client.delete("/users/999999")
    assert response.status_code == 404
    assert response.json["error"] == "Usuario no encontrado"
