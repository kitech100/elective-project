import os

algorithms = {
    "classification": {
        "title": "classification",
        "description": """
        The Classification algorithm is a Supervised Learning technique that is used to identify the category of new observations on the basis of training data. In Classification, a program learns from the given dataset or observations and then classifies new observation into a number of classes or groups. Such as, Yes or No, 0 or 1, Spam or Not Spam, cat or dog, etc. Classes can be called as targets/labels or categories. Unlike regression, the output variable of Classification is a category, not a value, such as "Green or Blue", "fruit or animal", etc. Since the Classification algorithm is a Supervised learning technique, hence it takes labeled input data, which means it contains input with the corresponding output.
        """
    },
    "regression": {
        "title": "regression",
        "description": """
        Regression is another important and broadly used statistical and machine learning tool. The key objective of regression-based tasks is to predict output labels or responses which are continues numeric values, for the given input data. The output will be based on what the model has learned in training phase. Basically, regression models use the input data features (independent variables) and their corresponding continuous numeric output values (dependent or outcome variables) to learn specific association between inputs and corresponding outputs.
        """
    },
    "clustering": {
        "title": "clustering",
        "description": """
        Clustering or cluster analysis is a machine learning technique, which groups the unlabelled dataset. It can be defined as "A way of grouping the data points into different clusters, consisting of similar data points. The objects with the possible similarities remain in a group that has less or no similarities with another group." It does it by finding some similar patterns in the unlabelled dataset such as shape, size, color behavior, etc., and divides them as per the presence and absence of those similar patterns. It is an unsupervised learning method, hence no supervision is provided to the algorithm, and it deals with the unlabeled dataset.
        """
    },
    "KNN": {
        "title": "KNN",
        "description": """
        The k-nearest neighbors (KNN) algorithm is a data classification method for estimating the likelihood that a data point will become a member of one group or another based on what group the data points nearest to it belong to. The k-nearest neighbor algorithm is a type of supervised machine learning algorithm used to solve classification and regression problems. However, it's mainly used for classification problems. KNN is a lazy learning and non-parametric algorithm. It's called a lazy learning algorithm or lazy learner because it doesn't perform any training when you supply the training data. Instead, it just stores the data during the training time and doesn't perform any calculations. It doesn't build a model until a query is performed on the dataset. This makes KNN ideal for data mining.
        """
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
    print('\t[e] go back to main menu')

    chosen_algo = input('input: ')

    if chosen_algo == 'a':
        display_classification_algorithm()
    elif chosen_algo == 'b':
        display_regression_algorithm()
    elif chosen_algo == 'c':
        display_clustering_algorithm()
    elif chosen_algo == 'd':
        display_KNN_algorithm()
    elif chosen_algo == 'e':
        display_main_menu()
    else:
        print('invalid input\n')

    input('\nenter any key to return...')
    choose_algorithm()
    
#  ================================= Algorithms ==================================

def display_classification_algorithm():
    os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['classification']
    title = (algo["title"]+" algorithm").upper()
    print(title)
    print(algo["description"])

    print('^')
    print('• class A         🔵     ⁄')
    print('•      🔵              ⁄')
    print('• 🔵 🔵    🔵  🔵    ⁄  🔴')
    print('•   🔵   🔵        ⁄  🔴  🔴    🔴')
    print('•       🔵   🔵  ⁄   🔴   🔴  🔴 ')
    print('• 🔵   🔵      ⁄   🔴  🔴 ')
    print('• 🔵  🔵     ⁄  🔴  Class B ')
    print('• 🔵       ⁄  🔴')
    print('•   🔵   ⁄   🔴 🔴 🔴 ')
    print('•      ⁄  🔴')
    print('•    ⁄ 🔴')
    print('•  ⁄')
    print('• • • • • • • • • • • • • • • • • • >')
    
    input('\nenter any key to return...')
    choose_algorithm()

def display_regression_algorithm():
    os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['regression']
    title = (algo["title"]+" algorithm").upper()
    print(title)
    print(algo["description"])

    input('\nenter any key to return...')
    choose_algorithm()

def display_clustering_algorithm():
    os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['clustering']
    title = (algo["title"]+" algorithm").upper()
    print(title)
    print(algo["description"])

    input('\nenter any key to return...')
    choose_algorithm()

def display_KNN_algorithm():
    os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['KNN']
    title = (algo["title"]+" algorithm").upper()
    print(title)
    print(algo["description"])

    input('\nenter any key to return...')
    choose_algorithm()

# display_main_menu()
display_classification_algorithm()