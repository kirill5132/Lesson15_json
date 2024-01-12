def names():
    name = input("Привет, как тебя зовут")
    print('Привет', name)
bites = pickle.dumps(names)
print(bites)