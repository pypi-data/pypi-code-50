from tkinter import *
import tkinter as tk
from tkinter import ttk
from ler_novo import *
import tkinter.font as tkfont
from functools import reduce




# teste = {}
# dicionario = dict(teste)
# dicionario[event.widget] = event.widget.get()

def clicouGravar(event=None):
    # pegar os valores selecionados no combo menos o ultimo
    listaDeEscolhasDoCombo=[]
    for numero in range(len(listaCombo[:-1])):
            listaDeEscolhasDoCombo.append(listaCombo[numero].get())
    # print('lista de escolha combo = ',listaDeEscolhasDoCombo)
    # pegar os valore no listbox


    listaDeEscolhasDolistbox=[]
    for x in range(listbox.size()):
        listaDeEscolhasDolistbox.append(listbox.get (x, last=None ))
    # print(listaDeEscolhasDolistbox)

    habilidades = str(reduce(lambda x, y: x + " , " + y, listaDeEscolhasDolistbox))

    listaGravar=listaDeEscolhasDoCombo[:]
    listaGravar.append(habilidades)
    listaGravarFinal=[]
    listaGravarFinal.append(listaGravar)

    df = pd.DataFrame(listaGravarFinal, columns=lista[0])
    print(df)



    writer =pd.ExcelWriter('c:/3.xlsx',mode='w')
    df.to_excel(writer,index=False,sheet_name = 'dados')

    writer.save()

def quit(x):
    exit()

def clicouAdicionar(event=None):
    if listaCombo[-1].get()!='':
        listbox.insert(END,(listaCombo[-1].get()))
        listaCombo[-1].set('')



def clicouDelete(event=None):
    # selected = listbox.get(listbox.curselection())
    listbox.delete(tk.ANCHOR)



def filtra(lista,listaescolha):

    tamanho_lista_escolha=0
    for x in listaescolha:
        if (x!=''):
            tamanho_lista_escolha=tamanho_lista_escolha+1



    # retorna todas as linhas de uma lista que detem o valor passado naquela posição
    novalistaAtualizada=[]
    for linha in lista:
        conta=0
        # print('tamanho de lista escolha=', tamanho_lista_escolha)
        for xx in range(tamanho_lista_escolha):
            # print('xx=',xx)
            # print('linha=',linha[xx])
            # print('lista escolha',listaescolha[xx])

            if linha[xx]==listaescolha[xx]:
                conta=conta+1
                # continue
        if conta==tamanho_lista_escolha:
            novalistaAtualizada.append(linha)







    return novalistaAtualizada



def on_actiont():
    print("asdaasd")
    pass



def on_select(event=None):


    for c in range(len(listaCombo)):
        if c<(len(listaCombo)-1):
            # ao encontrar o combo em questao
            if event.widget==listaCombo[c]:
                #zerar todos daquele combo pra frente
                for s in listaCombo[c+1:]:
                    s.set('')

    listaDeEscolhasDoCombo=[]
    # transforma a lista combo em uma lista normal(string)
    for numero in range(len(listaCombo)):
            listaDeEscolhasDoCombo.append(listaCombo[numero].get())
    # print('lista de escolha combo = ',listaDeEscolhasDoCombo)


    novalistaFiltrada = (filtra(lista[1:], listaDeEscolhasDoCombo))


    # percorre a lista com os endereços dos combos
    # e compara com o evento atual
    for c in range(len(listaCombo)):
        if c<(len(listaCombo)-1):
            # ao encontrar o combo em questao
            if event.widget==listaCombo[c]:
                #zerar todos daquele combo pra frente
                for s in listaCombo[c+1:]:
            # preenche o proximo combo com a proxima coluna
                    coluna = percorre_por_coluna(c + 1, novalistaFiltrada)
                    coluna = remove_repetidos(coluna)
                    listaCombo[c + 1]['values'] = (coluna[:])





# TODO file
file='c:/11.xlsx'
lista=ler_arquivo_para_lista(file)





