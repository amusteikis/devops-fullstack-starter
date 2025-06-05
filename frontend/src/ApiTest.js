import React, { useEffect, useState } from "react";

function ApiTest() {
  const [message, setMessage] = useState("Cargando...");

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL;
    console.log("API URL:", apiUrl);

    fetch(`${apiUrl}/`)
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("Error al conectar con backend"));
  }, []);

  return (
    <div>
      <h2>Prueba de conexion al backend:</h2>
      <p>{message}</p>
    </div>
  );
}

export default ApiTest;
