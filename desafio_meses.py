# DESAFIO
# Leia um valor inteiro entre 1 e 12, inclusive.
# Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso,
# em inglês, com a primeira letra maiúscula.

# ENTRADA
# A entrada contém um único valor inteiro.

#SAÍDA
# Imprima por extenso o nome do mês correspondente ao número existente na entrada,
# com a primeira letra em maiúscula.

#não é necessário solicitar entrada

month = int(input())

#método com dicionário para registrar os meses por extenso

def write_month(month):
  months_dict = {
  1:"January", 2:"February", 3: "March", 4:"April", 5:"May", 6: "June", 7: "July", 8:"August", 9:"September", 10:"October", 11:"November", 12: "December"
  }
  if 1<= month <=12:
    return months_dict[month]
  else:
    return "mês inválido"
  
  
name_month = write_month (month)
print(name_month)