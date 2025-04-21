from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# ------- wcześniejsze trasy -----------------------------------------------
@app.route('/')
def home():
    return jsonify(message="Witaj w moim API!")

@app.route('/mojastrona')
def moja_strona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get("name")
    msg = f"Hello {name}!" if name else "Hello!"
    return jsonify(message=msg)

# ------- NOWA trasa: /api/v1.0/predict -------------------------------------
@app.route('/api/v1.0/predict')
def predict():
    """Przykładowy 'model ML':
       zwraca 1, jeśli num1 + num2 > 5.8, w przeciwnym razie 0
    """
    try:
        num1 = float(request.args.get("num1", None))
        num2 = float(request.args.get("num2", None))
    except (TypeError, ValueError):
        # jeśli któryś parametr jest pusty lub nie‑liczbą, zwracamy 400
        abort(400, description="num1 i num2 muszą być liczbami")

    s = num1 + num2
    pred = 1 if s > 5.8 else 0

    return jsonify(
        prediction=pred,
        features={"num1": num1, "num2": num2}
    )

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)   # use_reloader=False ⇢ brak podwójnego startu
