# Deanna Clayton mod3 File1
## 2. Using the code and data provided in Section 4.3, calculate the max and min
def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print(maximum(12, 27, 36))
print(max(12, 27, 36))
print(min(15, 9, 27, 14))
## Your own minimum function could be writen.
##It would look similar to the max function, but using < instead of >.
def minimum(val1, val2, val3):
    min_value = val1
    if val2 < min_value:
        min_value = val2
    if val3 < min_value:
        min_value = val3
    return min_value
