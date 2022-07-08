"""
estudando na pratica var e if, else, elif

"""

a = 'ir verificar'
b = 'voltar a dormir'
c = 'ficar olhando para o teto'

print('Voce acorda com sons de passos na entrada da sua casa')
print('A: ir verificar')
print('B: voltar a dormir')
print('C: ficar olhando para o teto')

escolha = input('O que deseja fazer? ')

if escolha == 'a':
    print('Por uma fresta na cortina voce ve dois homens de preto, e uma chuva '
          'torrencial caindo no quintal')

elif escolha == 'b':
    print('voce ouve tres fortes batidas em sua porta de madeira')
    print('do lado de fora vem uma voz grave dizendo "sabemos que esta ai, abra a porta" ')

    a = 'levantar e ir abrir a porta'
    b = 'fingir que nao ouviu'
    c = 'sair pela porta dos fundos'

    print('A: levantar e ir abrir a porta')
    print('B fingir que nao ouviu')
    print('C sair pela porta dos fundos')

    escolha = input('O que deseja fazer? ')

    if escolha == 'a':
        print('voce abre a porta, e ve dois homens parados em ternos pretos')
        a = 'seguir os homens'
        b = 'se negar a sair'
        c = 'correr para a porta dos fundos'

        print('Senhor, precisamos que venha com a gente urgentemente, sua vida corre perigo')
        print('A: seguir os homens')
        print('B: se negar a sair')
        print('c: correr para a porta dos fundos')

        escolha = input('o que deseja fazer?')

        if escolha == 'a':
            print('eles levam voce ate um carro preto')

        elif escolha == 'b':
            print('nao temos tempo, levaremos voce a forca')

        elif escolha == 'c':
            print('voce corre ate a porta dos fundos, e sai debaixo de uma garoa fina, caindo levemente no quintal')



    elif escolha == 'b':
        print('"abra ou iremos quebrar sua porta, este é o primeiro e ultimo aviso"')

    elif escolha == 'c':
        print('voce corre pra fora de casa, uma chuva fina cai sobre sua cabeca e voce logo comeca a ficar com frio')

elif escolha == 'c':
    print('voce percebe que alguem esta dando a volta na casa')
