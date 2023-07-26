def add(num1,num2):
    result = num1 +num2
    print("The result is : ", result)


    def substract(num1,num2):
        result = num1-num2
    print("The result of sub is: ", result)


def multi(num1,num2):
        result = num1* num2
    print("The result of sub is: ", result)


def main():
    print("Enter the operation you want to perform: ")

    user_operation = input()
    user_input1 = int(input("Enter the first number: "))
    user_input2 = int(input("Enter the second number: "))

    if user_operation == "add":
        add(user_input1, user_input2)
    elif user_operation == "subtract":
        subtract(user_input1, user_input2)
    elif user_operation == "multiply":
        multiply(user_input1, user_input2)
    elif user_operation == "divide":
        divide(user_input1, user_input2)
    elif user_operation == "modulo":
        modulo(user_input1, user_input2)


main()
