"""
Exercício com Abstração, herança, Encapsulamento e Polimorfismos.
Criar um sistema bancário (extremamente simples), que tem clientes, contas e um banco. 
A ídeia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. 
Contas corrente tem um limite extra. 
Banco tem clientes e contas.

Dicas:
1. Criar classe cliente que herda da classe pessoa (herança)
  Pessoa tem nome e idade(getter)
  Cliente TEM conta(Agregação da classe ContaCorrente ou ContaPoupança)

2. Criar classes ContaPoupança e ContaCorrente que herdam da Conta
  ContaCorrente deve ter um limite extra
  Contas tem agências, número da conta e saldo
  Contas devem ter o método para depósito
  Conta(super classe) deve ter o método sacar abstrato (Abastração e polimorfismos - as subclasses que implementam o método sacar)

3. Criar classe Banco para AGREGAR classes de clientes e de contas(Agregação)

4. Banco será o responsável autenticar o cliente e as contas da seguinte maneira:
  Banco tem contas e clientes(Agregação)
  * Checar se agência é daquele banco
  * Checar se o cliente é daquele banco
  * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco(descritos acima)
"""

from classes.PF import pessoaFisica

Cliente1 = pessoaFisica(nome='Ricardo', idade=31, tipoConta='PF', conta='PF', nAgencia=1111, nConta=1111, banco='341', limite=100)
Cliente2 = pessoaFisica(nome='Wilson', idade=31, tipoConta='PF', conta='PF', nAgencia=2222, nConta=2222, banco='341', limite=1000)



Cliente1.sacar(50)
Cliente1.consultarSaldo()
Cliente1.sacar(49)
Cliente1.consultarSaldo()
Cliente1.sacar(1)
Cliente1.depositar(1000)

print('-='*50)

Cliente2.sacar(100)
Cliente2.consultarSaldo()
Cliente2.sacar(100) 
Cliente2.transferir(outroCliente=Cliente1, agencia=1111, conta=1111, valorTransferencia=100)
Cliente2.transferir(outroCliente=Cliente1, agencia=1111, conta=1111, valorTransferencia=100)
Cliente1.transferir(outroCliente=Cliente2, agencia=1111, conta=1111, valorTransferencia=100)
Cliente1.transferir(outroCliente=Cliente2, agencia=1111, conta=1111, valorTransferencia=100)
Cliente1.transferir(outroCliente=Cliente2, agencia=1111, conta=1111, valorTransferencia=100)
Cliente1.transferir(outroCliente=Cliente2, agencia=1111, conta=1111, valorTransferencia=100)
Cliente1.transferir(outroCliente=Cliente2, agencia=1111, conta=1111, valorTransferencia=100)
Cliente2.sacar(100)
Cliente2.consultarSaldo()
Cliente1.consultarSaldo()
Cliente2.transferir(outroCliente=Cliente1, agencia=1111, conta=1111, valorTransferencia=1)
Cliente2.consultarSaldo()