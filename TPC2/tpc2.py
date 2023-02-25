def sumOnOff():
    line = input()
    sum = 0
    word = ""
    number = ""
    isOn = True

    for char in line:
        if char.isdigit() and isOn:
            number += char
        elif char.lower() == 'o':
            word += char
        elif char.lower() == "f":
            word += char
            if word.lower() == 'off':
                isOn = False                
        elif char.lower() == 'n':
            word += char
            if word.lower() == 'on':
                isOn = True
        elif char == '=':
            if number != "":
                sum += int(number)
            print(sum) 
        else:
            if number != "":
                sum += int(number)
            word = ""        
            number = ""

sumOnOff()