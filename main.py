from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Gabigol',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Gabigol: ", resposta)
        else:
            print("Não entendi sua pergunta :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


trainer = ChatterBotCorpusTrainer(bot)
trainer = ListTrainer(bot)
trainer.train([
    "Oi", "Olá, como vai?",
    "Estou bem, e você?", "Estou ótimo, ainda Mais agora aprendendo Python!",
    "Que legal! e está gostando da linguagem?", "Sim, estou amando! É muito divertido, e gosto de inventar coisas novas! Vamos aprender também?",
    "Claro! podemos marcar um dia.", "Com certeza, te envio mensagem",
    "Blz, até mais!", "Até...",
    "Gosta do José?", "Sim, ele é um cara legal"
])