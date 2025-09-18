# DESAFIO: CLASSES DE UM JOGO

'''
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
- Classes e Objetos

## Objetivo:

Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}")
- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada

'''
class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        if(self.tipo == "mago"):
            self.ataque = "magia"
        elif(self.tipo == "guerreiro"):
            self.ataque = "espada"
        elif(self.tipo == "monge"):
            self.ataque = "artes marciais"
        elif(self.tipo == "ninja"):
            self.ataque = "shuriken"
        return print(f'O {self.tipo} atacou usando {self.ataque}')
    
Naruto = heroi("Naruto Uzumaki", "27", "ninja")
Naruto.atacar()