import requests
import json
import csv

url = "https://github.com/NAIST-SE/DevGPT/tree/main/snapshot_20230727"
response = requests.get(url)
data = response.json()

extracted_data = {}
extracted_data["payload"] = data["payload"]
extracted_data["title"] = data["title"]

with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['data'])  # Add column headers
    for key in extracted_data:
        csv_writer.writerow(extracted_data[key])
