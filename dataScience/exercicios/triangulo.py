# ver se é triangulo e determinar o tipo do triangulo


class Triangulo:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c    

  def eh_triangulo(self):
    if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
      return True  
    return False

  def eh_triangulo_equilatero(self):
    if self.a == self.b and self.a == self.b and self.a == self.c:
      return True
    return False
  
  def eh_triangulo_escaleno(self):
    if self.a != self.b and self.a != self.c and self.b != self.c:
      return True 
    return False 

  def eh_triangulo_isoceles(self):
    if not self.eh_triangulo_equilatero() or not self.eh_triangulo_escaleno:
      return True
    return False
  
count = 0
while count < 4:
  count += 1
  la,lb,lc = int(input(f"Entre o dado para lado A ")), int(input(f"Entre o dado para o lado B ")),int(input(f"Entre o dado para o lado C "))


  b = Triangulo(la,lb,lc)
  if b.eh_triangulo():
    if b.eh_triangulo_escaleno():
      print(f"{b.a, b.b, b.c}")
      print(f"Triangulo é escaleno")
    elif b.eh_triangulo_isoceles():
      print(f"{b.a, b.b, b.c}")
      print(f"Triangulo é isóceles")
    elif b.eh_triangulo_equilatero():
      print(f"{b.a, b.b, b.c}")
      print(f"Triangulo Equilatero")
  else:
    print(f"{b.a, b.b, b.c}")
    print(f"Não é triangulo")

