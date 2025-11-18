'''
2. Um aplicativo permite que o usuário personalize seu avatar escolhendo: 5 modelos de corpo; 6 estilos de
cabelo; 8 tipos de roupa e 4 cores de acessório. De quantas maneiras diferentes um avatar pode ser gerado?

'''

modelo_corpo = 5
estilo_cabelo = 6
tipo_roupa = 8
cores_acessorio = 4
avatar = modelo_corpo * estilo_cabelo * tipo_roupa * cores_acessorio
print(avatar)