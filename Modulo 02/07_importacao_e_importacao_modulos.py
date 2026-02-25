#Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas.
#A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente.

#Importação de um módulo
import math  # Importa o módulo math, que contém funções matemáticas

resultado = math.sqrt(16)  # Usa a função sqrt do módulo math para calcular a raiz quadrada de 16
print(resultado)  # Imprime o resultado, que é 4.0

#importando apenas uma função específica de um módulo
from math import sqrt  # Importa apenas a função sqrt do módulo math

resultado = sqrt(25)  # Usa a função sqrt diretamente, sem precisar do prefixo math
print(resultado)  # Imprime o resultado, que é 5.0

#funcoes e classes de modulos padrão
#random: módulo para gerar números aleatórios
#datetime: módulo para trabalhar com datas e horas
#os: módulo para interagir com o sistema operacional

import random
import datetime

numero_aleatorio = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
print(f"Número aleatório gerado: {numero_aleatorio}")

data_atual = datetime.datetime.now()  # Obtém a data e hora atual
print(f"Data e hora atual: {data_atual}")

