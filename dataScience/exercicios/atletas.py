











i = int(1)
saltos = []
nome = input("Atleta: ")
print("Informe os saltos do Atleta")
while(i <= 5):
  aux = float(input( f"Digite o {i}° salto => "))
  i = i + 1
  saltos.append(aux)

print (f"\nAtleta: {nome}")
print (" ")
print (f"Primeiro Salto: {saltos[0]} m")
print (f"Segundo Salto: {saltos[1]} m")
print (f"Terceiro Salto: {saltos[2]} m")
print (f"Quarto Salto: {saltos[3]} m")
print (f"Quinto Salto: {saltos[4]} m")
print (" ")
saltos.sort()
print (f"Melhor Salto: {saltos[4]} m")
print (f"Pior Salto: {saltos[0]} m")
media = (saltos[1]+saltos[2]+saltos[3]) / 3
print (f"Média dos demais saltos: {media} m")
print (f"\nResultado final:")
print (f"{nome}: {media} m")


 
