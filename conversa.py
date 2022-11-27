from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import curiosidadesCopa
import curiosidadesJogadores
import filters


bot = ChatBot('Galvão Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3',
        filters=[filters.get_recent_repeated_responses]
)

horario_jogos = 'https://www.google.com/search?q=hor%C3%A1rios+dos+jogos+da+copa&oq=hor%C3%A1rios+dos+jogos+da+copa&aqs=chrome..69i57j0i131i433i512l6j0i512l3.5104j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/m/0fp_8fm;2;/m/030q7;mt;fp;1;;;'

saber_algo = ("Gostaria de saber algo mais?")
bot_vida = ("<p> Coisas que eu sei até o momento:</p> <ul> <li>curiosidades</li> <li>Horários dos jogos</li> <li>Placar dos jogos</li> </ul> </br>  <p>Digite a palavra referente ao assunto </p>")
# <p></P>
trainer = ChatterBotCorpusTrainer(bot) 
trainer = ListTrainer(bot)
trainer.train([
    'ola', 'Sobre o que vamos conversar hoje?',
    'horarios dos jogos','do Brasil ou de todos?',
    'do brasil', f'<img src="../static/assets/horario.png"/> '
    f'<p> pode conferir no <a href="{horario_jogos}" target="_blank">Link</a></p> <p>{saber_algo}</p>',
    'de todos',
    f'<img src="../static/assets/todos.png"/><p> pode conferir no <a href="{horario_jogos}" target="_blank">Link</a>.<p/p> <p>{saber_algo}</p>',
    "sim", f'{bot_vida}',  
    'curiosidades', "Você quer saber curiosidades sobre a copa ou sobre os jogadores?",
    "sobre a copa", f'<h5>Escolha uma curiosidade digitando o número referente</h5> <ol> <li>{curiosidadesCopa.array_titulos[0]}</li> <li>{curiosidadesCopa.array_titulos[1]}</li> <li> {curiosidadesCopa.array_titulos[2]} </li> </ol>',
    "1", f'{curiosidadesCopa.array_curiosidades[0]} <p> {saber_algo} </p>',
    "2", f'{curiosidadesCopa.array_curiosidades[1]} <p> {saber_algo} </p>',
    "3", f'{curiosidadesCopa.array_curiosidades[2]} <p> {saber_algo} </p>', #ate aqui ok
    "sobre os jogadores", f'<h5>Para escolher uma curiosidade digite a letra referente</h5> <ol type="I"> <li>{curiosidadesJogadores.array_jogadores_titulos[0]}</li> <li>{curiosidadesJogadores.array_jogadores_titulos[1]}</li> <li> {curiosidadesJogadores.array_jogadores_titulos[2]} </li> </ol>',
    f'i', f'{curiosidadesJogadores.array_informacoes[0]} <p> {saber_algo} </p>',
    "ii", f'{curiosidadesJogadores.array_informacoes[1]} <p> {saber_algo} </p>',
    "iii", f'{curiosidadesJogadores.array_informacoes[2]} <p> {saber_algo} </p>', 
    "não", "Obrigado pelo seu tempo, quando quiser saber mais curiosidades sobre a copa é só chamar! :-)"
    
])

# <li></li>