import requests
import csv

url = "https://github.com/NAIST-SE/DevGPT/tree/main/snapshot_20230727"
response = requests.get(url)
data = response.json()

extracted_data = data["key"]["nested_key"]  # Adjust this based on your JSON structure

with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Column1', 'Column2', ...])  # Add column headers
    for item in extracted_data:
        csv_writer.writerow([item['key1'], item['key2'], ...])  # Add data based on JSON structure
