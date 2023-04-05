#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)
#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas
#data = pandas.read_csv("weather_data.csv")
#temp_list = data["temp"].to_list()
#print(temp_list)

#print(data["temp"].max())
#print(data["condition"])
#print(data.condition)

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday_temp = monday["temp"]
#monday_temp_F = (monday_temp * 9/5) + 32
#print(monday_temp_F)


#data_dict = {
#    "students": ["Amy", "James", "Angelas"],
#    "scores": [76, 56, 65]
#}

#datas = pandas.DataFrame(data_dict)
#datas.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
