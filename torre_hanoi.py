#
# Algoritmo de resolução da Torre de Hanoi
#

def mover(discos, origem = 'Torre 1', destino = 'Torre 2', auxiliar = 'Torre 3', movimentos = []):

    if discos == 1:
        movimentos.append('Mova da ' + origem + ' para a ' + destino)
        return movimentos

    mover(discos - 1, origem, auxiliar, destino, movimentos)
    movimentos.append('Mova da ' + origem + ' para a ' + destino)

    mover(discos - 1, auxiliar, destino, origem, movimentos)

    return movimentos

# main

n = int(input('\nQual o número de discos? '))
movimentos = mover(n)

print('\nExecução em', len(movimentos), 'movimentos')
print('-'*64)

for acao in movimentos:
    resposta = input(acao + '.' + ' '*10 + 'ENTER=Seguir, P=Parar ')
    if resposta == 'P' or resposta == 'p':
        break

print('-'*64)
