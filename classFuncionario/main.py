'''Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
'''

from funcionario.Funcionario import meuFuncionario

funcionario1 = meuFuncionario('Ricardo', 1000.999)
funcionario1.mostrarFuncionario()
funcionario1.aumentarSalario(10)
funcionario1.mostrarFuncionario()