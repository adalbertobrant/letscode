# ler dois números e realizar a operacao
import operator

operacoes = {'add':'+', 'divisao':'/', 'divisaoInteira':'//','multiplicacao':'*', 'subtracao':'-', 'resto':'%','potenciacao':'**'}

x = float(input(f"Entre o primeiro número => "))

y = float(input(f"Entre o segundo número => "))

while True:

  print(" ")
  print (f"------------------")
  print (f"1 - Somar {x} & {y}")
  print (f"2 - Dividir {x} & {y}")
  print (f"3 - Divisão inteira de {x} & {y}")
  print (f"4 - Multiplicação de {x} & {y}")
  print (f"5 - Subtração de {x} & {y}")
  print (f"6 - Resto entre {x} & {y} ")
  print (f"7 - Potenciação entre {x} & {y}")
  print(" ")
  op = int(input(f"Escolha uma opção para realizar a operação ou  digite '0' para sair => "))

  if op == 0:
    break
  else:
    print (" ")
    k = funcoes[op-1].__name__
    print(f"{k.upper()} => {x} {operacoes.get(k)} {y} == {operator.k(x,y)}")

     
