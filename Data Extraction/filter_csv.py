import csv

file = open("combined_allTopics.csv")
csvreader = csv.reader(file)

acceptable_first_column = ["commit", "pull request", "hacker news", "code file"]

ids = []
sourceTypes = []
urls = []
languages = []

print("Reading...")
for row in csvreader:
    if row[0] in acceptable_first_column and row[4] == "Python":
        ids.append(row[30])
        sourceTypes.append(row[0])
        urls.append(row[1])
        languages.append(row[4])

with open("filtered_big_file.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["ID", "Type", "URL", "RepoLanguage"])
        c_index = 0
        row_num = len(sourceTypes)
        print("Writing... (0 / ", row_num, ")")
        for id, (source, url, language) in enumerate(zip(sourceTypes, urls, languages), start=1):
            print("(", c_index, " / ", row_num, ")")
            csv_writer.writerow([id, source, url, language])
            c_index += 1

print("Finished")