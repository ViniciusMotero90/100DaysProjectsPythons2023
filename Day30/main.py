import math
#try:
#    file = open("a_file.txt")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["key"])
#except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("Something")
#except KeyError as error_message:
#    print(f"The key {error_message} does not exit.")
#else:
#    content = file.read()
#    print(content)
#finally:
#    raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / math.pow(height, 2)

print(bmi)
