import pandas as pd
import numpy as np

# Create a simple DataFrame to verify functionality
data = {
            'Name': ['Alice', 'Bob', 'Charlie'], 
            'Age': [25, 30, 35]
      }


df = pd.DataFrame(data)
# Display the DataFrame

# We can convert data into excel sheets
df.to_csv('test.csv')

# Remove first indexes
df.to_csv('test2.csv', index=False)

# Some data from whole data
df.head(2) # 2 row from start

df.tail(1) # one row from last

df.describe() # numerical value operations

"""   Age
count	3.0
mean	30.0
std	5.0
min	25.0
25%	27.5
50%	30.0
75%	32.5
max	35.0

"""


print(df)