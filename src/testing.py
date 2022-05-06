with open('1food.txt') as f:
    lines = f.readlines()
    temp=0
    for line in lines:
        name, value, description, price = line.split("/")
        print(name, temp)
        temp+=1