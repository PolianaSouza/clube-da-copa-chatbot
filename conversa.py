from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import curiosidadesCopa
import curiosidadesJogadores
import tempoReal
import filters


bot = ChatBot('Galvão Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3',
        filters=[filters.get_recent_repeated_responses]
)

horario_jogos = 'https://www.google.com/search?q=hor%C3%A1rios+dos+jogos+da+copa&oq=hor%C3%A1rios+dos+jogos+da+copa&aqs=chrome..69i57j0i131i433i512l6j0i512l3.5104j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/m/0fp_8fm;2;/m/030q7;mt;fp;1;;;'

saber_algo = ("Gostaria de saber algo mais?")
bot_aprendizado = ("<p> Coisas que eu sei até o momento:</p> <ul> <li>Curiosidades</li> <li>Horários dos jogos</li> <li>Informações em tempo real</li> </ul> </br>  <p>Digite a palavra referente ao assunto </p>")
# <p></P>
trainer = ChatterBotCorpusTrainer(bot) 
trainer = ListTrainer(bot)
trainer.train([
    'ola', 'Sobre o que vamos conversar hoje?',
    #Informações horários
    'horarios dos jogos','do Brasil ou de todos?',
    'do brasil', f'<img src="../static/assets/horario.png"/> '
    f'<p> pode conferir no <a href="{horario_jogos}" target="_blank">Link</a></p> <p>{saber_algo}</p>',
    'de todos',
    f'<img src="../static/assets/todos.png"/><p> pode conferir no <a href="{horario_jogos}" target="_blank">Link</a>.<p/p> <p>{saber_algo}</p>',
    "sim", f'{bot_aprendizado}',  
    'curiosidades', "Você quer saber curiosidades sobre a copa ou sobre os jogadores?",
    #Informações sobre a copa
    "sobre a copa", f'<h5>Escolha uma curiosidade digitando o número referente</h5> <ol> <li>{curiosidadesCopa.array_titulos[0]}</li> <li>{curiosidadesCopa.array_titulos[1]}</li> <li> {curiosidadesCopa.array_titulos[2]} </li> <li> {curiosidadesCopa.array_titulos[3]} </li> <li> {curiosidadesCopa.array_titulos[4]} </li> </ol>',
    "1", f'{curiosidadesCopa.array_curiosidades[0]} <p> {saber_algo} </p>',
    "2", f'{curiosidadesCopa.array_curiosidades[1]} <p> {saber_algo} </p>',
    "3", f'{curiosidadesCopa.array_curiosidades[2]} <p> {saber_algo} </p>', 
    "4", f'{curiosidadesCopa.array_curiosidades[3]} <p> {saber_algo} </p>', 
    "5", f'{curiosidadesCopa.array_curiosidades[4]} <p> {saber_algo} </p>', 
    "quando o brasil foi campeao?", f'{curiosidadesCopa.brasil_campeao} <p> {saber_algo} </p> ',
    "onde o brasil foi campeao?", f'{curiosidadesCopa.brasil_campeao} <p> {saber_algo} </p> ',
    # informações sobre os jogadores
    "sobre os jogadores", f'<h5>Para escolher uma curiosidade digite a letra referente</h5> <ol type="I"> <li>{curiosidadesJogadores.array_jogadores_titulos[0]}</li> <li>{curiosidadesJogadores.array_jogadores_titulos[1]}</li> <li> {curiosidadesJogadores.array_jogadores_titulos[2]} </li> <li> {curiosidadesJogadores.array_jogadores_titulos[3]} </li> </ol>',
    f'i', f'{curiosidadesJogadores.array_informacoes[0]} <p> {saber_algo} </p>',
    "ii", f'{curiosidadesJogadores.array_informacoes[1]} <p> {saber_algo} </p>',
    "iii", f'{curiosidadesJogadores.array_informacoes[2]} <p> {saber_algo} </p>',
    "iv", f'{curiosidadesJogadores.array_informacoes[3]} <p> {saber_algo} </p>', 
    # informações em tempo real
    'informacoes',f'{tempoReal.informacoes_tempo_real} <p> {saber_algo} </p>'
    'informacoes em tempo real',f'{tempoReal.informacoes_tempo_real} <p> {saber_algo} </p>',
    "sera que o brasil ganha a copa esse ano?", "Claro que ganha, vamos torcer pelo melhor",
    "porque gabigol nao foi a copa?", f'{curiosidadesJogadores.gabigol_copa} <p> {saber_algo} </p>',
    "Messi", f'{curiosidadesJogadores.messi_info} <p> {saber_algo} </p>',
    "neymar", f'{curiosidadesJogadores.neymar_info} <p> {saber_algo} </p>',
    "nao", "Obrigado pelo seu tempo, quando quiser saber mais curiosidades sobre a copa é só chamar! 😃"
    
])

# <li></li>