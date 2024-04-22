my_string = "My name is Shinas"
def replace_char(string, char, pos):
    new_str = ""
    for i in range(len(string)):
        if i == pos:
            new_str += char
        else:
            new_str += string[i]
    return new_str

replace_str = replace_char(my_string, 'F',11)
print(replace_str)

