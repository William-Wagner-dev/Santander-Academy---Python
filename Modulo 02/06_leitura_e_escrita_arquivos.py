#Leitura de Arquivos
arquivo = open("exemplo.txt", "r")  # Abre o arquivo para leitura
conteudo = arquivo.read()  # Lê o conteúdo do arquivo
print(conteudo)  # Imprime o conteúdo do arquivo
arquivo.close()  # Fecha o arquivo

#Escrita de Arquivos
arquivo = open("exemplo.txt", "w")  # Abre o arquivo para escrita (sobrescreve o conteúdo)
arquivo.write("Olá, este é um exemplo de escrita em um arquivo.")  # Escreve uma linha no arquivo
arquivo.close()  # Fecha o arquivo

#declaração de with para leitura de arquivos
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
#declaração de with para escrita de arquivos