from flask import app, Flask, render_template


minha_app = Flask(__name__) 


@minha_app.route('/')
@minha_app.route('/minhas_informacoes.html')
def minhas_informacoes():
    return render_template("minhas_informacoes.html")

@minha_app.route('/rotina.html')
def rotina():
    return render_template("rotina.html")

@minha_app.route('/meus_projetos.html')
def meus_projetos():
    return render_template("meus_projetos.html")

@minha_app.route('/hobbies.html')
def hobbies():
    return render_template("hobbies.html")
