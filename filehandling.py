import pandas as pd

df= pd.read_csv(r"C:\Users\yogen\Downloads\iris.csv")

df["PetalArea"] = df["PetalLengthCm"]* df["PetalWidthCm"]
df["SepalArea"] = df["SepalLengthCm"]* df["SepalWidthCm"]

df.drop(columns=["Id"],inplace=True,errors = "ignore")
df.to_csv(  r"C:\Users\yogen\Downloads\iris.csv",index=False) #with index = False, it will not write the index column to the csv file
# df.to_csv(r"C:\Users\yogen\Downloads\iris.csv",index=True) #with index = True, it will write the index column to the csv file(0th coloumn/?)
print(df.describe())

#Ordering the data in ascending and descending order

df.sort_values(["SepalLengthCm","PetalLen"],ascending=True,inplace=True) #inplace = True, it will change the original dataframe, inplace = False, it will not change the original dataframe)
print(df.head())

