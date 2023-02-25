def sumOnOff():
    line = input()
    sum = 0
    word = ""
    isOn = True

    for char in line:
        if char.isdigit() and isOn:
            sum += int(char)
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
            print(sum) 
        else:
            word = ""        

sumOnOff()