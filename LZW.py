# -*- coding: utf-8 -*-

from classes import switchK, Decompress, chooseArq, convertBinary, Compress 
import time 

print("Qual arquivo deseja comprimir?")
print("1 - Arquivo de texto")
print("2 - Arquivo de vídeo")

archive, output = chooseArq()
print(output)
file = open(archive, "rb") 
data = file.read()

print("Qual o tamanho do contexto K desejado? Escolha um número de 9 a 16")
K = switchK()

print("Começando a Compressão")
start1 = time.time()
DataCod = Compress(data, K)
DataBin = convertBinary(DataCod, K)

fileCompressed = open("Compressed.bin", "wb")
fileCompressed.write(DataBin)

end1 = time.time()
print("O tempo de demora para execução do Compressor foi: " + str(end1 - start1))

print("O número de índices para o contexto " + str(K) + " foi de " + str(len(DataCod)) )

print("Começando a Descompressão")
start2 = time.time()
DataDecod = Decompress(DataCod)

fileDecompressed = open(output, "wb")
output_decod = b''
for x in DataDecod: 
    output_decod += x
fileDecompressed.write(output_decod)
fileDecompressed.close

end2 = time.time()
print("O tempo de demora para execução do Descompressor foi: " + str(end2 - start2))

