from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Gabigol',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )

trainer = ChatterBotCorpusTrainer(bot)
trainer = ListTrainer(bot)
trainer.train([
    "Olá", "e ai, ancioso pros jogos?",
    "Claro, até já reservei a cerveja!", "Fiquei chateado que o Gabigol não foi convocado",
    "Pois é cara, que sacanagem! ele Joga muito bem!",
    "Joga mesmo!, chamaram o Gabriel Martinelli no lugar",
    "Injusto, já que foi Gabigol o cracke decisivo da libertadores", "que pena mesmo!",
    "Mas tomara que o Brasil ganhe o Hexa dessa vez",
    "Verdade, mas você já pensou nos times favoritos, caso ele não ganhe?",
    "Qual é cara, já está torcendo contra?",
    "Não, jamais kkkkk, mas vai que né?"
])

print("Bem vindo ao clube da copa 2022")
print("Sou o Gabigol e vamos conversar muito!!!")
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Gabigol: ", resposta)
        else:
            print("Não entendi sua pergunta :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break