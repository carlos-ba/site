# coding: utf-8

from collections import Counter


class lerarquivo:
    def __init__(self, nomearq, chave):
        self.nomearq = nomearq
        self.chave = chave

    def ler(self):
        arquivo = open(self.nomearq)
        linhaCk = (arquivo.readline())
        counter = Counter(linhaCk)
        nrcol = counter[';']
        col = []
        linhadados = {}

        for linha in arquivo:
            idlinha = (linha.split(';')[0]).split(':')[1]
            if idlinha == self.chave:

                for i in range(nrcol):
                    col.append((linha.split(';')[i]))

                for i1 in range(nrcol):
                    linhadados[col[i1].split(':')[0]] = col[i1].split(':')[1]

        return linhadados
