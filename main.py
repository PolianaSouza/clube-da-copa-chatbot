from flask import Flask, render_template, request

# Arquivos do chatbox inteligente
import conversa

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(conversa.bot.get_response(userText))

if __name__ == "_main_":
    app.run