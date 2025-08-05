import os
from datetime import datetime
horas=datetime.now()
agr=horas.strftime("%d-%m-%y %H-%M-%S") 
res=str(input("Digite (H) para ver a data e o horário.").upper())
if res=="H":
	print(agr)
else:
	print("Então que tal uma receita de bolo?")
	print("=========Massa do Bolo de Cenoura=========")
	print("1/2 xícara(chá) de óleo")
	print("4 ovos")
	print("2 e 1/2 xícaras(chá) de farinha de trigo")
	print("3 cenouras médias raladas(Raladas em pedaços pequenos)")
	print("2 xícaras(chá) de açúcar")
	print("1 colher(sopa) de fermento em pó")
	print("=========Cobertura do Bolo de Cenoura=========")
	print("1 colher (sopa) de manteiga")
	print("1 xícara (chá) de açúcar")
	print("3 colheres (sopa) de chocolate em pó")
	print("1 xícara (chá) de leite")