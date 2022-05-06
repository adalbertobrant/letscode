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

# argumento da main 
  
if __name__ == '__main__':
  comum = input("Entre o símbolo comum na matriz => ")
  principal = input("Entre o símbolo principal da matriz => ")
  n = int(input(f"Entre a quantidade de linhas da matriz => "))
  # cria objeto do tipo diagMatrix
  objeto = diagMatrix(comum, principal, n)
  # chama o método imprime para o objeto criado
  print(" ")
  objeto.imprime()
  

  
