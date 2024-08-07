
# Basic calculator

var1 = ""

try:
    num = int(input("100 / ? = "))
    print(f"100 / {num} = {100 / num}")


except ValueError as var2:
    print("Type in a number next time!")
    var1 = var2

except ZeroDivisionError as var2:
    print("You can't divide by zero.")
    var1 = var2

except Exception as var2:
    print("You screwed up!")
    var1 = var2

finally:
    # with the following file opened, writable, and referred to as "foo":
    with open("datlog.log", "w") as foo:
        print(var1, file=foo)

# ValueError <-- when we entered something not a number

# ZeroDivisionError <-- when we divide by zero


