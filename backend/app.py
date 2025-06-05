from flask import Flask, jsonify
from flask_cors import CORS  # ✅ Agregado

app = Flask(__name__)
CORS(app)  # ✅ Habilita CORS para todas las rutas

@app.route("/")
def home():
    return jsonify({"message": "Hola desde el backend Flask!"})  # también cambiamos para que devuelva JSON

@app.route("/ping")
def ping():
    return jsonify({"message": "Pong!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
