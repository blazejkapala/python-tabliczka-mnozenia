from random import randrange

a=randrange(5,11)
b=randrange(1,11)
c=a*b
name=0
print(a, " * ", b, " = ");
name = input("Podaj wynik: ")

while True:


  if c!=int(name):
    name = input("Spróbuj ponownie: ")
  else:
    a=randrange(1,11)
    b=randrange(1,11)
    c=a*b
    print(a, " * ", b, " = ");
    name = input("Podaj wynik: ")