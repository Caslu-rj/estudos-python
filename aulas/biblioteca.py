import biblioteca as np
# Crie um array NumPy de números inteiros
my_array = np.array([1, 2, 3, 4, 5])
# Imprima o array 
print("Array original:")
print(my_array)
# Realize operações matemáticas com o array
squared_array = my_array ** 2 # Eleva cada elemento ao quadrado
sum_of_elements = np.sum(my_array) # Calcula a soma de todos os elementos
# Imprima os resultados
print("\nArray ao quadrado:")
print(squared_array)
print("\nSoma dos elementos:")
print(sum_of_elements)
# Acesse elementos do array
element_at_index_2 = my_array[2] # Acessa o elemento no índice 2
print("\nElemento no índice 2:", element_at_index_2)





# Dados dos participantes 
participantes = [
    {
        "nome": "Alice",
        "localizacao": "EUA",
        "afiliacao": "Universidade A",
        "interesses": ["Física", "Astronomia"]
    },
    {
        "nome": "Bob",
        "localizacao": "Brasil",
        "afiliacao":
        "Instituto B",
        "interesses":
        ["Biologia", "Astronomia"]
    },
    {
        "nome": "Charlie",
        "localizacao": "Índia", 
        "afiliacao": "Instituto C", "interesses": ["Química", "Engenharia"]
    }
    # Adicione mais participantes conforme necessário
]
# Usando sets para indentificar diferentes regiões dos participantes 
regioes = set(participante["localizcao"] for participante in participantes)
# Usando um dicionário para categorizar afilições 
afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
        afiliacoes[afiliacao].append(participante["nome"])
# Usandod NumPy para analisar área de interesse
areas_de_interesse = np.array([interesse for particpante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmmax(contagem)]
# Resultados
print("Região dos participantes:", regioes)
print("Afiliações dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}: {','.join(nomes)}")
print("Área de interesse mais popular:", area_mais_popular)