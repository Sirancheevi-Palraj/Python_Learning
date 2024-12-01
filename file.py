import os

print(os.getpid())

with open("siran.txt",'a') as file:
    file.write(input("ennter data"))

with open("siran.txt",'r') as file:
    content = file.read()
    print(content)


