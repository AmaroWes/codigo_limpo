from sys import exit
from time import sleep

# lista com o nome das cidades e estados
cidades = list()
estados = list()

# função para verificar se existe algo dentro da lista cidades
def verifica_cidades():
    try:
        cidades[0] = cidades[0]
        return True
    except IndexError:
        print("Você ainda não possui nenhuma cidade cadastrada!\n")
        sleep(1)
        return False

# função que recebe o nome da cidade e verifca se ela consta na lista
def buscador_cidades(old):
    for i in range(len(cidades)):
        if old == cidades[i]:
            return True
        elif old == estados[i]:
            return True
    return False

# função para adicionar a cidade a lista
def add_cidade():
    cidade = input("Qual cidade você gostaria de cadastrar: ").upper()
    estado = input("Qual o estado para essa cidade: ").upper()
    if not buscador_cidades(cidade):
        cidades.append(cidade)
        estados.append(estado)
        print(f"Cidade {cidade} e estado {estado} cadastrada com sucesso!\n")
        sleep(1)
    else:
        print(f"A cidade {cidade} já consta na nossa DB!\n")
        sleep(1)

# função para listar a cidade
def list_cidade():
    if verifica_cidades():
        for i in range(len(cidades)):
            print(f"{i} {cidades[i]} {estados[i]}")
        print('\n')

# função para listar as cidades de um determinado estado
def list_cidade_estado():
    if verifica_cidades():
        aux = input(f"Informe o estado: ").upper()
        for i in range(len(estados)):
            if aux == estados[i]:
                print(f"{cidades[i]}")
        print('\n')

# função para alterar a cidade
def alt_cidade():
    if verifica_cidades():
        old = input("Informe o nome da cidade a ser alterada: ").upper()
        if buscador_cidades(old):
            new = input("Informe o novo nome da cidade: ").upper()
            for i in range(len(cidades)):
                if old == cidades[i]:
                    cidades[i] = new
                    print("Cidade alterada com sucesso\n")
        else:
            print("A cidade informada não consta na nossa DB!\n")

# função para alterar um estado
def alt_estado():
    if verifica_cidades():
        old = input("Informe o nome do estado a ser alterada: ").upper()
        if buscador_cidades(old):
            new = input("Informe o novo nome do estado: ").upper()
            for i in range(len(estados)):
                if old == estados[i]:
                    estados[i] = new
            print("Estados alterados com sucesso\n")
        else:
            print("O estado informado não consta na nossa DB!\n")

# submenu
def menu_exc():
    try:
        print(f"1 - Excluir cidade")
        print(f"2 - Excluir estado")
        aux = int(input("Informe a sua escolha: "))
        if aux == 1:
            exc_cidade()
        elif aux == 2:
            exc_estado()
        else:
            print("\n")
            print("O valor informado não é uma opção, tente novamente\n")
            sleep(1)
    except ValueError:
        print('\n')
        print("Por gentileza informe o número da opção desejada!\n")
        sleep(1)

# função para excluir a cidade            
def exc_cidade():
    if verifica_cidades():
        old = input("Informe o nome da cidade a ser excluida: ").upper()
        if buscador_cidades(old):
            for i in range(len(cidades)):
                if old == cidades[i]:
                    print(f"Cidade {cidades[i]} excluida com sucesso!\n")
                    cidades.remove(cidades[i])
                    estados.remove(estados[i])

def exc_estado():
    if verifica_cidades():
        old = input("Informe o nome do estado a ser excluida: ").upper()
        aux_list = list()
        cont = 0
        if buscador_cidades(old):
            for i in range(len(estados)):
                if old == estados[i]:
                    aux_list.append(int(i))
            for n in range(len(aux_list)):
                print(f"Estado {estados[aux_list[n] - cont]} excluido com sucesso!\n")
                cidades.remove(cidades[aux_list[n - cont]])
                estados.remove(estados[aux_list[n - cont]])
                cont += 1

# função para renderizar uma interface improvisada
def interface():
    print("0 - Finalizar o programa!")
    print("1 - Adicionar cidades e estados")
    print("2 - Listar as cidades e seus respectivos estados")
    print("3 - Alterar o nome de alguma cidade")
    print("4 - Alterar o nome de um estado")
    print("5 - Listar todas cidades de um terminado estado")
    print("6 - Retirar da lista uma cidade ou estado")

# função para fechar o programa
def fechar():
    print("Ok, até uma outra oportunidade")
    exit()

# função para controlar o menu de opções
def op_menu_controle(val):
    if val == 0:
        fechar()
    elif val == 1:
        add_cidade()
    elif val == 2:
        list_cidade()
    elif val == 3:
        alt_cidade()
    elif val == 4:
        alt_estado()
    elif val == 5:
        list_cidade_estado()
    elif val == 6:
        menu_exc()
    else:
        print("O valor passado não é uma opção, tente novamente\n")

# o menu de opções propriamente dito
def menu():
    while True:
        try:
            interface()
            val = int(input("O que você gostaria de fazer? "))
            print('\n')
            op_menu_controle(val)
        except ValueError:
            print('\n')
            print("Por gentileza informe o número da opção desejada!\n")
            sleep(1)

# profilaxia
if __name__ == "__main__":
    menu()