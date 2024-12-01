#basic program
from datetime import date
birthyear = int(input('enter the year'));
current_date = date.today()
current_year = current_date.year;
age = current_year - birthyear
print("your age is " + str(age))

#-----------------------------------------
#Objects
PhoneData = {
'siran' : '9600591085',
'siran1' : '8838978273',

}

print(PhoneData)

#------------------------------------------
#if
a = int(input('enter numbr a'))
b = int(input('enter numbr b'))
c = int(input('enter numbr c'))

if(a>b and a>c):
    print("a is bigger")
elif b > c:
    print("b is bigger")
else :
    print("c is bigger")

#--------------------------------------------
#loop
print('Fibnocci')
n = int(input('enter the range'))
a=0
b=1

# Loop to generate the sequence
for i in range(n):  # Start from index 2 since the first two are already printed
    c = a + b
    print(c)
    a, b = b, c


#functions
def add(a,b):
    c = a+b
    print("addition:",c)

def sub(a,b):
    c = a-b
    print(c)

def mul(a,b):
    c = a*b
    print(c)

def div(a,b):
    c = a/b
    print(c)


a = int(input("enter a value"))
b = int(input("enter b value"))
n = int(input("enter the option"))

if(n == 1):
    add(a,b)
elif(n ==2):
    sub(a,b)
elif(n == 3):
    mul(a,b)
else:
    div(a,b)


x = 10
def test():
   try:
        print(x)
   except Exception as e:
        print(e);

   

test()
print(x)