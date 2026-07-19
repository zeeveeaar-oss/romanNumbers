def romToInt(romanInput):
    roman = {'M': 1000, 'D': 500, 'C': 100,'L': 50, 'X': 10, 'V': 5, 'I': 1}

    resultInteger = 0

    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[1]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[1]]
        else:
            resultInteger += roman[romanInput[1]]
    return resultInteger + roman[romanInput[-1]]

roman = input("Input roman number:")

print("Integer equivalent :", romToInt(roman))
