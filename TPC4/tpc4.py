import json
import sys
import re
import os

def sumFunc(numbers):
    x = 0

    for i in numbers:
        x += int(i)

    return x

def medFunc(numbers):
    x = 0

    for i in numbers:
        x += int(i)

    return x/len(numbers)

def readCSV(fileName):
    notas = False
    somatorio = False
    media = False

    with open(fileName, mode='r') as file:
        lines = file.readlines()

        if re.search(r"(Notas)", lines[0]) != None:
            notas = True
            func = re.search(r"::([a-z]*)", lines[0])
            if func != None:   
                if func.group(1) == "sum":
                    somatorio = True
                elif func.group(1) == "media":
                    media = True

        header = lines[0].strip().split(',')
        header = [re.sub(r'{(\d+),?(\d+)?}?', '', h) for h in header if h.strip()]

        if somatorio:
            header[3] = "Notas_sum"
        elif media:
            header[3] = "Notas_media"

        data = []

        if not notas:
            for line in lines[1:]:
                values = line.strip().split(',')
                row = {}
                for i in range(len(header)):
                        row[header[i]] = values[i]
                data.append(row)

        else:
            if not somatorio and not media:
                for line in lines[1:]:
                    values = [val.strip() for val in line.split(',') if val.strip()]
                    row = {}
                    numbers = []
                    for i in range(len(values)):
                        if i >= 3:
                            numbers.append(values[i])
                        else:
                            row[header[i]] = values[i]
                    row[header[3]] = numbers
                    data.append(row)
            elif somatorio:
                for line in lines[1:]:
                    values = [val.strip() for val in line.split(',') if val.strip()]
                    row = {}
                    numbers = []
                    for i in range(len(values)):
                        if i > 3:
                            numbers.append(values[i])
                        else:
                            row[header[i]] = values[i]
                    row[header[3]] = sumFunc(numbers)
                    data.append(row)
            elif media:
                for line in lines[1:]:
                    values = [val.strip() for val in line.split(',') if val.strip()]
                    row = {}
                    numbers = []
                    for i in range(len(values)):
                        if i > 3:
                            numbers.append(values[i])
                        else:
                            row[header[i]] = values[i]
                    row[header[3]] = medFunc(numbers)
                    data.append(row)

        writeJSON(data, fileName)

def writeJSON(data, fileName):
    root, ext = os.path.splitext(fileName)
    file = root + ".json"
    with open(file, mode='w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

readCSV(sys.argv[1])