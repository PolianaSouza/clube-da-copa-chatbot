# links referência
link_messi = 'https://ge.globo.com/futebol/selecoes/argentina/noticia/2022/11/26/messi-iguala-maradona-e-chega-a-21-jogos-em-copas-pela-argentina.ghtml'

neymar_brinde = 'https://esportes.r7.com/prisma/cosme-rimoli/jogadores-decidem-blindar-neymar-que-luta-para-voltar-para-a-copa-raphinha-se-excede-e-ataca-internautas-26112022'

espn = 'https://www.espn.com.br/futebol/copa-do-mundo/artigo/_/id/11236047/ranking-os-50-melhores-jogadores-da-copa-do-mundo-do-qatar'

# fim links

# tags sendo usadas
# <h4> </h4>
# <p> </p>
# <a href="{}" target="_blank"> </a>
# <strong> </strong>

# Títulos das postagens
messi_titulo = "Messi, Maradona, 21jogos e 8 gols?"
neymar_titulo = "Jogadores blindam Neymar"
melhores_titulo = "Melhores jogadores do mundo participando da copa de 2022"
# fim

# Array para listar os titulos
array_jogadores_titulos = [messi_titulo, neymar_titulo, melhores_titulo]
# 

messi = (f'<h4> {messi_titulo} </h4> <p> Messi iguala marcas do seu ídolo Maradona, chegando a 21 jogos e 8 gols </p> <p>Saiba mais nessa reportagem do <a href="{link_messi}" target="_blank"> globo.com </a> </p>')

neymar = (f'<h4> {neymar_titulo} </h4> <p>Jogadores decidem blindar Neymar que lutra para voltar para a copa.</p><p>veja na matéria do <a href="{neymar_brinde}"> R7</a></p>')

melhores_jogadores = (f'<h4> {melhores_titulo} </h4> <p>Vamos concordar que pra estar na copa tem que ser os melhores né? mas o site ESPN listou os 50 melhores jogadores do mundo, dentre eles estão: <strong>Kylian Mbappé</strong> da França, <strong>Lionel Messi</strong> da Argentina, <strong>Neymar</strong> do Brasil e <strong>Vinicius Jr</strong> também do Brasil. </p> <p>Ficou curioso pra saber quem são os outros né? confira <a href="{espn}" target="_blank"> nessa matéria do site ESPN</a></p>')

# Array para listar as informações
array_informacoes = [messi, neymar, melhores_jogadores]