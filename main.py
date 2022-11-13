# Essa será a primeira página
import os
import conversa

def processar_resposta(retorno):
    if(retorno == '1'):
        print(f"{os.linesep}Os horários dos jogos")
    elif(retorno == '2'):
        print(f"{os.linesep}Você quer saber sobre as curiosidades da copa do mundo")
    elif(retorno == '3'):
        print(f"{os.linesep}Informações sobre todos os jogadores da copa de 2022")
    elif(retorno == '4'):
        print(f"{os.linesep}O que aconteceu nas copas anteriores?")
    elif(retorno == '5'):
        print(f"{os.linesep}Conversando com amigo sobre a copa")
        conversa
    else:
        print(f"{os.linesep}Escolha uma opção")

def start():
    print("Olá! Bem vindo ao clube da copa 2022")
    print("Aqui você fica por dentro de todas as novidades sobre a copa do mundo!")
    while True:
        retorno = input(f"Escolha uma opção: {os.linesep}"
                         f"[1] - Horários dos Jogos{os.linesep}"
                         f"[2] - Curiosidades sobre a copa de 2022{os.linesep}"
                         f"[3] - informações sobre os jogadores{os.linesep}"
                         f"[4] - Curiosidades sobre as copas anteriores{os.linesep}"
                         f"[5] - Vamos conversar sobre a copa?{os.linesep}")
        processar_resposta(retorno)

if __name__ == '__main__':
    start()





