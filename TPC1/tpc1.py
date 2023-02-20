import math
import matplotlib.pyplot as plt

# 1.
def readFile(name):
    file = open(name, 'r')
    content = file.read()
    print(content)
    file.close()

# 2.
def saveFile(name):
    file = open(name, 'r')
    content = []

    for line in file:
        temp = line.strip().split(",")
        content.append(temp)

    #print(content)
    return content[1:]

# 3.
def sicknessPerGender(name):
    content = saveFile(name)
    sick = 0
    total = -1
    male = 0
    female = 0

    for line in content:
        total += 1
        if (line[5] == '1'):
            sick += 1
            if (line[1] == 'M'):
                male += 1
            elif (line[1] == 'F'):
                female += 1

    result = []
    result.append(("Doentes", sick))
    result.append(("Homens", male))
    result.append(("Mulheres", female))

    return result

# 4.
def sicknessPerAge(name):
    content = saveFile(name)
    
    sick = 0
    total = -1
    ages = [0 for i in range(11)]

    for line in content:
        total +=1
        if (line[5] == '1'):
            sick += 1
            age = int(line[0])
            x = (age - 30) // 5
            if (0 <= x <= 14):
                ages[x] += 1

    result = []
    result.append(("Doentes", sick))

    for i in range(11):
        value = (i * 5) + 35
        result.append((value, ages[i]))

    return result

# 5.
def sicknessPerColesterol(name):
    content = saveFile(name)

    min = 1000
    max = 0

    for line in content:
        x = int(line[3])

        if (x < min and x != 0):
            min = x
        elif (x > max):
            max = x

    indexes = math.ceil((max - min) / 10)

    sick = 0
    total = -1
    people = [0 for i in range(indexes)]

    for line in content:
        total +=1
        if (line[5] == '1' and line[3] != '0'):
            sick += 1
            col = int(line[3])
            x = (col - min) // 10
            if (0 <= x <= indexes):
                people[x] += 1

    result = []
    result.append(("Doentes", sick))

    for i in range(indexes):
        value = (i * 10) + min
        result.append((value, people[i]))

    return result

# 6.
def table(data):

    width = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
    
    print('-' * (sum(width) + 7))
    print('|', end='')
    for i in range(len(data[0])):
        print(' {:{}} |'.format(str(data[0][i]), width[i]), end='')
    print('\n' + '-' * (sum(width) + 7))
    
    for row in data[1:]:
        print('|', end='')
        for i in range(len(row)):
            print(' {:{}} |'.format(str(row[i]), width[i]), end='')
        print('\n' + '-' * (sum(width) + 7))

    labels = [item[0] for item in data[1:]]
    values = [item[1] for item in data[1:]]

    # Create a histogram
    fig, axs = plt.subplots()
    axs.bar(labels, values, width=1.5)
    axs.set_title('Número de Doentes')
    axs.set_xlabel('Doentes')
    axs.set_ylabel('Valores')

    # Create a pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels=labels, autopct='%1.1f%%')
    ax2.set_title("Proporção da Doença")

    plt.show()

# 7. 
def ui(name):
    while True:
        print("\n\n-- Doença Cardíaca --")
        print("| 1. Doentes por sexo")
        print("| 2. Doentes por escalão etário")
        print("| 3. Doentes por valor de colesterol")
        print("| 0. Exit\n---------------------\n\n")
        choice = input("Insere uma escolha  (0-3): ")
        
        if choice == '1':
            table(sicknessPerGender(name))
            
        elif choice == '2':
            table(sicknessPerAge(name))
            
        elif choice == '3':
            table(sicknessPerColesterol(name))
            
        elif choice == '0':
            print("A sair do programa...")
            break
        else:
            print("Escolha inválida") 

ui("myheart.csv")