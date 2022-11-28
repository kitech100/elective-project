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

def printVerticalSpaces(n):
    for x in range(n):
        print()

def display_main_menu():
    os.system("cls")

    printVerticalSpaces(2)
    print('ML Regents'.upper())
    printVerticalSpaces(1)

    print('Members:')
    print('\tEchemane, Eric B.')
    print('\tBautista, Mark Alcel C.')

    printVerticalSpaces(1)

    print('Main menu:')
    print('\t[1] Choose ML Algorithm to display')
    print('\t[2] Display all ML Algorithm')
    print('\t[3] Exit')

    printVerticalSpaces(1)

    chosen_menu = input('input: ')

    if chosen_menu == '1':
        choose_algorithm()
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
    printVerticalSpaces(2)
    print('ML Algorithms'.upper())
    printVerticalSpaces(1)

    for key,algo in algorithms.items():
        print(algo['title'].upper())

    input('\nenter any key to return...')
    display_main_menu()

def choose_algorithm():
    os.system('cls')
    printVerticalSpaces(2)
    print('Choose algorithm to display:'.upper())
    
    print('\t[a] Classification Algorithm')
    print('\t[b] Regression Algorithm')
    print('\t[c] Clustering Algorithm')
    print('\t[d] KNN Algorithm')
    print('\t[e] Main menu')

    chosen_algo = input('input: ')

    if chosen_algo == 'a':
        print('you choose a')
    elif chosen_algo == 'b':
        print('you choose b')
    elif chosen_algo == 'c':
        print('you choose c')
    elif chosen_algo == 'd':
        print('you choose d')
    elif chosen_algo == 'e':
        display_main_menu()
    else:
        print('invalid input\n')

    input('\nenter any key to return...')
    choose_algorithm()

display_main_menu()