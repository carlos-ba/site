#coding: utf-8

# lista = ['Carlos', 1, 'Gustavo']
# print(type(lista))
# print(len(lista))
# print(lista[2])
#
# for i in lista:
#     print(i)
from collections import Counter

dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}
print(type(dados_cliente))
print(dados_cliente)
print(dados_cliente['Telefone'])

arquivo = open('dados.txt')
linha = (arquivo.readline())
counter = Counter(linha)
print(counter)
nrit = counter[';']
col=[]
linhadados={}
# print(linha)
# print(len(linha))
for linha in arquivo:
    idlinha = linha.split(';')[0]
    if idlinha == '2':
        print('achei')
        for i in range(nrit):
            col.append((linha.split(';')[i]))
        nrcol = len(col)
        # col2 = (linha.split(';')[2])
        # col3 = (linha.split(';')[3])
        # col4 = (linha.split(';')[4])
        # col5 = (linha.split(';')[5])
        # col6 = (linha.split(';')[6])
        # col6 = col6[0:(len(col6) - 1)]  # para retirar o caracter especial \n
        # linhadados = {col[1].split(':')[0]: col[1].split(':')[1], col[2].split(':')[0]: col[2].split(':')[1],
        #               col[3].split(':')[0]: col[3].split(':')[1],
        #               col[4].split(':')[0]: col[4].split(':')[1], col[5].split(':')[0]: col[5].split(':')[1],
        #               col[6].split(':')[0]: col[6].split(':')[1]}
        for i1 in range(1, nrcol):
            linhadados[col[i1].split(':')[0]] = col[i1].split(':')[1]
        #
        idcoluna = 'Congelados'
        print(linhadados[idcoluna])
        # a = linhadados[idcoluna]
        # print(type(linhadados))

        # if a <= '1400':
        #     print('O resultado é: achado')
        # else:
        #     print('não tem na tabela')
    # else:
    #     print('não achei', idlinha)

    # print(linha.split(';')[1])
    # print(len(linha))
