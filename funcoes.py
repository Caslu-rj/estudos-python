# Cria uma lsita de números 
numeros = [1,2,3,4,5,6] 

# Usa a função len() para calcular o comprimento dad lista 
comprimento = len(numeros)

# Imprime o comprimento da lista 
print("O comprimento da lista é:", comprimento)


#Definindo uma função chamada "Soma"
def soma(a, b):
    resultado = a + b
    return resultado

resultando_soma = soma(5, 3)

# Imprimindo o resultado 
print("A soma de 5 e 3 é:", resultando_soma)


#Definindo uma função chamada "e_par"
def e_par(numero):
    #operador módulo %
    if numero % 2 == 0:
        return True
    else:
        return False
    numero = 18371892371289731928754
    if e_par(numero):
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} não é um número par.")


# Lista de notas dos estudantes 
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

#Função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
    
    # Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

    # Calcular a média
media = calcular_media(notas)
media_arrendondada = arredondar_media(media)

    # verificar se os estudante foram aprovaddor 
situacao = "Aprovado" if media_arrendondada >= 7 else "Reprovado"

# Resultados
print("Notas dos estudante:", notas)
print("Média das notas:", media_arrendondada)
print("Situação do estudante:", situacao)