# Links referência
url = 'https://br.bolavip.com/futebol/Grandes-nomes-do-futebol-que-podem-jogar-sua-ultima-Copa-do-Mundo-no-Qatar-2022-20221108-0103.html'

estado_minas = 'https://www.em.com.br/app/noticia/empresas/2022/11/24/interna-empresas,1425226/quem-sao-os-favoritos-para-a-copa-do-mundo-de-2022-confira-as-apostas.shtml'

brasil_escola = 'https://brasilescola.uol.com.br/educacao-fisica/primeira-copa-mundo.htm'
pais_penta_link = f'https://brasilescola.uol.com.br/curiosidades/curiosidades-brasil-copas-mundo.htm#:~:text=Ali%C3%A1s%2C%20o%20Brasil%20%C3%A9%20o,%2C%201970%2C%201994%20e%202002.'
mais_titulos_link = 'https://cultura.uol.com.br/esporte/noticias/2022/02/03/2610_paises-com-mais-titulos-na-copa-do-mundo.html'

# fim links

# Títulos das informações
titulo_ultima_copa = "Jogadores que podem estar jogando sua última copa do mundo em 2022"

titulo_times_favoritos = "Quais são os times favoritos da copa de 2022"

titulo_primeira_copa = "Quando e onde aconteceu a primeira copa do mundo?"
pais_penta_titulo = "O Brasil é o único país que participou de todas as copas do mundo já organizadas!"
quantidade_titulos = "Países com mais títulos na Copa do Mundo"
# Array de titulos para serem usados la lista do bot
array_titulos = [titulo_ultima_copa, titulo_times_favoritos, titulo_primeira_copa, pais_penta_titulo, quantidade_titulos]

# fim títulos


ultima_copa = (f'<h4> {titulo_ultima_copa} </h4> <p>Alguns crackes do futebol devem se despedir da copa do mundo em 2022 devido sua idade.</p> <p>Dentre eles estão: <strong>Cristiano Ronaldo</strong>, <strong>Messi</strong>,<strong> Thiago Silva</strong> e <strong>Daniel Alves</strong>. Confira a matéria completa no site do BolaVip no <a href="{url}" target="_blank">link</a></p>')

times_favoritos = (f'<h4> {titulo_times_favoritos} </h4><p>Confira o ranking:</p> <ol> <li>Brasil</li> <li>Argentina</li> <li>França</li> <li>Bélgica</li> <li>Alemanha</li> </ol> <p>Saiba mais nessa matéria do <a href="{estado_minas}">Estado de Minas</a> </p>')

primeira_copa=(f'<h4> {titulo_primeira_copa} </h4> <p>A primeira copa do mundo foi realizada no Uruguai em 1930, apenas 13 seleções participaram dessa copa e o Uruguai foi o campeão após a vitória contra a Argentina.</p> <p>Confira mais nessa matéria do <a href="{brasil_escola}" target="_blank"> Brasil Escola</a> </p>')

pais_penta = (f'<h4>{pais_penta_titulo}</h4> <p>A primeira copa do mundo aconteceu em 1930 e teve a participação de apenas 13 países, dentre eles estava o nosso Brasil.</p> <p>O Brasil também possui a marca de ser o único país Penta Campeão, os títulos foram conquistados respectivamente em 1958, 1962, 1970, 1994 e 2002 </p> <p>Saiba mais em <a href="{pais_penta_link}" target="_blank">Brasil Escola </a> </p> ')

paises_com_mais_titulos = (f'<h4> {quantidade_titulos} </h4> <p>O Brasil é a nação que possuí a maior quantidade de títulos, sendo um total de 5, conquistados em 1958, 1962, 1970, 1994 e 2002 </p> <p>Em seguida temos a Alemanha com 4 títulos, a itália também com 4 títulos, a Argentina, a França e o Uruguai com dois títulos e Espanha e Inglaterra com apenas um título cada uma</p> <p> Saiba mais detalhes em <a href="{mais_titulos_link}" target="_blank">Uol </a> </p>')

brasil_campeao = (f'<p>O Brasil foi campeão nas seguintes copas do Mundo em 1958 que foi sediada na Suécia, em 1962 no Chile , em 1970 no México, em 1994 EUA e em 2002 no Japão e Coreia do Sul </p>')

# Array contendo todas as variáveis
array_curiosidades = [ultima_copa, times_favoritos, primeira_copa, pais_penta, paises_com_mais_titulos]
