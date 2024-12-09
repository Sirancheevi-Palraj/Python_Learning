import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample DataFrame
data = {"Month": ["Jan", "Feb", "Mar", "Apr"], "Sales": [200, 250, 300, 400]}
df = pd.DataFrame(data)

# Line plot
df.plot(x="Month", y="Sales", kind="line", title="Monthly Sales", legend=True)
plt.show()

# Bar plot
df.plot(x="Month", y="Sales", kind="bar", title="Monthly Sales", legend=True)
plt.show()

df["Profit"] = np.random.randint(50, 150, size=len(df))

# Histogram
df["Profit"].plot(kind="hist", title="Profit Distribution", bins=5)
plt.show()

# Customized visualization
df.plot(
    x="Month",
    y="Sales",
    kind="line",
    color="green",
    marker="o",
    figsize=(8, 4),
    title="Customized Monthly Sales",
    legend=True
)

plt.xlabel("Months")  # Add X-axis label
plt.ylabel("Sales in $")  # Add Y-axis label
plt.grid(True)  # Add grid
plt.show()
