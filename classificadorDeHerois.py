# DESAFIO: CLASSIFICADOR DE NÍVEL DE HEROI

''' 
O que deve ser utilizado
- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
'''

# Objetivo
'''
Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um heroi, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor que 1000 = Ferro
Se XP for entre 1001 e 2000 = Bronze
Se XP for entre 2001 e 5000 = Prata 
Se XP for entre 5001 e 7000 = Ouro
Se XP for entre 7001 e 8000 = Platina Diamante
Se XP for entre 8001 e 9000 = Ascendente
Se XP for entre 9001 e 10000 = Imortal
Se XP for maior ou igual a 10001 = Radiante
'''

# Saída
'''
Ao final deve se exibir uma mensagem: "O Heroi de nome {nome} está no nível {nível}
'''

nome_personagem = input('Insira o nome do Heroi: ')
nivel_xp_str= input('\nInsira o nível de experiência (XP) do Heroi: ')
nivel_xp = int(nivel_xp_str)

if nivel_xp < 1000:
    classificacao = "Ferro"
elif nivel_xp <= 1001 or nivel_xp <= 2000:
    classificacao = "Bronze"
elif nivel_xp <= 2001 or nivel_xp <= 5000:
    classificacao = "Prata"
elif nivel_xp <= 5001 or nivel_xp <= 7000:
    classificacao = "Ouro"
elif nivel_xp <= 7001 or nivel_xp <= 8000:
    classificacao = "Platina Diamante"
elif nivel_xp <= 8001 or nivel_xp <= 9000:
    classificacao = "Ascendente"
elif nivel_xp <= 9001 or nivel_xp <= 10000:
    classificacao = "Imortal"
elif nivel_xp >= 10001:
    classificacao = "Radiante"

print(f"\nO Heroi {nome_personagem} está no nível {nivel_xp} e tem classificação {classificacao}")