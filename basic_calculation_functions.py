def basic_calculations(a,b,operation):

    if(a.isnumeric() & b.isnumeric()):
        a=float(a)
        b=float(b)
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "divide":
            result = a / b
        elif operation == "multiply":
            result = a * b
        else:
            result = "Operations suppoerted is add, subtract, divide, and multiple only"

    else:
        result = "Please enter a valid number a and b"

    return result