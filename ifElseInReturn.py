def test(a, b):
    return ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

print(test(10,20))
