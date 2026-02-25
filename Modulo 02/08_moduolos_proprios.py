#Além de utilizar os módulos padrão do Python, também podemos criar nossos próprios módulos para organizar e reutilizar nosso código.

#meu_modulo.py
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao meu módulo.")

def calcular_soma(a, b):
    return a + b

#depois podemos importar nosso módulo e usar suas funções

import meu_modulo
meu_modulo.saudacao("William")  # Saída: Olá, William! Bem-vindo ao meu módulo.
resultado = meu_modulo.calcular_soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")  # Saída
# A soma de 5 e 3 é: 8

#Também podemos importar funções específicas do módulo
from meu_modulo import saudacao
saudacao("Maria")  # Saída: Olá, Maria! Bem-vindo ao meu módulo.
#Ou importar todas as funções do módulo
from meu_modulo import *
calcular_soma(10, 20)  # Saída: 30

#Organização do codigo em modulos é uma prática recomendada para manter o código limpo, modular e fácil de manter.

# operacoes.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

# utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)

def obter_nome_usuario():
    return input("Digite seu nome: ")

#importando os módulos
import operacoes
import utilidades

resultado_soma = operacoes.somar(5, 7)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado_soma}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}! Bem-vindo ao nosso programa.")
