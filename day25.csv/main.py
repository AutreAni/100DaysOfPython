import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240705.csv')

# squirrel_dict = {
#     "Color": ["Gray","Black", "Cinnamon"],
#     "Count": []
# }
# colors_list = squirrel_dict["Color"]
# # print(colors_list)
# for color in squirrel_dict["Color"]:
#     size = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
#     squirrel_dict["Count"].append(size)
#

squirrel_dict = {
    "Color":[],
    "Count":[]
}
grouped_by_color = squirrel_data.groupby(by = ["Primary Fur Color"])
for group in grouped_by_color:
    color = group[0]
    count = len(group[1])
    squirrel_dict["Color"].append(color)
    squirrel_dict["Count"].append(count)

pandas.DataFrame(squirrel_dict).to_csv("extracted_colors.csv")