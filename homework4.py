immutable_var = "apple", "coconut", "banana", 1, 2, (3, 4)
print(immutable_var)
#immutable_var[0] = "peach"  # Кортежи - не изменяемые, т.е нельзя присвоить 0-элементу кортежа другое значение, потому что он это не поддерживает
mutable_list = [1, 2 ,3, "green", "red", "blue"]
mutable_list[0] = 3
print(mutable_list)
