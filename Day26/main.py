import pandas
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Angela"
letters_list = [letter for letter in name]

range_list = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

sort_name = [name.upper() for name in names if len(name) > 5]

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print(sort_name)
