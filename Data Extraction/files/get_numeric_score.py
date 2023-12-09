# get just the number scores from scores.csv

import csv
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
csv_file_path = os.path.join(parent_directory, "filtered_big_file.csv")

scores = []

with open("scores.csv", "r", newline="", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        # Find the starting index of the score and extract the next three characters
        score_index = row[0].find("Your code has been rated at ") + len("Your code has been rated at ")
        score = row[0][score_index:score_index + 4]
        
        # Append the extracted score to the list
        if '.' in score:
            scores.append(score)
        else:
            scores.append("")

with open("just_scores.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    for score in scores:
            csv_writer.writerow([score])