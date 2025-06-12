import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "http://localhost:5000/users";

function UserForm() {
  const [name, setName] = useState("");
  const [users, setUsers] = useState([]);
  const [editingId, setEditingId] = useState(null);

  const fetchUsers = async () => {
    const response = await axios.get(API_URL);
    setUsers(response.data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (editingId) {
      await axios.put(`${API_URL}/${editingId}`, { name });
    } else {
      await axios.post(API_URL, { name });
    }

    setName("");
    setEditingId(null);
    fetchUsers();
  };

  const handleEdit = (user) => {
    setName(user.name);
    setEditingId(user.id);
  };

  const handleDelete = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
    fetchUsers();
  };

  return (
    <div>
      <h2>{editingId ? "Editar Usuario" : "Crear Usuario"}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          placeholder="Nombre"
          onChange={(e) => setName(e.target.value)}
        />
        <button type="submit">{editingId ? "Actualizar" : "Crear"}</button>
      </form>

      <h3>Usuarios existentes</h3>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name}{" "}
            <button onClick={() => handleEdit(user)}>✏️</button>{" "}
            <button onClick={() => handleDelete(user.id)}>🗑️</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserForm;
