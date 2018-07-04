import random
import math

command = 0
number_1 = 0
number_2 = 0
output_number = 0
random_choice = 0
exponent = 0
variable1 = 0
variable2 = 0
algebra_type = 0
algebra_exp_equ = 0
say = 0

print("Welcome to the Python CMD Calculator! Type help for a list of commands. ")
while True:
    command = input(">>> ")
    if command == "help":
        print("This is the Command Line Calculator, or as I like to call it, the CMDCalc. This is a list of commands: ")
        print("=======================================================================================================")
        print("'add' - This command allows you to add two numbers together.")
        print("'subtract' - This command allows you to subtract one number from another.")
        print("'multiply' - This command allows you to multiply two numbers.")
        print("'divide' - This command allows you to divide two numbers. You can also add 'integral' to the end to divide integrally.")
        print("'square' - This command allows you to square a number.")
        print("'cube' - This command allows you to cube a number.")
        print("'exponent' - This command allows you to raise a number to the power of your choice.")
        print("'modulus' - This command allows you to find the modulus of two numbers.")
        print("'double' - This command allows you to double a number.")
        print("'square_root' - This command allows you to find the square root of a number.")
        print(" ")
        print("Fun commands: ")
        print("'say' - This command allows the Python CMDCalc to print something of your choice.")
        print(" ")
        print("More commands are coming soon!")
        print("Check out my blog! littlebuglet.wordpress.com")
        
    if command == "add":
        number_1 = input("First number: ")
        number_2 = input("Second number: ")
        output_number = int(number_1) + int(number_2)
        print(output_number)
        
    if command == "subtract":
        number_1 = input("First number: ")
        number_2 = input("Second number: ")
        output_number = int(number_1) - int(number_2)
        print(output_number)
        
    if command == "multiply":
        number_1 = input("First number: ")
        number_2 = input("Second number: ")
        output_number = int(number_1) * int(number_2)
        print(output_number)
        
    if command == "divide":
        number_1 = input("First number: ")
        number_2 = input("Second number: ")
        output_number = int(number_1) / int(number_2)
        print(output_number)
        
    if command == "square":
        number_1 = input("Number: ")
        output_number = int(number_1) * int(number_1)
        print(output_number)

    if command == "cube":
        number_1 = input("Number: ")
        output_number = int(number_1) * int(number_1) * int(number_1)
        print(output_number)

    if command == "exponent":
        number_1 = input("Number: ")
        exponent = input("Raised to the power of: ")
        output_number = int(number_1) ** int(exponent)
        print(output_number)
        
    if command == "divide integral":
        number_1 = input("First number: ")
        number_2 = input("Second number: ")
        output_number = int(number_1) // int(number_2)
        print(output_number)

    if command == "modulus":
        number_1 = input("First number: ")
        number_2 = input("Second number: ")
        output_number = int(number_1) % int(number_2)
        print(output_number)

    if command == "square_root":
        number_1 = input("Number: ")
        output_number = math.sqrt(int(number_1))
        print(output_number)
        
# Algebraic expressions are fun!
    if command == "algebra":
        print("Usage: algebra start")
    if command == "algebra start":
        print("This command isn't finished yet, but you can still use it (sort of).")
        algebra_type = input("What do you want it to be? (expression, equation) ")
        if algebra_type == "expression":
                variable1 = input("What's the first variable? (One letter) ")
                variable2 = input("What's the second variable? (one letter, must be different from the first variable) ")
                number_1 = input("What will variable 1's number be? ")
                number_2 = input("What will variable 2's number be? ")
                algebra_exp_equ = input("What will the expression be? ")
                replace( variable1 , number_1 )
                replace( variable2 , number_2 )
                print(algebra_exp_equ)

    if command == "say":
        say = input("say >>> ")
        print(say)

    if command == "double":
        number_1 = input("Number: ")
        output_number = int(number_1) * 2
        print(output_number)
                                

