def add (num1, num2):
    return num1 + num2
def subtract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2

print("Operation: ")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = input("Please select operation: ")

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if choice == '1':
    print(str(add(num1,num2)))
elif choice == '2':
    print(str(subtract(num1,num2)))
elif choice == '3':
    print(str(multiply(num1,num2)))
elif choice == '4':
    print(str(divide(num1,num2)))
else:
    print("Invalid")