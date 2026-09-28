def grade(marks):
    if marks >= 90:
        return 'A - Excellent'
    elif marks >= 75:
        return 'B - Good'
    elif marks >= 50:
        return 'C - Not Fair'
    else:
        return 'F - Fail'

print(grade(95))
print(grade(85))
print(grade(77))
print(grade(55))
