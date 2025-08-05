print('-' * 50)
print('BEM VINDO A LOJA DO EDUARDO BATISTA!')
print('-' * 50)

valorPedido = float(input('Digite o valor do pedido: '))
qtParcelas = int(input('Digite a quantidade de parcelas: '))

if qtParcelas < 4:
    juros = 0

elif 4 <= qtParcelas < 6:
    juros = 4 / 100

elif 6 <= qtParcelas < 9:
    juros = 8 / 100

elif 9 <= qtParcelas < 13:
    juros = 16 / 100

else:
    juros = 32 / 100

valorParcela = valorPedido * (1 + juros) / qtParcelas

print(f'Valor da parcela: R$ {valorParcela:,.2f}')