try:
    x=int(input("Enter a number: "))
    print(x/0)
except ZeroDivisionError:
    print("You cant divide by zero")
else:
    print("No exception occured")
finally:
    print("This will run regardless of the exception")

# Custom exception handling

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    else:
        print("Age is valid")

try:
    check_age(15)
except ValueError as e:
    print(f"Custom Exception: {e}")

else:
    print("No exception occurred")
finally:
    print("Age chcecking complete")


try:
    x=int(input("Enter a number: "))
    y=int(input("Enter a number: "))
    print(x/y)
except ZeroDivisionError:
    print("You cant divide by zero")
except ValueError:
    print("Enter a valid number bruhh")

else:
    print("numbers divided successfully")

finally:
    print("This will run regardless of the exception")