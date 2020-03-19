# Em um novo programa, crie uma tupla para guardar os meses do ano.
# Em seguida, peça ao usuário a sua data de nascimento no formato DD-MM-AAAA e guarde-a
# na varivavel.
# Ao final, imprima "Você nasceu no mês de ___________", utilizando o nome do mês da tupla
# correspondente ao mês informado pelo utlizador

# Dica: Você vai precisar fazer o slicing na data de nascimento informada para ter o mês.
# Depois você tera que buscar o mês na tupla através do indice


print ('mês de aniversário')
meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
dataNascimento = input('Digite a sua data de nascimento no formato DD-MM-AAAA: ')

indice = int(dataNascimento[3:5])-1
mes = meses[indice]

print ('você nasceu no mês de: ',mes)
