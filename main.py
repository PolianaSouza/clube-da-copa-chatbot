# Essa será a primeira página
import os
import horarioJogos
import curiosidades
import copasAnteriores
import jogadores
# import conversa
#Está dando bug se executar com a conversa ativada

def processar_resposta(retorno):
    if(retorno == '1'):
        print(f"{os.linesep}Os horários dos jogos do")
        horarioJogos.todos_jogos()
        horarioJogos.jogos_brasil()
        tentar_novamente()
    elif(retorno == '2'):
        print(f"{os.linesep}Você quer saber sobre as curiosidades da copa do mundo de 2022")
        curiosidades.curiosidades_copa22()
        curiosidades.jogando_ultima_copa()
        tentar_novamente()
    elif(retorno == '3'):
        print(f"{os.linesep}Informações sobre todos os jogadores da copa de 2022")
        jogadores.info_jogadores()
        tentar_novamente()
    elif(retorno == '4'):
        print(f"{os.linesep}O que aconteceu nas copas anteriores?")
        copasAnteriores.copas_anteriores()
        tentar_novamente()
    elif(retorno == '5'):
        print(f"{os.linesep}Conversando com amigo sobre a copa")
        # conversa.bot
        tentar_novamente()
    else:
        print(f"{os.linesep}Escolha uma opção")

def start():
    print("Olá! Bem vindo ao clube da copa 2022")
    print("Aqui você fica por dentro de todas as novidades sobre a copa do mundo!")
    # while True:
    retorno = input(f"Escolha uma opção: {os.linesep}"
             f"[1] - Horários dos Jogos{os.linesep}"
             f"[2] - Curiosidades sobre a copa de 2022{os.linesep}"
             f"[3] - informações sobre os jogadores{os.linesep}"
             f"[4] - Curiosidades sobre as copas anteriores{os.linesep}"
             f"[5] - Vamos conversar sobre a copa?{os.linesep}"
            f"Resposta: ")
    processar_resposta(retorno)

def tentar_novamente():
    while True:
        pergunta = input(f"Tentar novamente? {os.linesep}")
        if (pergunta == "sim"):
            start()
        else:
            print("Obrigado por usar nossos serviços")
        break

if __name__ == '__main__':
    start()





