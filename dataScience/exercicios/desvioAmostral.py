# desvio padrão de uma lista de números

import math

def mediana(lista):
  lista.sort()
  if len(lista) % 2 == 0:
    soma = lista[(len(lista)//2)-1] + lista[len(lista)//2]
    return soma /2
  else:
    return lista[len(lista)//2]

def desvio(lista):
  listaDesviada = [ ]
  med = media(lista)
  for x in lista:
    des = x - med
    listaDesviada.append(des**2)
  
  return listaDesviada


def desvioAmostral(lista):
  soma = somatorio(desvio(lista))
  x = soma / len(lista)
  raiz = math.sqrt(x)
 
  return raiz

def somatorio(lista):
  soma = 0
  for x in lista:
    soma = soma + x

  return soma
  

def media(lista):
  x = somatorio(lista)
  return x/len(lista)

listaNumeros = []

while(True):
  x = float(input("Entre um número real xx.xx => "))
  if x != 0:
    listaNumeros.append(x)
  else:
    break

print (listaNumeros)
print (f"media(listaNumeros)=> {media(listaNumeros)}")
print (f"somatorio(listaNumeros)=> {somatorio(listaNumeros)}")
print (f"desvioAmostral(listaNumeros)=> {desvioAmostral(listaNumeros)}")
print (f"mediana(listaNumeros)=> {mediana(listaNumeros)}")

