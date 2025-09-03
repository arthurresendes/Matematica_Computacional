import datetime

bateria = int(input("Digite o numero da sua bateria: "))
rota = input("Rota livre ou fechada: ").title()

tempo = datetime.datetime.now() #.hour
hora = tempo.hour
print(hora)
if bateria >= 50 and rota == 'Livre' or hora > 8 or hora < 18:
    print("Entrega pode ser feita")
else:
    print("Nao pode")