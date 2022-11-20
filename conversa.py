from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import curiosidades


bot = ChatBot('Gabigol',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3',
        logic_adapters=[
            {'import_path': 'chatterbot.logic.BestMatch'},
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                "output_text": 'Ok, vou te ajudar' 
            }
        ]
)

linkBrasil = 'https://www.google.com/search?q=hor%C3%A1rios+dos+jogos+da+copa&oq=hor%C3%A1rios+dos+jogos+da+copa&aqs=chrome..69i57j0i131i433i512l6j0i512l3.5104j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/m/0fp_8fm;2;/m/030q7;mt;fp;1;;;'

trainer = ChatterBotCorpusTrainer(bot) 
trainer = ListTrainer(bot)
trainer.train([
    'ola', 'Do que vamos conversar hoje?',
    'horarios dos jogos','do Brasil ou de todos?',
    'do brasil', f'<img src="../static/assets/horario.png"/>'
    f'pode conferir no <a href="{linkBrasil}">Link</a>',
    'todos', '<img src="../static/assets/todos.png"/>',
    'curiosidades', curiosidades.ultima_copa 
])

# trainer.train([
#     "Olá", "e ai, ancioso pros jogos?",
#     "Claro, até já reservei a cerveja!", "Fiquei chateado que o Gabigol não foi convocado",
#     "Pois é cara, que sacanagem! ele Joga muito bem!",
#     "Joga mesmo!, chamaram o Gabriel Martinelli no lugar",
#     "Injusto, já que foi Gabigol o cracke decisivo da libertadores", "que pena mesmo!",
#     "Mas tomara que o Brasil ganhe o Hexa dessa vez",
#     "Verdade, mas você já pensou nos times favoritos, caso ele não ganhe?",
#     "Qual é cara, já está torcendo contra?",
#     "Não, jamais kkkkk, mas vai que né?"
# ])

# print("Bem vindo ao clube da copa 2022")
# print("Sou o Gabigol e vamos conversar muito!!!")
# while True:
#     try:
#         resposta = bot.get_response(input("Usuário: "))
#         if float(resposta.confidence) > 0.5:
#             print("Gabigol: ", resposta)
#         else:
#             print("Não entendi sua pergunta :(")
#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break