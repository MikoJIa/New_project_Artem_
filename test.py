string = "Hello!"

for i in range(1, len(string)):
    if i % 2 == 0:
        print(string[0:i])
    else:
        print(string[0:i], end=",")


