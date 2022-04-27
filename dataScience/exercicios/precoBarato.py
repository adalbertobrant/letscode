aux = 999999999999
contador = 0
while contador < 3:
  valor = float(input(f"Entre o valor do {contador+1}° produto => "))
  if valor < aux:
    aux = valor
    pos = contador + 1
  contador +=1
  
print(f"O produto mais barato é o {pos}° R${aux}")


  
  
