from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = []

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API funcionando correctamente"})

@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    return jsonify(tareas)

@app.route("/tareas", methods=["POST"])
def agregar_tarea():
    nueva_tarea = request.json
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104