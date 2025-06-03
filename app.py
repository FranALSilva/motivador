from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

frases = [
    "Você é mais forte do que imagina!",
    "Acredite no seu potencial!",
    "Cada dia é uma nova chance para vencer!",
    "Nunca é tarde para recomeçar!",
    "Coragem é agir com o coração!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frase')
def frase():
    return jsonify(frase=random.choice(frases))

if __name__ == '__main__':
    app.run(debug=True)
