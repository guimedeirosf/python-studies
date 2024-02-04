

def adicionar_itens(lista: list):
    item = input("\nEscreva o nome do item a ser adicionaddo: ")
    lista.append(item)
    return

def remover_itens(lista: list):
    visualizar_lista(lista)
    remover = input("Escreva o número ddo item para remover:")
    remover = int(remover)
    tamanho_lista = len(lista)
    if remover > tamanho_lista or remover <=0:
        print("Escolha invalidad")
        return
    else:
        remover -= 1
        lista.remove(lista[remover])
        return

def visualizar_lista(lista: list):
    print('\n######== Inicio da Lista==######')
    for i, item in enumerate(lista):
        print(f'{i+1} - {item}')
    print('######== Fim da Lista==######\n')
    return



def fuction_lista_compras(lista: list):
    display_lista = True
    while  display_lista:
        print("########################################")
        print("Escolha uma opção:")
        print("1. Adicionar item na lista de compras")
        print("2. Remover item na lista de compras")
        print("3. Visualizar lista de compras")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")
        escolha = int(escolha)
        if escolha == 1:
            adicionar_itens(lista)
        elif escolha == 2:
            remover_itens(lista)
        elif escolha == 3:
            visualizar_lista(lista)
        elif escolha ==  0:
            display_lista = False
        elif escolha not in (0,1,2,3):
            print("\nEscolha uma opção vália\n")


def nova_lista():
    nova_lista = input("Digite 1 para iniciar uma nova lista: ")
    nova_lista = int(nova_lista)
    if nova_lista == 1:
        return True
    return False

lista_compras = []

while nova_lista():
    lista_compras.clear()  
    fuction_lista_compras(lista = lista_compras)  