<h1>Compressor e Descompressor usando algoritmo LZW</h1> 
<p>&nbsp;&nbsp;&nbsp; Giovanni Bruno Travassos de Carvalho - 11506849</p>
<p>&nbsp;&nbsp;&nbsp; Jordan Elias Rodrigues - 11516379 </p>
<p>&nbsp;&nbsp;&nbsp; Kaio Moura dos Santos - 11506860 </p>
<p><b>UFPB - Introdução à Teoria da Informação</b></p>
<p><b>Professor: Derzu Omaia</b></p>
<p>Este trabalho tem como objetivo implementar um compressor e descompressor utilizando o algoritmo LZW com dicionário de tamanho variável. O LZW é um algoritmo contextual (probabilidade de um símbolo é calculada de acordo com outros eventos) e adaptativo (probabilidade muda a cada símbolo) de codificação baseado em dicionário, cuja ideia principal é construir um dicionário de símbolos ou palavras conforme o texto ou a informações que vai sendo processado.</p>
<p>Codificadores baseados em dicionários fazem a codificação sempre referenciando partes da mensagem que já aconteceram no passado. No início da codificação de um texto (ou imagem/vídeo), o dicionário inicial do LZW recebe os 256 caracteres da tabela ASCII, ou, no caso de imagem/vídeo, a quantidade de tons que compõem a paleta de cores (0 a 255).</p>

<h2> Sumário </h2> 
<ol>
	<li><a href="https://github.com/GiovanniBru/CompressorLZW/blob/main/README.md#desenvolvimento">Desenvolvimento</a></li>
	<li><a href="https://github.com/GiovanniBru/CompressorLZW#compress%C3%A3o">Compressão</a></li>
	<li><a href="https://github.com/GiovanniBru/CompressorLZW#descompress%C3%A3o">Descompressão</a></li>
	<li><a href="https://github.com/GiovanniBru/CompressorLZW#resultados-obtidos">Resultados Obtidos</a></li>
	<li><a href="https://github.com/GiovanniBru/CompressorLZW#conclus%C3%A3o">Conclusão</a></li>
	<li><a href="https://github.com/GiovanniBru/CompressorLZW#refer%C3%AAncias">Referências</a></li>
</ol>

<h2>Desenvolvimento</h2>
<p>A implementação deste projeto foi feita utilizando a linguagem Python e a IDE Replit, que nos permitiu desenvolver em conjunto pelo navegador. Os testes foram rodados na IDE  Spyder Anaconda, pois o Replit não comportava arquivos tão grandes, utilizando arquivos de texto menores para debugar e os arquivos solicitados pelo professor (‘corpus16MB.txt’ e ‘discorigido.mp4’).</p>
<p>Foi solicitado testes com diferentes tamanhos de contexto K bits, de 9 a 16, esse parâmetro define o tamanho máximo do dicionário, onde um contexto K =9 tem dicionário de tamanho 29= 512. As primeiras funções criadas foram de escolha do arquivo a ser compresso ‘chooseArq()’, e escolha do tamanho de K ‘switchK()’.</p>

<h2>Compressão</h2>
<p>Após ler o arquivo é preciso fazer a compressão. Iniciamos o dicionário com os 256 caracteres da tabela ASCII que será o nosso alfabeto e, durante a análise do conteúdo do arquivo, é adicionado novas palavras no dicionário a partir de combinações de dois caracteres ou mais. A função ‘Compress()’ recebe os dados e o contexto K e retorna os dados codificados como uma lista de índices.</p>
<p>A saída do compressor é uma lista com todos os índices inteiros, referentes ao dicionário criado, dos caracteres do arquivo. Para computar o número de índices, bastou utilizar a função len() passando os dados comprimidos. </p>
<p>Depois de feita a compressão precisamos converter os índices para binário, para que assim possamos salvar o arquivo binário e, posteriormente, enviá-lo para descompressão. Isso é feito na função ‘convertBinary()’, que recebe os dados que saíram do compressor e o valor do contexto K. Nessa função usando ‘bin(elem)[2:].zfill(K)’ transformaremos cada valor de índice em binário de K bits, preenchendo os valores com 0 caso precise, por exemplo um índice 4 que seria 100 em binário, para um contexto de tamanho 9, passará a ser 000000100.</p>

<h2>Descompressão</h2> 
<p>O descompressor foi feito de maneira simples, percorrendo os dados comprimidos, criando um novo dicionário do zero, da mesma maneira que o compressor, iniciando-o com os 256 caracteres da tabela ASCII e atribuindo a chave à lista de dados descomprimidos. A função criada recebe os dados comprimidos e retorna eles descomprimidos. </p>

