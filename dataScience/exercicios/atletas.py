def mediaModificada(a,b,c):
  return (a+b+c)/ 3

i = int(1)
saltos = []
ordinal = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
nome = input("Atleta: ")
print("Informe os saltos do Atleta")
while(i <= 5):
  aux = float(input( f"Digite o {ordinal[i-1]} salto => "))
  i = i + 1
  saltos.append(aux)

print (f"\nAtleta: {nome}")
print (" ")
for j in range(0,5):
  print (f"{ordinal[j]} Salto: {saltos[j]} m")
print (" ")
saltos.sort()
print (f"Melhor Salto: {saltos[4]} m")
print (f"Pior Salto: {saltos[0]} m")
media = mediaModificada(*saltos[1:-1])
print (f"Média dos demais saltos: {media} m")
print (f"\nResultado final:")
print (f"{nome}: {media} m")


 
