print("Simple Calculator")

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter 1, 2, 3 or 4: ")

if operation == "1":
    answer = number1 + number2
    print("Answer:", answer)

elif operation == "2":
    answer = number1 - number2
    print("Answer:", answer)

elif operation == "3":
    answer = number1 * number2
    print("Answer:", answer)

elif operation == "4":
    answer = number1 / number2
    print("Answer:", answer)

else:
    print("Invalid choice.")