# coding: utf-8
# import pandas as pd

import sys
# sys.path.append('C:/pandas2/uso2')


from uso2 import pandas as pd



def nada():
    pass


    # numero de linhas
    # print(len(df[df.columns[0]]))
    # numero de colunas
    # print(len(df.columns))

    # linha 1 coluna1
    # print((df[df.columns[0]][0]))

    # linha 2 coluna1
    # print((df[df.columns[0]][1]))

    # linha 3 coluna1
    # print((df[df.columns[0]][2]))

    # linha 1 coluna 2


    # linha 1 coluna2
    # print((df[df.columns[1]][0]))

    # toda a linha 1




def ler_arquivo_para_lista(file):


    df=pd.read_excel(file)

    numeroLinhas=len(df[df.columns])

    todaLista=[]
    listaLinha=[]

    # pega os nomes das colunas e grava na primeira posição da lista
    for x in df.columns:
        listaLinha.append(x)
    todaLista.append(listaLinha)

    # anda em todas as linhas
    for linha in range(numeroLinhas):
        listaLinha = []
        numeroColunas=df.columns
        # anda em todas as colunas da linha
        for coluna in range(len(numeroColunas)):
            listaLinha.append((df[df.columns[coluna]][linha]))
        todaLista.append(listaLinha)
    return todaLista


def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    # l.sort()
    return l

def percorre_por_coluna(coluna,lista):
    novaLista=[]
    for x in lista:
        # print()
        novaLista.append(x[coluna])
    # novaLista=remove_repetidos(novaLista)

    return novaLista




# lista=ler_arquivo_para_lista(file)
# coluna0=percorre_por_coluna(0,lista)
# print(coluna0)


# procurar item dentro de uma lista
# try:
#   print(lista[3].index('teste3'))
# except:
#   print("An exception occurred")




# para gravar em novao arquivo
# lista=ler_arquivo_para_lista('c:/1.xlsx')
# print(lista)
# lista=[(1,2,3,4,5),(1,2,3,4,5)]
# df = pd.DataFrame(lista[1:], columns=lista[0])
#
# print('deu certo \n',df)
# df.to_excel('c:/3.xlsx',index=False)




# como bucar na lista??
# buscar no primeiro elemento se tiver guarda a nova lista
# buscar no segundo
#
#
#
#
# try:
#   print(todaLista[1].index('aldo'))
# except:
#   print("An exception occurred")
#
# print('aldo' in todaLista[1])

# adicionando itens sem repetir



# adiciona se nao repetido


# lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]
#
# lista = remove_repetidos(lista)
# print (lista)

