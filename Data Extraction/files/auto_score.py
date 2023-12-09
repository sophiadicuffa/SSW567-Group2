import subprocess
import csv

tests = []
results = []

for i in range(1, 306):
    tests.append("sample" + str(i))

for test in tests:
    try:
        print(f"Scoring File: {test}")
        result = subprocess.run(
            "pylint " + test + " --output-format=text",
            capture_output = True,
            text = True)
        results.append(result.stdout)
    except Exception as e:
            print(f"Error Scoring File {test}: {e}")

print("Writing Results to CSV")
with open("scores.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        for result in results:
            csv_writer.writerow([result])

print("Finished")