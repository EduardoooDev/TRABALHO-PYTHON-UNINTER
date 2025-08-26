print('-------BEM VINDO A LOJA DE MARMITAS DO EDUARDO BATISTA-------')

print("CARDÁPIO:")
print("SABOR: Bife Acebolado (BA)  | Filé de Frango (FF)")
print("TAMANHO P - R$16,00 (BA) | R$15,00 (FF)")
print("TAMANHO M - R$20,00 (BA) | R$18,00 (FF)")
print("TAMANHO G - R$25,00 (BA) | R$22,00 (FF)")
print("-" * 61)


total = 0



while True:
    while True: 
        escolhaSab = input('Entre com o sabor desejado: (BA/FF): ').upper()
        if escolhaSab in ['BA','FF']:
            break
        print('Sabor invalido! Tente novamente.')
        continue



    while True:
        tamanho = input('Digite o tamanho da marmita (P/M/G): ').upper()
        if tamanho in ['P' , 'M' , 'G']:
            break
        print('Tamanho invalido! Tente novamente. ')
        continue

    if escolhaSab == 'BA' and tamanho == 'P':
        preco = 16.00
        print(f'Você pediu um Bife Acebolado tamanho P total : R${preco:.2f}')
        total += preco
    elif escolhaSab == 'BA' and tamanho == 'M':
        preco = 18.00
        print(f'Você pediu um Bife Acebolado tamanho M total : R${preco:.2f}')
        total += preco
    elif escolhaSab == 'BA' and tamanho == 'G':
        preco = 22.00
        print(f'Você pediu um Bife Acebolado tamanho G total : R${preco:.2f}')
        total += preco
    elif escolhaSab == 'FF' and tamanho == 'P':
        preco = 15.00
        print(f'Você pediu um File de Frango tamanho P total : {preco:.2f}')
        total += preco
    elif escolhaSab == 'FF' and tamanho == 'M':
        preco = 17.00
        print(f'Você pediu um File de Frango tamanho M total : {preco:.2f}')
        total += preco
    elif escolhaSab == 'FF' and tamanho == 'G':
        preco = 21.00
        print(f'Você pediu um File de Frango tamanho M total : {preco:.2f}')
        total += preco

    continuar = input('Deseja continuar (S/N): ').upper()
    if continuar == 'N':
     break


print (f'Valor do pedido {total:.2F}')
