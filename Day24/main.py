#with open("/Users/W11/Desktop/ProjectsPython/Day24/my_file.txt") as file:
#    contents = file.read()
#    print(contents)

with open("/Users/W11/Desktop/ProjectsPython/Day24/file.txt", mode="a") as file:
    file.write("New text.")