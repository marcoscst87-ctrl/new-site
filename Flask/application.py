from flask import Flask, render_template, request
app = Flask(__name__)# name contem o nome do arquivo atual, esta dizendo que é um servidor web
@app.route("/") # o @ no python é apricar uma função a outra
def index():
    return "Bem Vindo Dev"
    # return render_template("teste2.html") Direcionando para página web
@app.route("/ola") # o @ no python é aplicar uma função a outra
def ola():
    return 'Seja Bem vindo' # para aparecer "seja bem vindo" adicione na Url /ola
if __name__ == '__main__':
    app.run(debug=True) # permitir debugar, atualizar código do navegador a medida que edita 