import pandas as pd

# Read the CSV file into a dataframe
df_cocoa = pd.read_csv('flavors_of_cocoa.csv')

# Check data types and identify which feature requires data conversion
data_types = df_cocoa.dtypes
print("Data types:\n", data_types)
