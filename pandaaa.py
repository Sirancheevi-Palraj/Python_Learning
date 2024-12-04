import pandas as pd

# ---------------------Create a Series-------------------------
s = pd.Series([10, 'test', 30, 40], index=["a", "b", "c", "d"])
print(s)

# Accessing elements
print(s["b"])  # 20

#-------------------------------------------------------------
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)


#-------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.head().to_string())  # View the first 5 rows

#df.to_csv("output.csv", index=False)

#-------------data reading-------------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df.loc[1])
print(df.loc[0:1, ["Name", "City"]])
print(df.loc[1:2,["Name"]])
print(df.iloc[2,2])
print(df.iloc[1:2,1:2])
print(df[df["Age"] > 25]) #condition based rendering
print(df.loc[df["Age"] > 25, ["Name", "City"]])