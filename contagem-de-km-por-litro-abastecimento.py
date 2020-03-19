print ('ATENÇÃO: Nunca use virgula')

kmInicial = int(input('Digite o KM Inicial: '))
kmFinal = int(input('Digite o KM Final: '))

valorAbastecido = float(input('Valor Abastecido: '))
precoLitro = float(input('Preço do Litro do combustivel: '))

litroAbastecido = valorAbastecido / precoLitro
kmRodado = kmFinal-kmInicial

kmLitro = float(kmRodado / litroAbastecido)

print ('\nLitro Abastecido: ', int(litroAbastecido))
print ('Km Rodados:', int(kmRodado))
print ('Km por Litro:', int(kmLitro))

