# Casting tipe data
# Mengubah  tipe data dari data satu ke data yang lain

print("=========INTEGER=========")
data_int = 10
print("Data ini : ", data_int, "Type-nya : ", type(data_int))

data_float = float(data_int)
print("Data ini : ", float(data_float), "Type-nya : ", type(data_float))

data_string = str(data_int)
print("Data ini : ", str(data_string), "Type-nya : ", type(data_string))

data_boolean = bool(data_int) # akan false jika nilai integer 0
print("Data ini : ", bool(data_boolean), "Type-nya : ", type(data_boolean))

print("=========FLOAT=========")
data_float = 2.5
print("Data ini : ", data_float, "Type-nya : ", type(data_float))

data_integer = int(data_float)
print("Data ini : ", data_integer, "Type-nya : ", type(data_integer))

data_string = str(data_float)
print("Data ini : ", data_string, "Type-nya : ", type(data_string))

data_boolean = bool(data_float)
print("Data ini : ", data_boolean, "Type-nya : ", type(data_boolean))

print("=========STRING=========")
data_string = "25"
print("Data ini : ", data_string, "Type-nya : ", type(data_string))

data_integer = int(data_string)
print("Data ini : ", data_integer, "Type-nya : ", type(data_integer))

data_float = float(data_string)
print("Data ini : ", data_float, "Type-nya : ", type(data_float))

data_boolean = bool(data_string)
print("Data ini : ", data_boolean, "Type-nya : ", type(data_boolean))

print("=========BOOLEAN=========")
data_boolean = True
print("Data ini : ", data_boolean, "Type-nya : ", type(data_boolean))

data_integer = int(data_boolean)
print("Data ini : ", data_integer, "Type-nya : ", type(data_integer))

data_string = str(data_boolean)
print("Data ini : ", data_string, "Type-nya : ", type(data_string))

data_float = float(data_boolean)
print("Data ini : ", data_float, "Type-nya : ", type(data_float))