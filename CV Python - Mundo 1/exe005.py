print('===================================================')
print("         Classificando Strings")
print('===================================================')
algo = input('Digite algo: ')
print ('A string \'{}\' é do tipo numérico? '.format(algo))
print (algo.isnumeric())
print ('A string \'{}\' são números?'.format(algo))
print(algo.isdigit())
#diferenças entre .isdigit and .isnumeric
print('A string \'{}\' são apenas letras?'.format(algo))
print(algo.isalpha())
print('A string \'{}\' é do tipo alphanumérica (letras e/ou números)?'.format(algo))
print(algo.isalnum())
print('A string \'{}\' é do tipo decimais (sem pontos)?'.format(algo))
print(algo.isdecimal())
print('A string \'{}\' está escrita toda em maiúscula?'.format(algo))
print(algo.isupper())
print('A string \'{}\' está escrita em minúscula?'.format(algo))
print(algo.islower())
print('A string digitada contém só espaços?')
print(algo.isspace())
print('A string \'{}\' inicía em maiúsculas, seguida de minúsculas?'.format(algo))
print(algo.istitle())
print('Método var.isidentifier desconhecido, classificando: {}'.format(algo))
print(algo.isidentifier())
print ('Método var.isprintable desconhecido, classificando: {}'.format(algo))
print('Pode ser letras, símbolos, digitos, pontuação e espaço em branco...  ')
print (algo.isprintable())
