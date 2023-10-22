import csv
import json

file_names = ["727_chatgpt_sharing_urls.csv", 
              "803_chatgpt_sharing_urls.csv",
              "810_chatgpt_sharing_urls.csv",
              "817_chatgpt_sharing_urls.csv",
              "824_chatgpt_sharing_urls.csv",
              "831_chatgpt_sharing_urls.csv",
              "907_chatgpt_sharing_urls.csv",
              "914_chatgpt_sharing_urls.csv"]

condensed = set()

for file in file_names:
    print("Starting File: " + file)
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3] == "True":
                condensed.add(row[1])

with open("condensed_chatgpt_sharing_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        for item in condensed:
            csv_writer.writerow([item])

print("Finished")