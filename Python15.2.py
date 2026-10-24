try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result is: ", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("This will execuate no matter what")