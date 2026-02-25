def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media
# Exemplo de uso da função

print("Media:", calcular_media (10, 20, 30, 40, 50))

def somar_3(x):
    return x + 3
# Exemplo de uso da função

somar = lambda x: x + 3
print("Somar 3 a algum numero:", somar(5))

#documentacao de funcoes
def area_retangulo(base, altura):
    """Calcula a área de um retângulo.

    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.

    Returns:
        float: A área do retângulo.
    """
    return base * altura

#funcoes com numeros variaveis de argumentos
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        return total
    print(soma_variavel(1, 2, 3, 4, 5))
    print(soma_variavel(10, 20, 30))

    