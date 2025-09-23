texto = "Explorando a diversaidaded de linguagens de programação com Python."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Qauntidade de e no texto = {texto.count('e')}")
print(f"As 5 primeiras letras são: {texto[:5]}")


texto[13]

cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
for cor in cores:
    print(f'Posição = {cores.index(cor)}, cor = {cor}')



# Função map
# aplica a uma função em toda sequencia
# map(funcao, sequencia)
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_reias = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares)) 
print(precos_em_reias)

#função filter!
# filtra uma sequencia com base em uma função que retorna True ou False
# filter(funcao_teste, sequencia)
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

# A ORDEM IMPORTA--
# EXEMPLOS DE MAIS TUPLAS E UTILIDADE
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")



# Tupla de convidados 
convidados = ("Anna", "Luciana", "Carlos", "Pedro", "Alexandre")
# Lista de confirmações
confirmados = ["Carlos", "Anna"]
#Identificar quem ainda não confirmou 
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
# Exibir os convidados que não confirmaram 
print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)
# Enviar lembretes aos não confirmados 
print("\nEnviando lembretes para os convidados que ainda nao confirmaram.") 