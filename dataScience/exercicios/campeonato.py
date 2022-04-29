# fazer notas média e imprimir atleta

from statistics import mean

class Atleta():
  def __init__(self, nome, notas_atleta):
    self.nome = nome
    self.pontos = notas_atleta
      
  def ordena(self):
    return sorted(self.pontos)
  
  def media_notas(self):
    med = self.ordena()
    med = med[1:6]
    return mean(med)
    
  
  def imprime(self):
    texto = f"Resultado final:{chr(10)}Atleta: {self.nome}{chr(10)}Melhor Nota: {max(self.pontos)}{chr(10)}Pior Nota: {min(self.pontos)}{chr(10)}Média: {self.media_notas()} {chr(10)}"
    return texto


if __name__ == '__main__':
  nome_atleta = input("Atleta: ")
  notas = []
  for x in range(0,7):
    notas.append(float(input(f"Nota: ")))
  print(" ")
  # constrói a classe Atleta

  atleta = Atleta(nome_atleta, notas)
  print(atleta.imprime())
  



  
  
  


  



    
  

