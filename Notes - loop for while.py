# Example 1:
for i in range(5):
    print(i)

# Example 2:
for i in 'mujtahidun':
    print(i, end='\t')


print('\n')

for i in 'mujtahidun':
    print("\n",i)


a = 1
while a <= 5:
    print("a = ",a)
    a = a + 1

q = 1
while q <= 5:
    print("q = ",q)
    q += 1

b = 100
while b >= 94:
    print("b = ", b)
    b = b-1

r = 100
while r >= 94:
    print("r = ",r)
    r -= 1

x = lambda a : a + 10
print(x(5))

# Example: Apply lambda to each element in a list
numbers = [1, 2, 3, 4, 5]
doubled = [(lambda x: x * 3)(x) for x in numbers]
print(doubled)
print(max(doubled))
print(min(doubled))
print(sum(doubled))
print(list(filter(lambda x: x%2 == 0, doubled)))
