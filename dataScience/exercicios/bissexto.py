def bissexto(ano):
  if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    return True
  return False


ano = int(input(f"Entre o ano para saber se é bissexto ou não => "))

print(f"O ano {ano} é bissexto = > {bissexto(ano)}")


