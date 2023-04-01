def formart_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formart_f_name = f_name.title()
    formart_l_name = l_name.title()
    return f"Result: {formart_f_name} {formart_l_name}"

print(formart_name(input("What is your first name?"), input("What is your last name?")))