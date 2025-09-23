# Utilizando For
#numeros = [1,2,3,4,5]
#for num in numeros:
   # print(num)

    
# Utilizando While    
    
    
    
   # numero = int(input("Digite um numero (ou 0 para sair): "))

   # while numero != 0:
       # if numero % 2 == 0:
         #   print("O número é par.")
       # else: print("O número é ímpar.")
       # numero = int(input("Digite um número (ou 0 para sair):"))


        # Repetição por quatidade 

       # for x in range(5):
          #  print("Repetição", x)

            # Limites Incial e Superior

         #   for y in range(2, 7):
               # print("Repetição com limites", y)

# Com incrimento

              #  for z in range (1, 11, 2):
                   # print("Repetição com incremento", z)


# Break e Continue

#for numero in range(1, 11):
   # if numero % 2 == 0:
       # print("O primeiro número par encontrado é:", numero)
        #break


   # for numero in range(1, 11):
        #if numero == 5:
           # continue
        #print(numero)



# Lista de filmes para classificação

filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

# Mensagens de Boas-vindas 

print("Bem-vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar. \n")

# Loop para iterar sobre cada filme na lista
for filme in filmes:
    # Solicita a classificação ao usuário
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou '0' para parar): ")

# Verifica se o usuário deseja parar 
if classificacao == '0':
    print("Que pena que você não irá classificar mais os filmes.") 
    # Encerra o loop principal

# COnverte a classificaçãi para um número inteiro
classificacao = int(classificacao) 

#Verifica se o calssificaçaõ está dentro do intervalo válido
if classificacao < 1 or classificacao > 5:
    print("Por favor, digite uma classificação válida de 1 a 5.")
else:
    # Exibe a classificação e passa para o próximo filme
    print(f"Você lcassificou '{filme}' com {classificacao} estrelas.\n")

    # Mensagem de agradecimento ao finalizar 
    print("Obrigado por classificar os filmes!")