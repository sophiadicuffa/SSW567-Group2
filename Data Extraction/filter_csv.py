import csv

file = open("combined_allTopics.csv")
csvreader = csv.reader(file)

acceptable_first_column = ["commit", "pull request", "hacker news", "code file"]

python_rows = []

print("Reading...")
for row in csvreader:
    if row[0] in acceptable_first_column and row[4] == "Python":
        python_rows.append(row[30] + "," + row[0] + "," + row[1] + "," + row[4])

python_rows = set(python_rows)

with open("filtered_big_file.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["ID", "Type", "URL", "RepoLanguage"])
        c_index = 0
        row_num = len(python_rows)
        print("Writing... (0 / ", row_num, ")")
        for row in python_rows:
            print("(", c_index, " / ", row_num, ")")
            csv_writer.writerow(python_rows)
            c_index += 1

print("Finished")