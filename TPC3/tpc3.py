import re
import json

def saveFile(name):
    with open(name, 'r') as file:
        data = file.read().split('::::')

    data = [line.strip().split('::') for line in data]

    return data


# 1.
def perYear(name):
    data = saveFile(name)

    min = 2100
    max = 1000

    for line in data:
        if line is not None and len(line) > 1:  
            year_str = line[1][:4]
            if year_str.isdigit():
                year = int(year_str)

                if year > max:
                    max = year
                if year < min:
                    min = year

    indexes = max - min

    processes = [0 for i in range(indexes + 1)]

    for line in data:
        if line is not None and len(line) > 1:
            year_str = line[1][:4]
            if year_str.isdigit():
                year = int(year_str)
                index = year - min
                processes[index] += 1

    result = []

    for process in processes:
        result.append((processes.index(process) + min, process))

    sort = sorted(result, key=lambda x: x[1], reverse=True)

    repeated = []
    lastElem = (0,0)

    for elem in sort:
        if elem != lastElem:
            repeated.append(elem)
            lastElem = elem

    return repeated 


# 2.
def namesAndSurnames(name):
    data = saveFile(name)

    century_names = {}
    century_surnames = {}

    for i in range(0, 4):
        century_names[i] = {}
        century_surnames[i] = {}

    for line in data:
        if line is not None and len(line) > 1:
            year_str = line[1][:4]
            if year_str.isdigit():
                year = int(year_str)
                century = (year // 100) - 16

                name_pattern = re.compile(r'(\w+)\s+\w+\s+(\w+)')
                match = name_pattern.search(line[2])
                if match:
                    first = match.group(1)
                    surname = match.group(2)

                    if first not in century_names[century]:
                        century_names[century][first] = 0
                    century_names[century][first] += 1

                    if surname not in century_surnames[century]:
                        century_surnames[century][surname] = 0
                    century_surnames[century][surname] += 1

    result = []

    for i in range(0, 4):
        topNames = sorted(century_names[i], key=lambda x: century_names[i][x], reverse=True)[:5]
        topSurnames = sorted(century_surnames[i], key=lambda x: century_surnames[i][x], reverse=True)[:5]

        result.append((i + 17, topNames, topSurnames))

    return result


# 3.
def relations(name):
    data = saveFile(name)

    relation = {}
    possiblities = re.compile(r'\b(Pai|Mae|Irmao|Filho|Tio|Sobrinho|Neto|Avo|Primo)\b', re.IGNORECASE)

    for line in data:
        for item in line:
            match = possiblities.findall(item)
            for i in match:
                name = i.lower()
                if name in relation:
                    relation[name] += 1
                else:
                    relation[name] = 1

    result = [(name, count) for name, count in relation.items()]
    sort = sorted(result, key=lambda x: x[1], reverse=True)

    return sort


# 4.
def toJSON(name):
    with open(name, 'r') as f:
        lines = f.readlines()[:20]

    data = []
    for line in lines:
        match = re.search(r'^(\d+)::([\d-]+)::(.*)::(.*)::(.*)::(.*)::(.*)$', line)
        if match:
            id_, date, name1, name2, name3, name4, info = match.groups()
            data.append({
                'id': id_,
                'date': date,
                'name1': name1,
                'name2': name2,
                'name3': name3,
                'name4': name4,
                'info': info
            })

    with open('output.json', 'w') as f:
        json.dump(data, f, indent=2)


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

def ui(name):
    while True:
        print("\n\n----- Processos -----")
        print("| 1. Frequência de processos por ano")
        print("| 2. Frequência de nomes própios e apelidos")
        print("| 3. Frequência dos tipos de relação")
        print("| 4. Converter 20 primeiros registos ")        
        print("| 0. Exit\n---------------------\n\n")
        choice = input("Insere uma escolha  (0-3): ")
        
        if choice == '1':
            table(perYear(name))        
        elif choice == '2':
            table(namesAndSurnames(name))    
        elif choice == '3':
            table(relations(name))
        elif choice == '4':
            toJSON(name)

ui("processos.txt")