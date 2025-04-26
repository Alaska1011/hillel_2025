import string
import keyword
def name(variable_name):
    if variable_name[0].isdigit():
        return False
    if any(char.isupper() for char in variable_name) or \
       any(char in string.punctuation for char in variable_name if char != '_') or \
       ' ' in variable_name:
        return False
    if variable_name.count('_') > 1:
        return False
    if variable_name in keyword.kwlist:
        return False

    return True
variable_name = input("Enter name:")
result = name(variable_name)
print(f"{result}")
