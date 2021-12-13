import pandas

# how many grey ones,cinamon,black from furcolor coramn

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_sq_count,red_sq_count,black_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("sq_count_csv")
