import os

algorithms = {
    "classification": {
        "title": "classification"
    },
    "regression": {
        "title": "regression"
    },
    "clustering": {
        "title": "clustering"
    },
    "KNN": {
        "title": "KNN"
    },
}

def printSpaces(n):
    for x in range(n):
        print()

def display_main_menu():
    os.system("cls")

    printSpaces(2)
    print('ML Regents'.upper())
    printSpaces(1)

    print('Members:')
    print('\tEchemane, Eric B.')
    print('\tBautista, Mark Alcel C.')

    printSpaces(1)

    print('Main menu:')
    print('\t[1] Choose ML Algorithm to display')
    print('\t[2] Display all ML Algorithm')
    print('\t[3] Exit')

    printSpaces(1)

    chosen_menu = input('input: ')

    if chosen_menu == '1':
        print('you choose 1')
    elif chosen_menu == '2':
        display_all_algorithm()
    elif chosen_menu == '3':
        print('thank you!'.upper())
        exit()
    else:
        input('invalid input, enter any key to return...')
        display_main_menu()

def display_all_algorithm():
    os.system('cls')
    printSpaces(2)
    print('ML Algorithms'.upper())
    printSpaces(1)

    for key,algo in algorithms.items():
        print(algo['title'].upper())

    input('\nenter any key to return...')
    display_main_menu()

display_main_menu()