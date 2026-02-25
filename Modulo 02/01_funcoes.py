#definição e chamada de uma função simples em Python
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao() #aparece a mensagem "Olá, seja bem-vindo!" na tela.

# Parametros e argumentos
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")
saudacao("Maria") #aparece a mensagem "Olá, Maria! Seja bem-vindo!" na tela.
saudacao("João") #aparece a mensagem "Olá, João! Seja bem-vindo!" na tela.

#valores de retorno
def soma(a, b):
    return a + b
resultado = soma(5, 3)
print(resultado) #aparece o valor 8 na tela.

#funções anonimas (lambda)
quadrado = lambda x: x ** 2
print(quadrado(5)) #aparece o valor 25 na tela.

#escopo de variaveis (global e local)
def funcao():
    variavel_local = 10
    print(variavel_local) #Acessível dentro da função.

variavel_global = 20

def funcao2():
    print(variavel_global) #Acessível dentro da função.

funcao() #aparece o valor 10 na tela.
funcao2() #aparece o valor 20 na tela.
print(variavel_global) #aparece o valor 20 na tela.
print(variavel_local) #gera um erro, pois variavel_local não é acessível fora da função.