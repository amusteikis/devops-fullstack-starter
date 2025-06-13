from flask import Flask, jsonify, request
from flask_cors import CORS  # ✅ Agregado
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError
import os
import time

load_dotenv()

app = Flask(__name__)
CORS(app)  # ✅ Habilita CORS para todas las rutas

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")

    if not name:
      return jsonify({"error": "El nombre es obligatorio"}), 400

    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": f"usuario '{user.name}' creado con ID {user.id}"}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "El nombre es obligatorio"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    user.name = name
    db.session.commit()

    return jsonify({"message": f"Usuario con ID {user_id} actualizado a '{name}'"})


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": f"Usuario con ID {user_id} eliminado correctamente"})



@app.route("/users", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@app.route("/")
def home():
    return jsonify({"message": "Hola desde el backend Flask!"})  # también cambiamos para que devuelva JSON

@app.route("/ping")
def ping():
    return jsonify({"message": "Pong!"})

if __name__ == "__main__":
    with app.app_context():
        for _ in range(10):  # 10 intentos con espera
            try:
                db.create_all()
                print("Tablas creadas exitosamente.")
                break
            except OperationalError:
                print("La base de datos no está lista. Reintentando en 2 segundos...")
                time.sleep(2)
        else:
            print("No se pudo conectar a la base de datos después de múltiples intentos.")
    app.run(host="0.0.0.0", port=5000)
