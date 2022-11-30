# módulo para remover acentos das strings
from unidecode import unidecode
from flask import Flask, render_template, request

# Arquivos do chatbox inteligente
import conversa

app = Flask(__name__)

mensagem = (f"Seja bem vindo ao clube da COPA 2022, aqui você vai fica por dentro de todas as novidades sobre a copa do mundo!")

dica = ("Algumas coisas que eu sei:")
clube = ["Horários dos jogos", "Curiosidades sobre a copa do mundo", "informações sobre os jogadores"]

@app.route("/")
def inicio():
    
    return render_template('index.html', msgs=mensagem, dica=dica, clube=clube)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText = unidecode(userText).lower()
    while True:
        try:
            resposta = conversa.bot.get_response(userText)
            if float(resposta.confidence) > 0.5:
                return str(conversa.bot.get_response(userText))
            else:
                return str(f"<p>Ainda não tenho resposta para sua pergunta :(</p> <p> {conversa.bot_aprendizado} </p>")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break

# if __name__ == "_main_":
#     app.run




