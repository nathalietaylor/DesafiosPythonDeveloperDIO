# DESAFIO
# O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
# Conferir se um texto vai caber em um tuíte é sua tarefa.

# ENTRADA
# A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

# SAÍDA
# A saída é dada em uma única linha.
# Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres.
# Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

# a entrada é determinada pelo sistema, não há necessidade de solicitar

T = input()

def TODO(T):
  limite = 140
  if len(T)<= limite:
    print ("TWEET")
  else:
    print ("MUTE")

TODO(T)
