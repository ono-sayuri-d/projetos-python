# DESAFIO: CALCULADORA DE PARTIDAS RANKEADAS

''' 
O que deve ser utilizado
- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
'''

# Objetivo
'''
Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas).

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal
'''

# Saída
'''
Ao final deve se exibir uma mensagem: "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"
'''

def ranking(vitoria,derrota):
    saldoVitoria = vitoria - derrota
    if vitoria <= 10:
        classificacao = "Ferro"
    if vitoria >= 11 or vitoria <=20:
        classificacao = "Bronze"
    if vitoria >= 21 or vitoria <=50:
        classificacao = "Prata"
    if vitoria >= 51 or vitoria <=80:
        classificacao = "Ouro"
    if vitoria >= 81 or vitoria <=90:
        classificacao = "Diamante"
    if vitoria >= 91 or vitoria <=100:
        classificacao = "Lendário"
    if vitoria >= 101:
        classificacao = "Imortal"
    return print(f'\nO Heroi tem saldo de {saldoVitoria} vitórias e classificação {classificacao}')

vitoria_str = input('Insira o número de vitórias do Heroi: ')
derrota_str = input('\nInsira o número de derrotas do Heroi: ')
vitoria = int(vitoria_str)
derrota = int(derrota_str)
ranking(vitoria,derrota)