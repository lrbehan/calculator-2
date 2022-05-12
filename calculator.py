"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    
    users_input = input("Enter an equation > ")
    
    tokens = users_input.split()
    
    operator = tokens[0]
    
    if len(tokens) > 2:
        
        num1 = float(tokens[1])
        
        num2 = float(tokens[2])

        if operator == "+":
            result = add(num1, num2)
        
        elif operator == "-":
            result = subtract(num1, num2)
        
        elif operator == "*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(float(num1), float(num2))
        
        elif operator == "mod":
            result = mod(float(num1), float(num2))

        elif operator == "pow":
            result = power(num1), (num2)    
        
        else:
            print("Invalid option.")
            
        print(result)
    
    elif len(tokens) == 2:
        
        num1 = float(tokens[1])
        
        if operator == "square":
            result = square(num1)

        elif operator == "cube":
            result = cube(num1)
        
        else:
            print("Invalid option.")
        
        print(result)       
    
    elif len(tokens) == 1:
        
        if operator == "q":
            
            print ("quitting program")
            
            break
    
    



