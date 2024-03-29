immutable_var = "1", 1, 1., [0,1,2]
for i in range(len(immutable_var)) : print(immutable_var[i], " : ", type(immutable_var[i]))
print()
immutable_var = immutable_var*2
immutable_var[3][2] = 0
for i in range(len(immutable_var)) : print(immutable_var[i], " : ", type(immutable_var[i]))
immutable_var[7][2] = 10
print()
for i in range(len(immutable_var)) : print(immutable_var[i], " : ", type(immutable_var[i]))
