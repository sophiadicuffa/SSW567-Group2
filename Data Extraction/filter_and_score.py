# run this file to filter from combined_allTopics.csv, extract the files from github, and score them in one go
# scores output in scores.csv - if there was a problem scoring the file the line just gets written as ERR
# Fair warning: This could take a bit to run
import subprocess
import os

try:
    print("Running: python filter_csv.py")
    subprocess.run("python filter_csv.py")
except:
    print("Error: combined_allTopics.csv Does Not Exist - Attempting Extraction from Existing Dataset")

try:
    print("Changing Directory to files")
    os.chdir("files")
    print("Running: python extract.py")
    subprocess.run("python extract.py")
    # TODO: Don't hardcode the language, file prefix, and number of files
    print("Running: python auto_score.py python sample 305")
    subprocess.run("python auto_score.py python sample 305")
    print("Running: python get_numeric_score.py")
    subprocess.run("python get_numeric_score.py")
except Exception as e:
    print(f"Error: {e}")