<h2>Resultados Obtidos</h2> 
<p>O arquivo de texto ‘corpus16MB.txt’ originalmente possui tamanho de 15.272 KB, e o arquivo ‘discorigido.mp4’ originalmente possui tamanho de 2.062 KB. Colocamos os dados no Excel para gerar os gráficos. Abaixo segue os resultados obtidos para todos os contextos solicitados.</p> 
<p align="center"><img src = "https://github.com/GiovanniBru/CompressorLZW/blob/main/images/Figura1.PNG"></p>
<p align="center">Figura 1 - Número de índices obtidos para cada K</p>
<p>O gráfico da Figura 1 mostra o número de índices obtidos para ambos os arquivos solicitados, dado todos os sete valores de K. Podemos observar que, para os dois arquivos, o número de índices aumenta conforme o contexto diminui, pois, quanto maior o tamanho do contexto, maior é o espaço disponível no dicionário para se criar novas combinações de símbolos e não existe a necessidade de uma maior quantidade de índices. </p>
<p align="center"><img src = "https://github.com/GiovanniBru/CompressorLZW/blob/main/images/Figura2.PNG"></p>
<p align="center">Figura 2 - Tamanho do arquivo comprimido para cada K</p>
<p>O gráfico da Figura 2 relaciona o tamanho dos arquivos comprimidos e os diferentes valores de contexto. Relembrando que os arquivos de texto e vídeo possuem 15.271 KB e 2.062 KB respectivamente, observa-se que para o vídeo, ao aumentar o contexto, o tamanho do arquivo comprimido diminui, como esperado. Já para o vídeo, o tamanho aumenta até K = 13 e depois começa a diminuir conforme o contexto aumenta. </p>
<p>Tendo o tamanho dos arquivos comprimidos e sabendo o tamanho do arquivo original, podemos calcular a Razão de Compressão (RC) através da fórmula: Razão de Compressão = Comprimento Sem Compressão / Comprimento com Compressão. </p>
<p align="center"><img src = "https://github.com/GiovanniBru/CompressorLZW/blob/main/images/Figura3.PNG"></p>
<p align="center">Figura 3 - Razão de Compressão para cada K</p>
<p>A Razão de Compressão é uma medida para calcular a eficácia do algoritmo, ela nos dá uma relação de X:1 onde X é o valor de RC que nos diz que X MB da mensagem passa para 1 MB, ou seja, quanto maior a Razão de Compressão melhor é o algoritmo. </p>
<p>Dito isso, como a Razão de Compressão é proporcional ao tamanho do arquivo comprimido, as mesmas conclusões feitas para Figura 2 são válidas para Figura 3.</p>
<p align="center"><img src = "https://github.com/GiovanniBru/CompressorLZW/blob/main/images/Figura4.PNG"></p>
<p align="center">Figura 4 - Tempo de compressão para cada K</p>
<p>O gráfico da Figura 4 mostra o tempo de execução da compressão dos arquivos de texto e vídeo para cada K solicitado. Podemos observar que para o arquivo de texto o tempo se manteve crescente até K = 12, depois voltando a ser crescente, sendo para K = 16 mais de uma hora de execução. Já para o arquivo de vídeo o tempo se manteve sempre crescente, e para K = 16 o tempo foi muito maior, sendo mais de uma hora de execução. </p>

<h2>Conclusão</h2> 
<p>O algoritmo criado comprime e descomprime os arquivos, mas com tempo de execução muito elevado, sendo maior que uma hora para contextos grandes. O algoritmo se mostrou bastante eficaz para o texto, comprimindo independentemente do tamanho do contexto. Porém, para o vídeo, a compressão não foi boa. Entretanto o algoritmo se mostrou bastante eficaz no quesito descompressão, pois, até mesmo para o vídeo e outras imagens testadas, o arquivo volta a ser exatamente igual ao que era antes.</p> 

<h2>Referências</h2> 
<p>1 -  GEEKS FOR GEEKS. LZW (Lempel-Ziv-Welch) Compression technique. Disponível em: https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/. Acesso em: 16 mai. 2021.</p>
<p>2 -  DIGITAL SIGNAL PROCESSING GUIDE. LZW Compression. Disponível em: https://www.dspguide.com/ch27/5.html. Acesso em: 17 mai. 2021.</p>
<p>3 - DELFTSTACK. Como Converter Int em Bytes em Python 2 e Python 3. Disponível em: https://www.delftstack.com/pt/howto/python/how-to-convert-int-to-bytes-in-python-2-and-python-3/. Acesso em: 17 mai. 2021.</p>
<p>4 - PYTHON.ORG. Built-in Types. Disponível em: https://docs.python.org/3/library/stdtypes.html. Acesso em: 18 mai. 2021.</p>
<p>5 - PYTHON REFERENCE. Zfill. Disponível em: https://python-reference.readthedocs.io/en/latest/docs/str/zfill.html. Acesso em: 18 mai. 2021. </p>

