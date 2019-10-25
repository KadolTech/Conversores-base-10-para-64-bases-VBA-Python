##########################################################################################
##   PROGRAMA FEITO POR - HENRIQUE RIBEIRO DOS SANTOS E CAROLINA RIBEIRO DA COL SILVA   ##
##                   MATRÍCULAS - 2840481821014 // 2840481821003                        ##
##########################################################################################
import os

dic = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def testNum():
	x = input("Digite um valor decimal: ")
	while not x.isnumeric():
		x = input("Digite um valor decimal: ")
	return int(x)

def testBase():
	base = input("Digite a base para conversão: ")
	while not base.isnumeric():
		base = input("Digite a base para conversão: ")
	return int(base)

try:
	conti = 1;
	while (conti == 1):
		print (f"Conversor para até {len(dic)} bases")
		x = testNum()
		base = testBase()
		while base <=1 or base >62:
			base = testBase()
		resposta = ""

		while (x!=0):
			resposta = resposta + dic[int(x%base)]
			x = int(x/base)

		print (f"O valor escolhido com base {base} é: {resposta[::-1]}")
		conti = int(input ("Deseja fazer uma nova conversão? [1] - Sim // [2] - Não \n"))
		os.system("cls")
	os.system("pause")
except:
	print ("Erro!! Contate os administradores!!\n")
	os.system("pause")
