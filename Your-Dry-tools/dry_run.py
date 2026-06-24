paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
to = {x[1] for x in paths}
fro = {x[0] for x in paths}
print(to)
print(fro)
print(list(to - fro))