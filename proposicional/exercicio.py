entrada = False

identificação = input("Digite seu nome: ").title()
horario = 23
lista_suspenso = ['Arthur', 'Jose','Gustavo']

if horario >= 6 and horario <= 22:
    print("Acesso liberado!!")
    entrada = True
elif identificação not in lista_suspenso:
    print("Acesso liberado!!")
    entrada = True
else:
    print("Acesso negado")