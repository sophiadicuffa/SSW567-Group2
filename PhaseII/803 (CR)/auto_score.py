import subprocess
import csv

tests = ["test1.py", "test2.py", "test3.py", "test4.py", "test5.py"]
results = []

for test in tests:
    result = subprocess.run(
        "pylint " + test + " --output-format=text",
        capture_output = True,
        text = True)
    results.append(result.stdout)

with open("scores.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        for result in results:
            csv_writer.writerow([result])
