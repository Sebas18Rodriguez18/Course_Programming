import os
import time

BLACK = '\033[30m'
RED = '\033[91m'
BLUE = '\033[34m'
RESET = '\033[0m'
GREEN = '\033[92m'
YELLOW = '\033[33m'
VIOLET = '\033[35m'
COMMENTED = '\033[90m'
GREY_UNDERLINE = '\033[47m'
HIGHLIGHTED = '\033[7m'
BLUE_UNDERLINE = '\033[44m'
ENCAPSULATED = '\033[53m'
GREEN_UNDERLINE = '\033[42m'
UNDERLINED_DOUBLE = '\033[21m'
YELLOW_UNDERLINE = '\033[43m'
DARK_UNDERLINE = '\033[40m'
PINK_UNDERLINE = '\033[45m'
RED_UNDERLINE = '\033[41m'
CROSSED_OUT = '\033[9m'
UNDERLINED = '\033[4m'
ITALICS = '\033[3m'
GREY = '\033[37m'
 #*********************************************************************************************************************
option = 0
option2 = 0
product = []
quantity = []
cost = []

def menu():
    os.system('cls')
    print(f"{UNDERLINED}{ITALICS}{YELLOW} MENU OF FRUITS INVENTORY{RESET}")
    print()
    print(f"{GREEN}1.{RESET}{VIOLET} ADD PRODUCT{RESET}")
    print(f"{GREEN}2.{RESET}{VIOLET} UPDATE FRUITS")
    print(f"{GREEN}3.{RESET}{VIOLET} DELETE PRODUCT")
    print(f"{GREEN}4.{RESET}{VIOLET} VIEW PRODUCT")
    print(f"{GREEN}5.{RESET}{VIOLET} LIST PRODUCT")
    print(f"{GREEN}6.{RESET}{VIOLET} CALCULATE INVENTORY COST")
    print(f"{GREEN}7. {RESET}{RED}{UNDERLINED_DOUBLE}FINISH{RESET}")

def addProduct(product, quantity, cost):
    print('Desea agregar un producto? ')
    option2 = int(input(f'{YELLOW}Digite 1 si desea agregar un producto.\nDigite 2 si no desea agregar nada.\nRespuesta:{RESET} '))
    while option2 == 1:
        fruit = input('Ingrese el producto a agregar: ').upper()
        amount = int(input('Ingrese la cantidad del producto que agregó: '))
        worth = int(input('Ingrese el valor unitario del producto que agregó: '))
        product.append(fruit)
        quantity.append(amount)
        cost.append(worth)
        os.system('cls')
        print('Desea agregar un producto? ')
        option2 = int(input(f'{YELLOW}Digite 1 si desea agregar un producto.\nDigite 2 si no desea agregar nada.\nRespuesta: {RESET}'))
    print('Las frutas han sido adicionados correctamente')
    print()

def updateProduct(product, quantity, cost):
    option2 = int(input(f'{YELLOW}Digite 1 si desea actualizar un producto.\nDigite 2 si no desea actualizar nada.\nRespuesta: {RESET}'))
    while option2 == 1:
        fruit = input('Ingrese el nombre del producto que desea actualizar: ').upper()
        if fruit in product:
            index = product.index(fruit)
            new_quantity = int(input('Ingrese la nueva cantidad: '))
            new_cost = int(input('Ingrese el nuevo costo unitario: '))
            quantity[index] = new_quantity
            cost[index] = new_cost
            os.system('cls')
            print('Producto actualizado')
        else:
            print('Producto no encontrado')
            os.system('cls')
        option2 = int(input(f'{YELLOW}Digite 1 si desea actualizar un producto.\nDigite 2 si no desea actualizar nada.\nRespuesta: {RESET}'))

def deleteProduct(product, quantity, cost):
    option2 = int(input('Digite 1 si desea borrar un producto.\nDigite 2 si no desea borrar nada.\nRespuesta: '))
    while option2 == 1:
        delete = input('Ingrese el nombre del producto que desea eliminar: ').upper()
        if delete in product:
            index = product.index(delete)
            product.pop(index)
            quantity.pop(index)
            cost.pop(index)
            os.system('cls')
            print('Producto eliminado exitosamente')
        else:
            print('Producto no encontrado')
            os.system('cls')
        option2 = int(input(f'{YELLOW}Digite 1 si desea borrar un producto.\nDigite 2 si no desea borrar nada.\nRespuesta: {RESET}'))

def viewProduct(product, quantity, cost):
    view = input('Ingrese el nombre del producto que desea ver: ').upper()
    if view in product:
        index = product.index(view)
        print(f'Producto: {product[index]}')
        print(f'Cantidad: {quantity[index]}')
        print(f'Valor unitario: {cost[index]}')
        print(f'Valor total del producto: {quantity[index] * cost[index]}')
    else:
        print('Producto no encontrado')

def listProduct(product, quantity, cost):
    if len(product) == 0:
        print('No hay productos en el inventario')
    else:
        print('Lista de productos:')
        for i in range(len(product)):
            print(f"Producto: {product[i]}, Cantidad: {quantity[i]}, Costo unitario: {cost[i]}")

def calculateInventory(quantity, cost):
    totalCost = 0
    for i in range(len(quantity)):
        totalCost += quantity[i] * cost[i]
    print(f'Costo total del inventario: {totalCost}')

# *********************************************************************************************************************************
while option != 7:
    menu()
    print()
    option = int(input(f'{ENCAPSULATED}Digite la sección del menu que desea ver: {RESET}'))

    match option:
        case 1:
            os.system('cls')
            print(f"{GREEN}{ITALICS}ADD FRUITS{RESET}")
            print()
            addProduct(product, quantity, cost)
            print()
            input(f"{BLUE}{ITALICS}ENTER TO CONTINUE{RESET}")
        case 2:
            os.system('cls')
            print(f"{GREEN}{ITALICS}UPDATE PRODUCT{RESET}")
            print()
            updateProduct(product, quantity, cost)
            print()
            input(f"{BLUE}{ITALICS}ENTER TO CONTINUE{RESET}")
        case 3:
            os.system('cls')
            print(f"{GREEN}{ITALICS}DELETE PRODUCT{RESET}")
            print()
            deleteProduct(product, quantity, cost)
            print()
            input(f"{BLUE}{ITALICS}ENTER TO CONTINUE{RESET}")
        case 4:
            os.system('cls')
            print(f"{GREEN}{ITALICS}VIEW PRODUCT{RESET}")
            print()
            viewProduct(product, quantity, cost)
            print()
            input(f"{BLUE}{ITALICS}ENTER TO CONTINUE{RESET}")
        case 5:
            os.system('cls')
            print(f"{GREEN}{ITALICS}LIST PRODUCT{RESET}")
            print()
            listProduct(product, quantity, cost)
            print()
            input(f"{BLUE}{ITALICS}ENTER TO CONTINUE{RESET}")
        case 6:
            os.system('cls')
            print(f"{GREEN}{ITALICS}CALCULATE INVENTORY COST{RESET}")
            print()
            calculateInventory(quantity, cost)
            print()
            input(f"{BLUE}{ITALICS}ENTER TO CONTINUE{RESET}")
        case 7:
            for i in range(5, 0, -1):
                os.system('cls')
                print(f"{DARK_UNDERLINE}{RED}Finish in {i} seconds...{RESET}")
                time.sleep(1)

os.system('cls')
print(f"{RED}{DARK_UNDERLINE} You have logged out of the system {RESET}")