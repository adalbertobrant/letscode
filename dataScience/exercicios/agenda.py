# criar agenda com código pessoa, número telefone, idade

# inserir um contato
def inserir_contato(args, agenda):
  codPessoa, numTel, idade = *args,
  if len(agenda) == 0:
    agenda = [ { 'codigoPessoa':codPessoa, 'numeroTelefone':numTel, 'idade':idade } ]
    return agenda
  else:
    agenda.append( {'codigoPessoa':codPessoa, 'numeroTelefone':numTel, 'idade':idade } )
    return agenda   

# remover um contato pelo código da pessoa
def remover_contato(codPessoa, agenda):
  for i in range(len(agenda)):
    if agenda[i]['codigoPessoa'] == codPessoa:
      del agenda[i]
      break
  return agenda

# editar um contato
def editar_contato(codPessoa, agenda):
  newCodPessoa = input("Entre o novo código da pessoa => ")
  newNumeroTelefone = input("Entre o novo número de telefone da pessoa => ")
  newIdade = input("Entre a nova idade da pessoa => ")
  for i in range(len(agenda)):
    if agenda[i]['codigoPessoa'] == codPessoa:
      agenda[i]['codigoPessoa'] = newCodPessoa
      agenda[i]['numeroTelefone'] = newNumeroTelefone
      agenda[i]['idade'] = newIdade
      break
  return agenda

def imprimir_agenda(agenda):
  for x in agenda:
    print(x)

# buscar um contato pelo código
def buscar_contato(codPessoa, agenda):
  flag = True
  for i in range(len(agenda)):
    if agenda[i]['codigoPessoa'] == codPessoa:
      print ("\nContato encontrado")
      flag = False
      return agenda[i]
  if flag:
    return f"\nContato não encontrado\n" 

def menu():
  print ("------------------------")
  print (f"1 - Inserir um contato ")
  print (f"2 - Remover um contato ")
  print (f"3 - Editar um contato ")
  print (f"4 - Buscar um contato ")
  print (f"5 - Imprimir agenda ")
  print (f"6 - Sair ")
  print ("------------------------")

agenda = {}

while(True):
  menu()
  opcao = int(input(" ===> "))

  if opcao == 1:
    codPessoa = input("Entre o código da pessoa => ")
    numTel = input("Entre o número da pessoa => ")
    idade = input("Entre a idade da pessoa => ")
    lista = [codPessoa, numTel, idade]
    agenda = inserir_contato(lista, agenda=agenda)
  
  if opcao == 2:
    codPessoa = input("Entre o código da pessoa => ")
    agenda = remover_contato(codPessoa, agenda)

  if opcao == 3:
    codPessoa = input("Entre o código da pessoa para editar => ")
    agenda = editar_contato(codPessoa, agenda)

  if opcao == 4:
    codPessoa = input("Digite o código da pessoa para buscar => ")
    print(buscar_contato(codPessoa, agenda))
    
  
  if opcao == 5:
    imprimir_agenda(agenda)

  if opcao == 6:
    exit()






  
