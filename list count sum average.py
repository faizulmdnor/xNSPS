la= ['3', '5', '7', '23']
print(la)

ul = input("enter list of number seperated with comma: ")
list = ul.split(",")
tuple = tuple(list)



print("list: ", list)
print("Tuple: ", tuple)

tlist = map(int, list)
print("Converted to int: ", tlist)
sum = sum(tlist)
print("Sum of the list", sum)

length = len(list)
i = 0
while i < length :
    print(list[i])
    i += 1
print("Jumlah nombor yang dimasukkan: ", i)

aver = sum/i
print("purata number diatas: ", aver)