root =tk.Tk()
root.title("Ti Fora da Caixa")
# root.geometry('600x500')
root.attributes("-fullscreen", True)
# root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.bind("<Escape>", quit)



tab_control = ttk.Notebook(root)

aba2 = ttk.Frame(tab_control)
aba2.config(cursor="circle")
tab_control.add(aba2, text = "MONTAGEM PLANO DE AULAS")
aba2.place(relx=0.01, rely=0.1, relheight=0.88, relwidth = 0.95)

lb0 = Label(aba2, text= '')
lb0.grid(column=1, row=10)







botaoAdicionar = tk.Button(aba2, text="Adicionar Item",bg="green",font=("Arial",10,"bold"),fg="white")
botaoAdicionar.bind('<Button-1>', clicouAdicionar)
botaoAdicionar.grid(column=0, row=15)
botaoAdicionar.grid(padx=10, pady=1)

# sticky=tk.W+tk.E

listbox = tk.Listbox(aba2,width=185)
listbox.grid(column=1, row=16,sticky=tk.W+tk.E)
listbox.place(relx=0.01, rely=0.342, relheight=0.57686, relwidth = 0.95)
listbox.configure(disabledforeground="#a3a3a3")


delete = tk.Button(aba2, text="   Delete item  ",bg="red",font=("Arial",10,"bold"),fg="white")
delete.bind('<Button-1>', clicouDelete)
delete.grid(column=0, row=17 )
delete.grid(padx=10, pady=1)
# Label(aba2, text="First").grid(row=15)

gravar = tk.Button(aba2, text="   Gravar em planilha  ",bg="blue",font=("Arial",10,"bold"),fg="white")
gravar.bind('<Button-1>', clicouGravar)
gravar.grid(column=0, row=18 )









# button.pack()




coluna0=percorre_por_coluna(0,lista)
coluna0=remove_repetidos(coluna0)
listaCombo=[]


inicial = ttk.Combobox(aba2, width=120, font="Verdana 10 bold" , values=(coluna0[1:]))
inicial.bind('<<ComboboxSelected>>', on_select)
inicial.grid(column=1, row=0)
inicial.grid(padx=10, pady=1)
inicial.grid(sticky=tk.W+tk.E)
listaCombo.append(inicial)
# inicial.bind('<Button-1>', clicou)



#encutar e concaternar a lista para os labels e combos
listaConcatenada=[]
for linha in lista:
    ultimo2=linha[-1]
    # print('ultimo',ultimo2)
    novaLinha=linha[:-1]
    novaLinha[-1]=novaLinha[-1]+' / '+ultimo2
    listaConcatenada.append(novaLinha)


lista=listaConcatenada





conta=0
# preenche todos os combos e labels
for x in lista[0]: #lista[0] tem os titulos das colunas que serao os valores do label
    # numero = (lista[0].index(x))
    lb = Label(aba2, text= x)
    lb.grid(column=0, row=conta)

    conta +=1

    if conta<len(lista[0]):
        cm1 = ttk.Combobox(aba2, width=100, font="Verdana 10" )
        cm1.bind('<<ComboboxSelected>>', on_select)
        cm1.grid(column=1, row=conta)
        cm1.grid(padx=10, pady=1)
        cm1.grid(sticky=tk.W + tk.E)
        listaCombo.append(cm1)

        # cm1.bind('<Configure>', on_combo_configure)
        # cm1.bind('<Button-1>', clicou)

#TODO largura
# listaCombo[0].config(width=30)
#
# listaCombo[0].grid(sticky=tk.W)
#
#
# listaCombo[-1].config(width=120)


# cm1 = ttk.Combobox(aba2,postcommand = on_actiont ,textvariable="1",width=40,values=(coluna0[1:]))

# cm1.bind('<Button-1>', on_select)
# cm1.bind('<Key>', on_select)







tab_control.pack(fill=BOTH, expand=True)
# tab_control.pack(expand=1, fill='both')
root.mainloop()