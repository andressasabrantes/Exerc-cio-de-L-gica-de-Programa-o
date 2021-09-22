print('Vamos fazer as compras de frutas da semana?!')
print('1-Laranja 2-Maçã 3-Banana 4-Kiwi 5-Pêra 6-Limão 7-Mamão 8-Abacaxi 9-Melão 10-Carambola')
fruta1 = int(input('Digite a quantidade de Laranja que deseja comprar: '))
valordacompra = fruta1 * 1.50
fruta2 = int(input('Digite a quantidade de Maçã que deseja comprar: '))
valordacompra2 = fruta2 * 1.75
fruta3 = int(input('Digite a quantidade de Banana que deseja comprar: '))
valordacompra3 = fruta3 * 1.25
fruta4 = int(input('Digite a quantidade de Kiwi que deseja comprar: '))
valordacompra4 = fruta4 * 1.30
fruta5 = int(input('Digite a quantidade de Pêra que deseja comprar: '))
valordacompra5 = fruta5 * 3.50
fruta6 = int(input('Digite a quantidade de Limão que deseja comprar: '))
valordacompra6 = fruta6 * 2.50
fruta7 = int(input('Digite a quantidade de Mamão que deseja comprar: '))
valordacompra7 = fruta7 * 3.50
fruta8 = int(input('Digite a quantidade de Abacaxi que deseja comprar: '))
valordacompra8 = fruta8 * 1.75
fruta9 = int(input('Digite a quantidade de Melão que deseja comprar: '))
valordacompra9 = fruta9 * 1.85
fruta10 = int(input('Digite a quantidade de Carambola que deseja comprar: '))
valordacompra10 = fruta10 * 1.95
res = (valordacompra + valordacompra2 + valordacompra3 + valordacompra4 + valordacompra5 + valordacompra6 + valordacompra7 + valordacompra8 + valordacompra9 + valordacompra10)
print('A sua compra de frutas da semana deu um total de: {} reais'.format(res))




