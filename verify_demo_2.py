import random
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))    # chr返回整数对应的ascll字符
        print(temp)
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)