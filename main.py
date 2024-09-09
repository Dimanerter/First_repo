lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
print(lst)

d_lst = set(lst)
lst = list(d_lst)

print(lst)

numbers = {1, 2, 3}
numbers.add(4)
print(numbers) 

numbers.remove(3)
print(numbers)

numbers.discard(3)
print(numbers)
