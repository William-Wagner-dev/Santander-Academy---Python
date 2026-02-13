"""Os loops nos permitem repetir um bloco de código várias vezes. Em Python, os loops mais comuns são for e while.

 For
O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável.
A sintaxe básica é a seguinte:

for variável in sequência:

    # Bloco de código a repetir
    instruções"""
 
 #exemplo:

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

"""While
O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:
while condição:

    # Bloco de código a repetir
    instruções"""

contador = 0

while contador < 5:

    print(contador)
    contador += 1

#Controle de loops

"""Break
A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição.
Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.
Exemplo:"""

contador = 0

while True:

    print(contador)
    contador += 1


    if contador == 5:
        break

"""Continue
A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.
Exemplo:"""

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

"""Pass
A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente
necessária, mas nenhuma ação é desejada.
Exemplo:"""

for i in range(5):
    pass
