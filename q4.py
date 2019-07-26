palavra_secreta =  "ingles"
letra_descobertas = []

#append serve para adicionar um elemento à lista
#esse for vai percorrer a palavra secreta e substituir por *
for i in range(0, len(palavra_secreta)):
	letra_descobertas.append("*")

acertou = False

rodada = 0

while(rodada < 11):
		
#esse while vai percorrer a palavra secreta e compara com a letra digitada
	while acertou == False:
		letra = str(input( "Digite a letra: "))

#esse for vai compara a letra digitada com a palavra secreta 
		for i in range(0, len(palavra_secreta)):
			if letra == palavra_secreta[i] :
				letra_descobertas[i] = letra
			print(letra_descobertas[i])

		acertou = True
#esse for vai substituir o * pela a letra digitada
		for x in range(0, len(letra_descobertas)):
			if letra_descobertas[x] ==  "*":
				acertou = False
	rodada = rodada + 1
			
print("parabéns")