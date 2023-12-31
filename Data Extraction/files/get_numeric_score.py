# get just the number scores from scores.csv

import csv
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
csv_file_path = os.path.join(parent_directory, "filtered_big_file.csv")

scores = []

# TODO: Make this work for static code analyzer outputs other than Pylint
if __name__ == "__main__":
    with open("scores.csv", "r", newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # TODO: Figure out a better way of determining if a given line has a score
        for row in csv_reader:
            # Find the starting index of the score and extract the next three characters
            score_index = row[0].find("Your code has been rated at ") + len("Your code has been rated at ")
            score = row[0][score_index:score_index + 4]

            # Scores should be in the format X.XX
            if '.' in score:
                scores.append(score)
            else:
                scores.append("ERR")

    with open("just_scores.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        for score in scores:
                csv_writer.writerow([score])