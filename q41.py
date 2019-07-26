

def jogar():
	palavra_secreta = "ingles"
	enforcou = False
	ganhou = False
	
	for rodada in range(1,10):
	
		while(not enforcou and not ganhou):
			index = 0
			chute = input("Qual a Lentra: ").lower().strip()
			for x in palavra_secreta:
				if(chute == x):
					print("Lentra {} encontrada na posicao {}".format(chute,index))
				index += 1

	print("Fim do jogo")

jogar()