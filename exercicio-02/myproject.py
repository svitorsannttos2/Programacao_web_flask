from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    variavel = "Adivinhe o número correto"

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)     
    else:
        
        numero = random.randint(1,5)
        palpite = request.form.get(numero)

        if numero == palpite:
            return '<h1> Você acertou o número <h1>'
        else:
            return '<h1> Você não encontrou o número <h1>'

@app.route("/paginainicial")
def pgInicial():
    return "Página nova"

@app.route("/erro")
def erro():
    return "Página não encontrada"        

if(__name__ == "__main__"):
    app.run()