print("This is my calculator")
print()
print("The operations:")
print("Addition")
print("subtraction")
print("Multiplication")
print("Division")
print("Floor Division")
print("Exponential")
print("Remainder")
# I created my variables and made them a flaot or int.
p=float(input("first"))
o=float(input("second"))
t=int(input("third"))

# 
if t == 1:
    d = p + o
    print(d)
elif t ==2:
    d = p - o
    print(d)
elif t == 3:
    d=p * o
    print(d)
elif t == 4:
    d = p / o
    print(d)
elif t == 5:
    d = p // o
    print(d)
elif t == 6:
    d = p ** o
    print(d)
elif t == 7:
    d= p % o
    print(d)
else:
     print("Invalid Input")