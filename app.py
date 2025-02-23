from flask import Flask, jsonify, request
#from flask_cors import CORS
import json, os

app = Flask(__name__)
#CORS(app)
database_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")

# Function for loading Data
def load_data() -> dict:
    with open(database_file, "r", encoding="utf-8") as database:
        return json.load(database)

# Function for saving Data
def save_data(data: dict) -> None:
    with open(database_file, "w", encoding="utf-8") as database:
        json.dump(data, database, indent=4)

# Flask route for getting Aulas
@app.route("/aulas", methods=["GET"])
def get_aulas():
    data = load_data()
    return jsonify(data["aulas"])

# Flask route for adding Aulas
@app.route("/aulas", methods=["POST"])
def add_aulas():
    data = load_data()
    newAula = request.json

    # New ID for Aula
    newAula["id"] = len(data["aulas"]) + 1 # Aulas amount + 1
    data["aulas"].append(newAula)

    # Save and return new data
    save_data(data)
    return jsonify({
        "Mensagem do Servidor": "Aula Adicionada com Sucesso!"
    }), 200

# Flask route for getting Alunos
@app.route("/alunos", methods=["GET"])
def get_alunos():
    data = load_data()
    return jsonify(data["alunos"])

# Flask route for adding Alunos
@app.route("/alunos", methods=["POST"])
def add_alunos():
    data = load_data()
    newAluno = request.json

    # New ID for Aluno
    newAluno["id"] = len(data["alunos"]) + 1 # Alunos amount + 1
    data["alunos"].append(newAluno)

    # Save and return new data
    save_data(data)
    return jsonify({
        "Mensagem do Servidor": "Aluno cadastrado com Sucesso!"
    }), 200

@app.route("/")
def home():
    return "<h1>Error: 404</h1>"

if __name__ == "__main__":  
    port = int(os.environ.get("PORT", 5000))  # Render define a porta automaticamente  
    app.run(host="0.0.0.0", port=port)  
