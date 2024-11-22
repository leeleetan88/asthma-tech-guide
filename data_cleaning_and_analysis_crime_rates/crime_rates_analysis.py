import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset and display the first few rows and data types
file_path = '/content/crime_rates_2011_to_2023.csv'
data = pd.read_csv(file_path)

# Display the first few rows and data types of each column
print(data.head())
print(data.dtypes)

# Load the dataset with the correct header starting from row 9
data_cleaned = pd.read_csv(file_path, header=9)

# Display the first few rows and check for missing values
print(data_cleaned.head())
print(data_cleaned.isnull().sum())

# Rename columns using the values in row 0 as headers
new_headers = data_cleaned.iloc[0].values
data_cleaned.columns = new_headers
data_cleaned = data_cleaned.drop(index=0)

# Convert year columns to numeric and handle missing values
data_cleaned.iloc[:, 1:] = data_cleaned.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)

# Check the cleaned data with new headers and confirm data types
print(data_cleaned.head())
print(data_cleaned.dtypes)

# Ensure year columns are explicitly converted to numeric
for year in new_headers[1:]:
    data_cleaned[year] = pd.to_numeric(data_cleaned[year], errors='coerce')

# Prepare data for the heatmap
# Transpose the data to have years as rows and divisions as columns
data_cleaned = data_cleaned.set_index(new_headers[0])  # Set the first column as index (Division or equivalent)
total_divisions = data_cleaned.iloc[:, :].T  # Transpose the data for heatmap

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(total_divisions, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=.5)

plt.title('Crime Rates Across Divisions and Years')
plt.xlabel('Division')
plt.ylabel('Year')
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=0)
plt.show()
