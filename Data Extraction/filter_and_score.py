# run this file to filter from combined_allTopics.csv, extract the files from github, and score them in one go
# scores output in scores.csv - if there was a problem scoring the file the line just gets written as ""
# Fair warning: this will take few minutes to finish running
import subprocess

try:
    subprocess.run("python filter_csv.py")
    subprocess.run("cd files")
    subprocess.run("python extract.py")
    subprocess.run("python auto_score.py")
    subprocess.run("python get_numeric_score.py")
except Exception as e:
    print(f"Error: {e}")