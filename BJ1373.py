binary = input()[::-1]

octal = ''
for i in range(0, len(binary), 3):
    bList = binary[i:i+3]
    if len(bList) == 2:
        bList += '0'
    elif len(bList) == 1:
        bList += '00'
    octal += str(int(bList[0]) + int(bList[1]) * 2 + int(bList[2]) * 4)
    
print(octal[::-1]) 

