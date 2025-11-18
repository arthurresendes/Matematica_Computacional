'''
3. Um professor deseja selecionar 4 alunos para apresentar projetos na ordem A → B → C → D, mas um dos alunos
(João) só pode apresentar em último. Entre 8 alunos, quantos arranjos válidos existem?


'''

import math

def fatorial(num: int):
    return math.factorial(num)

alunos = fatorial(7)
alunos_menos_ordem = fatorial(4)

aluno_fixo = 1

total = alunos / alunos_menos_ordem
total = total * aluno_fixo
print(total)

