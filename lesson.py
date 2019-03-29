a = float(input("Inter first number: "))
b = float(input("Inter second number: "))
v = input("Chose +,-,*,/ : ")

str(v)
if v == '+':
    c = a + b
    print("Your number is: ",c)
elif v == '-':
    c = a - b
    print("Your number is: ",c)
elif v == '*':
    c = a * b
    print("Your number is: ",c)
elif v == '/':
    c = a/b
    print("Your number is: ",c)
else:
    print("Error")



