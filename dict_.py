dic = {}
num1 = {}
for i in range(10):
    num = int(input('>: '))
    if num in dic:
        dic[num] += 1
        print(dic)
    else:
        dic[num] = 1
        print(dic)
        print(len(dic))
