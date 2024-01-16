import csv
import json

# This script is based on extract_json_to_csv.py in the archive

def find_code_files(file_suffix: str, csv_filename: str, output_filename: str) -> None:
    file = open(csv_filename)
    csvreader = csv.reader(file)

    acceptable_first_column = ["commit", "pull request", "hacker news", "code file"]

    sourceTypes = []
    urls = []
    languages = []
    number_of_prompts = []

    print("Reading...")
    for row in csvreader:
        # Lines in combined_allTopics.csv aren't all in the same format, so we have to check if a given line is in the right format
        if row[0] in acceptable_first_column and file_suffix in row[1]:
            sourceTypes.append(row[0])
            urls.append(row[1])
            languages.append(row[4])

            # TODO: Extract the actual json object instead of just looking for this string
            prompts_index = row[9].find("'NumberOfPrompts': ")
            if prompts_index != -1:
                prompts_data = row[9][prompts_index:]
                num_prompts = int(prompts_data.split(",")[0].split(":")[1])
                number_of_prompts.append(num_prompts)
            else:
                number_of_prompts.append("ERR")

    with open(output_filename, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Type", "URL", "Prompts" ,"RepoLanguage"])
            c_index = 0
            row_num = len(sourceTypes)
            print("Writing... (0 / ", row_num, ")")
            for id, (source, url, num_prompts, language) in enumerate(zip(sourceTypes, urls, number_of_prompts, languages), start=1):
                print("(", c_index, " / ", row_num, ")")
                csv_writer.writerow([id, source, url, num_prompts, language])
                c_index += 1

if __name__ == "__main__":
    find_code_files(".py", "combined_allTopics.csv", "")
    print("Finished")