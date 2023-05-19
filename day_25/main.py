# with open("weather_data.csv") as data:
#     data = data.readlines()
# print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# total = 0
# for temp in temp_list:
#     total +=temp
# avg_temp = round(sum(temp_list)/len(temp_list), 2)
# print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)

# #Get data in Row
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# mon_temp_inC = monday.temp
# mon_temp_inF = ((mon_temp_inC/5)*9)+32
# print(mon_temp_inF)

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Anna", "Marie", "John"],
#     "scores": [89, 52, 67]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel[squirrel["Primary Fur Color"] == "Black"])

count_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

squirrel_count = pandas.DataFrame(count_data)
squirrel_count.to_csv("squirrel_count.csv")



