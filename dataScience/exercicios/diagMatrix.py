from random import *

# criação da classe 

class diagMatrix():
  def __init__(self,comum,principal,numero):
    self.comum = comum
    self.principal = principal
    self.numero = numero

# método para impressão da classe diagMatrix

  def imprime(self):
    for x in range(0,self.numero - 1):
      for y in range(0,self.numero - 1):
        if (x == y):          
          print(self.principal, end = '')          
        else:
          print(self.comum, end = '')
      print(" ")

# transforma em emoji selecionados randomicamente
  def viraEmoji(self):
    
    lista = [
      "\U0001F600","\U0001F603","\U0001F604","\U0001F601",
      "\U0001F606","\U0001F923","\U0001F602","\U0001F642",
      "\U0001F643","\U0001F60A","\U0001F607","\U0001F60D",
      "\U0001F929","\U0001F618","\U0001F617","\U0001F61A",
      "\U0001F619","\U0001F60B","\U0001F61B","\U0001F61C",
      "\U0001F92A","\U0001F61D","\U0001F911","\U0001F917",
      "\U0001F92D","\U0001F92B","\U0001F914","\U0001F910",
      "\U0001F928","\U0001F610","\U0001F611","\U0001F636",
      "\U0001F60F","\U0001F612","\U0001F644","\U0001F62C",
      "\U0001F925","\U0001F60C","\U0001F614","\U0001F62A",
      "\U0001F924","\U0001F634","\U0001F637","\U0001F912",
      "\U0001F915","\U0001F922"
      ]
    self.comum = randrange(len(lista))
    self.principal = randrange(len(lista))
    if ( self.comum != self.principal ):
      print("sorteio realizado com sucesso")
      print("carinhas escolhidas => ", end = '')
      self.comum = lista[self.comum]
      self.principal = lista[self.principal]
      print(self.principal, end = ' ')
      print(self.comum)
    else:
      self.comum = lista[3]
      self.principal = lista[10]

    return diagMatrix(self.comum, self.principal, self.numero)

    

# argumento da main 
  
if __name__ == '__main__':
  comum = input("Entre o símbolo comum na matriz => ")
  principal = input("Entre o símbolo principal da matriz => ")
  n = int(input(f"Entre a quantidade de linhas da matriz => "))
  surpresa = input(f"Vc quer uma coisa diferente ? S para sim N para não => ")
  if surpresa == 'S' or surpresa == 's':
    emoji = diagMatrix(comum, principal, n)
    emoji = emoji.viraEmoji()
    print( " ")
    emoji.imprime()

  else:
     # cria objeto do tipo diagMatrix
    objeto = diagMatrix(comum, principal, n)
     # chama o método imprime para o objeto criado
    print(" ")
    objeto.imprime()
  print(" ")
  

  
