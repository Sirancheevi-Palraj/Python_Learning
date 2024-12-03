import pandas as pd

# Create a Series
s = pd.Series([10, 'test', 30, 40], index=["a", "b", "c", "d"])
print(s)

# Accessing elements
print(s["b"])  # 20

#-----------------------------------------------------------
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

# Accessing a column
print(df["Name"])  # Series with names


#-------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.head().to_string())  # View the first 5 rows

#df.to_csv("output.csv", index=False)