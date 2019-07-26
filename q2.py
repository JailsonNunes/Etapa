import random

numero_secreto = random.randrange(1,101)
rodada = 0
print("Você tem 10 Chance Boa Sorte")
for rodada in range(1,11):
	print("rodada: ",rodada)

	chute = int(input("Digite um numero entre 1 e 100: "))
#esse if vai fazer a comparação caso o usuario digite um numero menor que 1 ou maior que 100
	if(chute < 1 or chute > 100):
		print("Você deve digitar um número entre 1 e 100!")
		chute = int(input("Digite um numero? "))

#aqui vai fazer comparação com as variavel caso chute foi acertou, maior ou menor
	acertou = chute == numero_secreto
	maior   = chute > numero_secreto
	menor   = chute < numero_secreto

#aqui vou usar if para compara se a acertou e igual a numero secreto se for falso vou else com um if e elif
	if(acertou):
		print("Parabéns Você Acertou")
		break
	else:
#vou usar um if e elif para compara se chute foi maior ou menor que o numero secreto
		if(maior):
			print("Você errou! O seu chute foi alto do que o número secreto.")
		elif(menor):
			print("Você errou! O seu chute foi baixo do que o número secreto.")

print("numero secreto era: ",numero_secreto)