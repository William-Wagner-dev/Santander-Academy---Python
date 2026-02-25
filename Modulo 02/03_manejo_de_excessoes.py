#exemplos de manejo de excessoes

try:
    #codigo que pode gerar uma excessao
    resultado = 10 / 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    #codigo para lidar com a excessao
    print("Erro: Divisão por zero não é permitida.")

#exemplo com except para tratar mais de um tipo de excessao
try:
    #codigo que pode gerar uma excessao
    resultado = 10 / 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Valor inválido.")


#exemplo com finally para garantir que um bloco de codigo seja executado independentemente de uma excessao ocorrer ou nao

try:
    #codigo que pode gerar uma excessao
    arquivo = open("arquivo_inexistente.txt", "r")
    #realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    arquivo.close() #garante que o arquivo seja fechado mesmo que ocorra uma excessao
    