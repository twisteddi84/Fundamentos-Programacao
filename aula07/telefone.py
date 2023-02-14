def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contatos):
    list = {}
    partName = input('Parte do nome: ')
    for numb, name in contatos.items():
        if partName.lower() in name.lower():
            list[numb] = name
    print('Correspondências:')
    print(list)

def addContact(contactos):
    nome = input("Nome do contacto:")
    numero = input("Número do contacto:")
    while True:
        try:
            numero = int(numero)
            break
        except:
            print("Número Inválido")
            numero = input("Número do contacto:")
    numero = str(numero)
    contactos[numero] = nome
    return contactos

def removeContact(contactos):
    while True:
        numero = input("Número a remover:")
        try:
            test = int(numero)
            if numero not in contactos:
                print("Número não está nos contactos.")
            else:
                break
        except:
            print("Número Inválido")
    del contactos[numero]
    return contactos

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

def findNum(contatos):
    numb = input("Número: ")
    if numb not in contatos:
        print(numb)
    else:
        print(contatos[numb])


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op =="A":
            listContacts(addContact(contactos))
        elif op =="R":
            listContacts(removeContact(contactos))
        elif op == 'N':
            findNum(contactos)
        elif op == 'P':
            filterPartName(contactos)
        else:
            print("Não implementado!")

main()

