bateria = 70
horario = 12
estrada = 'Fechado'

if bateria >= 50 and estrada == 'Livre':
    print("Pode ser entregue")
else:
    if horario > 9 and horario < 18:
        print("Pode ser entregue")
    else:
        print("Não pode ser entregue")