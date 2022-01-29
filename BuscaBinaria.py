import struct
from io import SEEK_SET

import sys

procurado = '26112000'
tamanhoRegistro = 300


def tamanho_arquivo(arquivo):

    tamanho = arquivo.seek(0, 2)
    print('O arquvio tem ', tamanho, 'Bytes')
    return tamanho

def busca(inicio, final, procurado):
    meio = (inicio + final) // 2
    arquivo.seek(meio*tamanhoRegistro, SEEK_SET)
    
    linha = arquivo.readline()
    endereco = str(linha[0:300])
    cep = str( linha[290:298])
    
    if (cep == procurado):
        print ('CEP Encontrado')
        print (endereco)
    elif (procurado < cep):
        final = meio-1
        busca(inicio, final, procurado)
    elif (procurado > cep):
        inicio = meio+1
        busca(inicio, final, procurado)
    

arquivo = open('cep_ordenado.dat','r')

print('Arquivo aberto')

tamanho = tamanho_arquivo(arquivo)

quantidadeRegistro = int(tamanho / tamanhoRegistro)

print(quantidadeRegistro, 'Registros')

inicio = 0
final = int(quantidadeRegistro - 1)

busca(inicio, final, procurado)

arquivo.close()

print('Arquivo fechado')
