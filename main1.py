# coding: utf-8

from collections import Counter

arquivo = open('dados1.txt')
linhaCk = (arquivo.readline())
counter = Counter(linhaCk)
nrcol = counter[';']
col = []
linhadados = {}

for linha in arquivo:
    idlinha = (linha.split(';')[0]).split(':')[1]
    if idlinha == '2':

        for i in range(nrcol):
            col.append((linha.split(';')[i]))

        for i1 in range(nrcol):
            linhadados[col[i1].split(':')[0]] = col[i1].split(':')[1]

        idcoluna = 'Preparo'
        print(linhadados[idcoluna])
