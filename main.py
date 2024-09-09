my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

my_dict["age"] = 26
my_dict["email"] = "alice@example.com"

print(my_dict)

del my_dict["age"]
print(my_dict)

print("name" in my_dict)
print("age" in my_dict)
