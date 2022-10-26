idade = int(input('Digite sua idade: '))
peso = int(input('Digite seu peso (em kg): '))
altura = int(input('Digite sua altura (em cm): '))

if idade > 18 and peso >= 60 and altura >= 160:
    print('Você está apto para servir ao Exército.')
else:
    print('Você não está apto para servir ao Exército.')