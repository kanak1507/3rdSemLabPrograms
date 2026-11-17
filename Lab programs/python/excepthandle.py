try:
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    c = a/b
    print("The value of c is: ",c)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid Input")
finally:
    print("Program Executed")