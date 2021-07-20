# -*- coding: utf-8 -*-

def chooseArq():    # Função que escolhe o arquivo para comprimir
    option = int(input())

    if option == 1:
      file = "corpus16MB.txt"
      output = "Decompressed.txt"
    elif option == 2: 
      file = "discorigido.mp4"
      output = "Decompressed.mp4"
    else: 
      return print("Opção inválida")
    
    print("A opção escolhida foi: " + str(file))
  
    return file, output

def switchK():  # Função que escolhe o tamanho do contexto K 
    option = int(input())

    if option == 9: 
      k = 9
    elif option == 10:
      k = 10
    elif option == 11:
      k = 11
    elif option == 12:
      k = 12
    elif option == 13:
      k = 13
    elif option == 14:
      k = 14
    elif option == 15:
      k = 15
    elif option == 16:
      k = 16
    else: 
      return print("Opção inválida")

    print("A opção escolhida foi um contexto de tamanho " + str(k))  
    return k

def Compress(Data,K): # Função de Compressão 
    sizeDict = 256     
    alphabet = {}
    
    for i in range(sizeDict): # Inicializa dicionário com tabela ASCII
        alphabet[i] = bytes([ord(chr(i))])
        
    alphabet = list(alphabet.values())
    Dictionary = alphabet.copy()

    bin = [] 
    str_bit = b''   # Vetor de bytes 
    index = 0
    aux = 0
    
    while(index < len(Data)): # Percorre todos os dados
        
        if Data[aux:index+1] in Dictionary:  # Se a palavra já está no Dicionário
            str_bit = str_bit + alphabet[Data[index]]
            index +=1

        else:   # Se a palavra não está no dicionário 
            if(len(Dictionary) < 2**K-1): # Se o dicionário tiver espaço 
                Dictionary.append((str_bit + alphabet[Data[index]]))

            bin.append(Dictionary.index(str_bit))
            str_bit = b''
            aux = index 
            
    if(str_bit != b''):
        bin.append(Dictionary.index(str_bit))
        Dictionary.append((str_bit + 'EOF'.encode()))
    
    return bin

def Decompress(bin):
    sizeDict = 256     
    alphabet = {}
    
    for i in range(sizeDict): # Inicializa dicionário com tabela ASCII
        alphabet[i] = bytes([ord(chr(i))])
    alphabet = list(alphabet.values())

    Dictionary = alphabet.copy()  # Dicionário inicia com a tabela ASCII 
    DataDecomp = []
    index = 0
 
    while (index < len(bin)):

        if(index == 0):
            Dictionary.append(Dictionary[bin[index]])

        else:
            Dictionary[len(Dictionary)-1] = Dictionary[bin[index-1]] + alphabet[Dictionary[bin[index]][0]]
            Dictionary.append(Dictionary[bin[index]])

        DataDecomp.append(Dictionary[bin[index]])
 
        index += 1
 
    Dictionary[len(Dictionary)-1] = (Dictionary[len(Dictionary) -1] + 'EOF'.encode())

    return DataDecomp

def convertBinary(DataCod, K):
    DataBin = ''
 
    for x in DataCod:
        DataBin += (bin(x)[2:].zfill(K))
            # zfill = adiciona zeros no início da string até atingir comprimento especificado (K)
 
    bitsTotal = len(DataBin)
    bytesTotal = 0
 
    if ((bitsTotal % 8) == 0): 
        bytesTotal = int(bitsTotal / 8)
    else:
        bytesTotal = int(bitsTotal / 8) + 1
 
    trash = ''
    for i in range(bytesTotal * 8 - bitsTotal):
        trash += '0'
        
    DataBin = int(DataBin + trash, 2).to_bytes(bytesTotal, 'big')
          # big = ordem dos bytes, o byte mais significativo estará no início da matriz 

    return DataBin