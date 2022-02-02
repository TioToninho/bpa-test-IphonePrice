# Teste para desenvolvedor Jr. Python

## Candidato: Antonio Moura

### objetivo: Abrir o site da Amazon, pesquisar por  iphone, pegar os resultados da primeira página (nome e preço) e criar uma planilha Excel com esses dados

### Projeto

O programa inicia chamando a ***função main***, de onde é realizada e chamada todas as ações do projeto.
Dentro da ***função main*** chamamos da ***função get_html*** que vai abrir o navegador, entrar no site da Amazon, entrar na página de pesquisa sobre 'iphone' e salvar o html da página, após isso ela vai passar o html da página como argumento para a ***biblioteca BeautifulSoup*** que vai filtrar toda a página html para então só sobrar os cards dos anúncios que precisamos.

Após termos todos os cards da página, chamamos outra função, a ***format_data***. Ela vai pegar todos os cards e chamar outra função, a ***scrape_data***, dentro dela ela vai criar um dicionario com todos os produtos, organizando por Titulo do anúncio e Preço. Após isso ela retorna o dicionario para a ***função format_data*** que vai anexar tudo em uma lista.

Quando já temos todas as informações anteriores, vamos para a última etapa, que é escrever as informações em um arquivo excel. Então passamos as informações da função anterior para a ***função write_csv***, ao entrar nessa função, vamos criar um arquivo csv onde de primeira vai ser escritos todas aquelas informações que estavam na lista, após isso vamos transformar esse arquivo csv em um xlsx para melhor visualização dos dados.

Após essas etapas será concluído o fluxo do programa.

Nesse repositório temos o arquivo ***main.py*** onde está todo o código usado e temos também um ***arquivo xlsx*** de exemplo do que o programa gera.

Esse projeto poderia ter sido feito de várias maneiras e usando diversas tecnologias, utilizei selenium e BeautifulSoup pois é o que tenho mais facilidade, mas reconheço que poderia ter usado scrapy e outra ferramentas para fazer scraping com python.
