def compute():
    try:
        x = 5 / 0
    except ZeroDivisionError:
        return f"Division by zero gives infinity!"

x = compute()
print(x)