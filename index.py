python
import pandas as pd
import requests
import json

# Define the URL for the dataset (JSON format)
dataset_url = "https://example.com/DL06-Freelance-Activities-ADRA-OD-010-AFR.json"

# Fetch the dataset
response = requests.get(dataset_url)
data = response.json()

# Convert JSON data to Pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())

# Example: Filter activities related to 'Consultancy Services'
consultancy_services = df[df['english_name'].str.contains("consultancy", case=False)]
print("\nConsultancy Services:")
print(consultancy_services)

# Example: Save filtered data to a new CSV file
output_file = "filtered_consultancy_services.csv"
consultancy_services.to_csv(output_file, index=False)
print(f"\nFiltered data saved to {output_file}")
