from flask import Flask, request, render_template, redirect, url_for
from crypt import methods
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/')
def home():
    songs = os.listdir("static/songs")
    songs_name = []
    for song in songs:
        song = song.replace(".mp3","")
        songs_name.append(song)
    return render_template("musica.html",files = songs_name,song_name = songs)

@app.route("/mensagem/")
def mensagem():
    nome = 'Flask'
    return f'Utilizo {nome}!'    

@app.route("/busca/")
def lerArgumentos():
    nome = request.args.get('nome')
    valor = request.args.get('valor')
    return f'Olá {nome}! Tenho o {valor}!' 

@app.route('/produtos/<produto>')
def lerProduto(produto):
    return f'Você escolheu o produto {produto}'

@app.route('/valor/<int:valor>')
def lerValorInteiro(valor):
    return f'O valor é {str(valor)}'

@app.route('/valorReal/<float:valor>')
def lerValorReal(valor):
    return f'O {str(valor)}'

@app.route('/bemvindo/')
def retornarArquivosHTML():
    return render_template('bemvindo.html')

@app.route('/admin/')
def admin():
    usuario = 'Admin'
    return render_template('usuario.html', usuario = usuario)   

@app.route('/professor/')
def professor():
    usuario = 'Professor'
    return render_template('usuario.html', usuario = usuario)   

@app.route('/aluno/')   
def aluno():
    usuario = 'Aluno'
    return render_template('usuario.html', usuario = usuario)   

@app.route('/user/<tipo>')
def usuario(tipo):
    if tipo == 'aluno':
        return redirect(url_for('aluno'))
    elif tipo == 'professor':
        return redirect(url_for('professor'))
    elif tipo == 'admin':
        return redirect(url_for('admin'))
    else:
        return ''' <h1> Usuário não encontrado <h1>'''

@app.route('login/', methods=['GET', 'POST'])
def login():
    metodo = request.method
    if metodo == 'POST': # Vai pegar a ação da página
        nome = request.form['nome']
        senha = request.form['senha']
        if nome == 'admin' and senha == 'admin':
            return "Seja bem vindo Admin"
        else:
            return "Imformações incorretas. Verifique as informações!"
    else: #Carrega a página
        return render_template('login.html')

@app.route('/usuarios/')
def lista_usuarios():
    lista_users = ['aluno', 'professor', 'admin']
    return render_template('usuarios.html', lista_users = lista_users)

if(__name__ == "__main__"):
    app.run(debug = True)