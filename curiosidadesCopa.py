import os

def curiosidades_copa22():
    print("Curiosidades sobre a copa de 2022")

# Links referência
url = 'https://br.bolavip.com/futebol/Grandes-nomes-do-futebol-que-podem-jogar-sua-ultima-Copa-do-Mundo-no-Qatar-2022-20221108-0103.html'

estado_minas = 'https://www.em.com.br/app/noticia/empresas/2022/11/24/interna-empresas,1425226/quem-sao-os-favoritos-para-a-copa-do-mundo-de-2022-confira-as-apostas.shtml'

brasil_escola = 'https://brasilescola.uol.com.br/educacao-fisica/primeira-copa-mundo.htm'

# fim links
# Títulos das informações
titulo_ultima_copa = "Jogadores que podem estar jogando sua última copa do mundo em 2022"

titulo_times_favoritos = "Quais são os times favoritos da copa de 2022"

titulo_primeira_copa = "Quando e onde aconteceu a primeira copa do mundo?"

# Array de titulos para serem usados la lista do bot
array_titulos = [titulo_ultima_copa, titulo_times_favoritos, titulo_primeira_copa]

# fim títulos

ultima_copa = (f'<h4 style="color:red"> {titulo_ultima_copa} </h4> <p>Alguns crackes do futebol devem se despedir da copa do mundo em 2022 devido sua idade.</p> <p>Dentre eles estão: <strong>Cristiano Ronaldo</strong>, <strong>Messi</strong>,<strong> Thiago Silva</strong> e <strong>Daniel Alves</strong>. Confira a matéria completa no site do BolaVip no <a href="{url}" target="_blank">link</a></p>')

times_favoritos = (f'<h4> {titulo_times_favoritos} </h4><p>Confira o ranking:</p> <ol> <li>Brasil</li> <li>Argentina</li> <li>França</li> <li>Bélgica</li> <li>Alemanha</li> </ol> <p>Saiba mais nessa matéria do <a href="{estado_minas}">Estado de Minas</a> </p>')

primeira_copa=(f'<h4> {titulo_primeira_copa} </h4> <p>A primeira copa do mundo foi realizada no Uruguai em 1930, apenas 13 seleções participaram dessa copa e o Uruguai foi o campeão após a vitória contra a Argentina.</p> <p>Confira mais nessa matéria do <a href="{brasil_escola}"> Brasil Escola</a> </p>')

array_curiosidades = [ultima_copa, times_favoritos, primeira_copa]
