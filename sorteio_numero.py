import random
resp = "S"

while resp == "S":
    n = int(input("Informe a quantidade de números: "))
    n1 = int(input("Informe o número inicial: "))
    n2 = int(input("Informe até qual número irá: "))
    for i in range(n):
        numero_sorteado = random.randint(n1, n2)
        print(numero_sorteado)
    resp = input("Deseja sortear novamemte? [S/N]: ")
    while (resp != "S" and resp !="s") and (resp != "N" and resp !="n"):
        resp = input("Opção inválida, escolha novamente [S/N]: ")
print("Programa encerrado!")