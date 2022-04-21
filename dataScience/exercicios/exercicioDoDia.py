# fazer uma lista , pegar outro número e ver se este número é o resultado da multiplicação de 
# elementos da lista

numLista = [ ]
while(True):
  aux = int(input(" Entre um número => "))
  if aux != 0:
			numLista.append(aux)
  else:
    break

aux = int(input("Entre o outro número para verificação => "))

caso1 = False

for i in range(0,len(numLista)-1):
  for j in range(i+1,len(numLista)):
    if(numLista[j] * numLista[i] == aux):
      print(f"Resultado: {numLista[i]} e {numLista[j]}")
      caso1 = True

if caso1 == False:
  print("Resultado: não existe tais números")







