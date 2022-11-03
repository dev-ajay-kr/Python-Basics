# Datatype with key value pair
# similar to java maps

# with Integer Keys
Dict = {1: 'IT', 2: 'Source', 3: 'Code'}
print("Using Integer Keys to Make a Dictionary:")
print(Dict)

# with Mixed Keys
Dict = {'Hello': 'World', 2: [1, 2, 3, 4, 5]}
print("\nUsing Mixed Keys to Make a Dictionary:")
print(Dict)


###### when we try to value to a add key twice only second instance  persist
Dict = {1: 'IT', 2: 'Source', 3: 'Code'}

Dict[1] = "Information Technology"
print(Dict)

