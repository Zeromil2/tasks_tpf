# RESOLUÇÕES: PASSO-A-PASSO
Aqui estarei explicando qual a lógica por trás dos algoritmos utilizados, assim como bibliotecas e módulos importados.
A ordem da explicação será dada conforme a ordem que as tasks foram feitas, indo da maís fácil para mais difícil.
# Problema_02
Esta questão apresentou ser a mais fácil entre as que foram dadas, visto que era apenas necessário ler um arquivo txt e informar qual número faltava dentro daquela sequência.

Um comando que vai aparecer tanto nessa, quanto nas outras questões, é o "ROOT_PATH = Path(__file__).parent", que é um comando da biblioteca pathlib, que permite capturar o arquivo dentro da pasta desejada, sem ter que precisar se preocupar diretamente na localização nativa do arquivo em sua máquina.

Além disso, outro comportamento comum nas outras tasks é a manipulação segura de arquivos (através do comando "with open()"), juntamente com o tratamento de exceções(utilizando try e except).

Por fim, nesta task foi utilizado list comprehension para armazenar a sequencia do arquivo txt dentro de uma lista, e logo em seguida foi realizada uma iteração nesta lista para descobrir qual o número que faltava.

# Problema_03
Além dos comportamentos já vistos na task anterior, nesta task e na seguinte eu optei por modularizar o arquivo em funções, de modo a criar uma função específica que permita iterar pela lista e retornar a maior sequência contínua, assim como o seu respectivo valor.

# Problema_01
Foi de longe a task mais difícil entre as que foram apresentadas, devido a utilização da API viacep, o que me fez demorar um pouco a entender como ela funciona, mas com o auxílio da documentação, assim como comentários no stackoverflow e repositórios do Github e ChatGPT, foi possível assimilar o assunto e resolver a task.

Nela também foi necessária realizar a importação de algumas bibliotecas, como: requests (para realizar a requisição HTTP) e pandas (para construir o dataframe).

Primeiramente, foi realizada a leitura do arquivo contendo os CEPs, sendo eles armazenados em uma lista. Nisto, foi realizada uma consulta em cada um deles através da função "consultar_cep()".

Nesta função, primeiramente era realizado o preenchimento da url_base da API da viacep com o CEP analisado, para logo em seguida identificar se a resposta HTTP foi igual a 200 (significando que houve um OK como resposta).

Em caso afirmativo, foram coletadas as informações do arquivo json que foi transformado em um dicionário, e logo em seguida retornado e adicionado a lista que contém os dicionários com os dados de cada um dos CEPs. Em caso negativo, os dados possuem a informação 'indisponível'.

Por fim, esta lista com os dicionários que contém os dados dos CEPs foi transformada em um dataframe, e logo em seguida escrita num arquivo em formato .csv
