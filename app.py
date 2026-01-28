from flask import Flask, request, jsonify

app = Flask(__name__)

# Route pour l'addition
@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"operation": "addition", "result": a + b, "status": "success"})
    except (TypeError, ValueError):
        return jsonify({"error": "Paramètres 'a' et 'b' invalides"}), 400

# Route pour la soustraction
@app.route('/sub', methods=['GET'])
def sub():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"operation": "soustraction", "result": a - b, "status": "success"})
    except (TypeError, ValueError):
        return jsonify({"error": "Paramètres invalides"}), 400
    
# Route pour la multiplication
@app.route('/mul', methods=['GET'])
def mul():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"operation": "multiplication", "result": a * b, "status": "success"})
    except (TypeError, ValueError):
        return jsonify({"error": "Paramètres invalides"}), 400

# Route pour la division (avec gestion d'erreur)
@app.route('/div', methods=['GET'])
def div():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division par zéro impossible"}), 400
        return jsonify({"operation": "division", "result": a / b, "status": "success"})
    except (TypeError, ValueError):
        return jsonify({"error": "Paramètres invalides"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)