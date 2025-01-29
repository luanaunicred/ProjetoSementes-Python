nota1 = float(input('Informe a nota da primeira prova: '))
nota2 = float(input('Informe a nota da segunda prova: '))
nota3 = float(input('Informa a nota da terceira prova:'))

media = (nota1 + nota2 + nota3) / 3

if media < 5:
    print('Infelizmente sua média foi {} e você está reprovado. Nos vemos ano que vem.'.format(media))
elif 5 <= media <= 6:
    print('Atenção! Sua média foi {} e você está em recuperação. Estude mais!'.format(media))
else:
    print('Parabéns, sua média foi {} e por isso você está APROVADO!!!'.format(media))