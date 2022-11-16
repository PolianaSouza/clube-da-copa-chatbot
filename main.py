from flask import Flask, render_template, request

# Arquivos do chatbox inteligente
import conversa

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/conversa/get", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    while True:
        try:
            resposta = conversa.bot.get_response(userText)
            if float(resposta.confidence) > 0.5:
                return str(conversa.bot.get_response(userText))
            else:
                return str("Não entendi sua pergunta :(")
                # print("Não entendi sua pergunta :(")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
    

if __name__ == "_main_":
    app.run