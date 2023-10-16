import random
resp = "S"

while resp == "S":
    n = int(input("Informe a quantidade de números: "))
    for i in range(n):
        numero_sorteado = random.randint(1, 26)
        print(numero_sorteado)
    resp = input("Deseja sortear novamemte? [S/N]: ")
    while (resp != "S" and resp !="s") and (resp != "N" and resp !="n"):
        resp = input("Opção inválida, escolha novamente [S/N]: ")
print("Programa encerrado!")

#O programa pede ao usuário quantos número ele deseja sortear e também solicita a ele qual o número ele irá até onde vai;
#No fim ele ainda pergunta se deseja refazer o sorteio ou encerrar o programa
