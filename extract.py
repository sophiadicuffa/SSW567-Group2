import requests
import json
import csv

def get_data(url: str):
    response = requests.get(url)
    data = response.json()
    print(data) #just figured I'd leave the print for now
    extracted_data = {}
    for key in data:
        extracted_data[key] = data[key]

    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['data'])
        for key in extracted_data:
            csv_writer.writerow(extracted_data[key])

if __name__ == "__main__":
    get_data("https://github.com/NAIST-SE/DevGPT/tree/main/snapshot_20230727")