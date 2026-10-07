print("Simple Calculator")
while True:
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
        print(number1, "+", number2, "=", answer)

    elif operation == "2":
        answer = number1 - number2
        print(number1, "-", number2, "=", answer)

    elif operation == "3":
        answer = number1 * number2
        print(number1, "*", number2, "=", answer)
    
    elif operation == "4":
        if number2 == 0:
            print("You cannot divide by zero.")
        else: 
            answer = number1 / number2
            print (number1, "/", number2, "=", answer)

    else:
        print("Invalid choice.") 
    again = input("Would you like to calculate again? (yes/no): ")
    
    if again.lower() != "yes":
        print("Thanks for using  the calculator!")
        break
    