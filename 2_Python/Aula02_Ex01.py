num_itens = int(input('Digite quantos itens precisa comprar no mercado: '))

lista_compras = []

for i in range(num_itens):
    item = input(f'Digite o item {i + 1} da lista de compras: ')
    lista_compras.append(item)

for item in lista_compras:
    print(item)