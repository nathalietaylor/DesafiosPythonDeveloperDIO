# Desafio
# Construa um programa para verificar, à partir de dois valores muito grandes A e B,
# se B corresponde aos últimos dígitos de A.

# Entrada
# A entrada consiste de vários casos de teste.
# A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste.
# Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor,
# confome exemplo abaixo.

#não é necessário solicitar entrada

N = int(input())

#metodo para verificação de A e B
def verif(A,B):
  if len(B) > len(A):
    return "nao encaixa"
  elif A[-len(B):] == B:
    return "encaixa"
  else:
    return "nao encaixa"

#teste
while(N > 0):
  A, B = input().split() #split para separar os valores após espaço
  saida = verif(A,B)
  print (saida)
  N -= 1 #para decrementar o nº de testes até que chegue em zero e o loop seja encerrado
