# Essa será a primeira página
import os
import horarioJogos
import curiosidadesCopa
import copasAnteriores
import jogadores


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

# @app.route("/conversa")
# def index():
#     return render_template('index.html')

@app.route("/get")
def get_bot_response():
    str(conversa.bot.get_response('Bem vindo') )
    userText = request.args.get('msg')
    while True:
        try:
            resposta = conversa.bot.get_response(userText)
            if float(resposta.confidence) > 0.2:
                return str(conversa.bot.get_response(userText))
            else:
                return str(f"<p>Ainda não tenho resposta para sua pergunta :(</p> <p> {conversa.bot_vida} </p>")
                # print("Não entendi sua pergunta :(")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
    
    # conversa.entrada = request.args.get('msg')
    # return str(conversa.bot.get_response(conversa.entrada))

if __name__ == "_main_":
    app.run




