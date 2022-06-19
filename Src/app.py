from flask import Flask, render_template, url_for 


minha_app = Flask("__name__") 


@app.route('/')
@app.route('/minhas_informacoes.html')
def minhas_informacoes():
    return render_template("minhas_informacoes.html")

@app.route('/rotina.html')
def rotina():
    return render_template("rotina.html")

@app.route('/meus_projetos.html')
def meus_projetos():
    return render_template("meus_projetos.html")

@app.route('/hobbies.html')
def hobbies():
    return render_template("hobbies.html")
