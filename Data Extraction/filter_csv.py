import csv
import json

file = open("combined_allTopics.csv")
csvreader = csv.reader(file)

acceptable_first_column = ["commit", "pull request", "hacker news", "code file"]

sourceTypes = []
urls = []
languages = []
number_of_prompts = []

print("Reading...")
for row in csvreader:
    if row[0] in acceptable_first_column and ".py" in row[1]:
        sourceTypes.append(row[0])
        urls.append(row[1])
        languages.append(row[4])

        prompts_index = row[9].find("'NumberOfPrompts': ")
        if prompts_index != -1:
            prompts_data = row[9][prompts_index:]
            num_prompts = int(prompts_data.split(",")[0].split(":")[1])
            number_of_prompts.append(num_prompts)
        else:
            number_of_prompts.append(0)

with open("filtered_big_file.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Type", "URL", "ChatGPTSharing" ,"RepoLanguage"])
        c_index = 0
        row_num = len(sourceTypes)
        print("Writing... (0 / ", row_num, ")")
        for id, (source, url, num_prompts, language) in enumerate(zip(sourceTypes, urls, number_of_prompts, languages), start=1):
            print("(", c_index, " / ", row_num, ")")
            csv_writer.writerow([source, url, num_prompts, language])
            c_index += 1

print("Finished")