'''Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre 
os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.'''


from classes.interagindo import interagir


bv = interagir(nome='Ricardo', fome=10, saude=10, idade=0)
bv.status()
bv.comer('maça')
bv.brincar('bola')
bv.pararDeBrincar()
bv.comer('maça')
bv.pararDeComer()
bv.status()
bv.cuidarSaude()
bv.cuidarSaude()
bv.cuidarSaude()
bv.cuidarSaude()
bv.cuidarSaude()
bv.cuidarSaude()
bv.comer('maça')
bv.pararDeComer()
bv.comer('maça')
bv.pararDeComer()
bv.comer('maça')
bv.pararDeComer()
bv.comer('maça')
bv.pararDeComer()
bv.comer('maça')
bv.pararDeComer()
bv.comer('maça')
bv.pararDeComer()
