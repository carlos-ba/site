# coding: utf-8

from arquivo.lerArquivo import lerarquivo

nomearq = input('Digite o nome do arquivo:')
chave = input('Digite a area: ')
coluna = input('Digite a coluna: ')

lerdd = lerarquivo(nomearq, chave)

print(lerdd.ler()[coluna])
