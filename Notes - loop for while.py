
# Example 1:
for i in range(5):
    print(i)

# Example 2:
for i in 'kehidupan':
    print(i, end=' ')
print('\n')
for i in 'kehidupan':
    print(i)

a = 1
while a <= 10:
    print(a)
    a = a+1

b = 100
while b >= 80:
    print(b)
    b = b-1

x = lambda a : a + 10
print(x(5))

# Example: Apply lambda to each element in a list
numbers = [1, 2, 3, 4, 5]
doubled = [(lambda x: x * 3)(x) for x in numbers]
print(doubled)  # Output: [2, 4, 6, 8, 10]
print(max(doubled))
print(min(doubled))
print(sum(doubled))
print(list(filter(lambda x: x%2 == 0, doubled)))
