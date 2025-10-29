python_total = 50
c_total = 32
java_total = 26
python_c_ambos = 10
python_java_ambos = 12
java_c_ambos = 15
tudo_tres = 5
total_pessoas = 115


apenas_python_c = python_c_ambos - tudo_tres
apenas_python_java = python_java_ambos - tudo_tres
apenas_java_c = java_c_ambos - tudo_tres


apenas_python = python_total - (apenas_python_c + apenas_python_java + tudo_tres)
apenas_c = c_total - (apenas_python_c + apenas_java_c + tudo_tres)
apenas_java = java_total - (apenas_python_java + apenas_java_c + tudo_tres)


sabem_apenas_um = apenas_python + apenas_c + apenas_java


sabem_duas_ou_mais = apenas_python_c + apenas_python_java + apenas_java_c + tudo_tres


sabem_alguma_lingua = sabem_apenas_um + sabem_duas_ou_mais
sabem_nada = total_pessoas - sabem_alguma_lingua


print(f"Pessoas que sabem exatamente uma linguagem: {sabem_apenas_um}")
print(f"Pessoas que sabem duas ou mais linguagens: {sabem_duas_ou_mais}")
print(f"Pessoas que não sabem nenhuma linguagem: {sabem_nada}")
