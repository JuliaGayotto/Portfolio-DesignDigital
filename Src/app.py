from flask import Flask, render_template, url_for 


app = Flask("__name__") 


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/minhas_informacoes.html')
def minhas_informacoes():
    return render_template("minhas_informacoes.html")

@app.route('/rotina.html')
def rotina():
    return render_template("rotina.html")

@app.route('/profissional.html')
def profissional():
    return render_template("profissional.html")

@app.route('/hobbies.html')
def hobbies():
    return render_template("hobbies.html")
