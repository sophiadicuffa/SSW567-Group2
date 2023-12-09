import csv
import os
import wget

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
csv_file_path = os.path.join(parent_directory, "filtered_big_file.csv")

def download_file_from_github(url, output_path):
    try:
        wget.download(url, out=output_path)
        print(f"File '{output_path}' downloaded successfully.")
    except Exception as e:
        print(f"Failed to download file. Error: {e}")

with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # skip header row

    num = 0
    for row in csv_reader:
        num += 1
        url = row[1]
        url = url.replace("github", "raw.githubusercontent")
        url = url.replace("/blob", "")
        print(url)
        output_filename = f"sample{num}.py"
        try:
            download_file_from_github(url, output_filename)
            print(f"File '{output_filename}' downloaded successfully.")
        except Exception as e:
            print(f"Failed to download file. Error: {e}")