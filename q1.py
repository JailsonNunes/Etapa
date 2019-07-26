import random

resposta = True

while (resposta == 1):
    #random vai gera um numero entre 1 e 6
  numeros_aleatorios = random.randint(1,6)
  
  print ('Valor do dado  = ', numeros_aleatorios)
  #depois que roda o dado vai pergunta se quer continuar ou para
  resposta = int(input('Voce quer continuar? Digite 1 para continuar ou 0 para finalizar '))



