# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

sum_temp = 0
for temp in temp_list:
    sum_temp += temp

average_temp = sum_temp/len(temp_list)
print("Average Temperature:", average_temp)

#Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.temp)
print(monday.temp*9/5 + 32)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("scores_data.csv")