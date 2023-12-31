import subprocess
import csv
from sys import argv

def write(results: list):
    """Function for Writing Scoring Results to CSV"""
    with open("scores.csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            for result in results:
                csv_writer.writerow([result])
    
    return None

def score_python(file_prefix: str, num_files: int):
    """Scores Python Code Samples Using Pylint"""
    tests = []
    results = []

    # Use the file prefix and number of samples input to generate the full names of files to be scored
    if num_files > 1:
        for i in range(1, num_files+1):
            tests.append(file_prefix + str(i))
    else:
        tests.append(file_prefix)

    # For every file, try to run Pylint. If it can't, skip and move onto the next one
    for test in tests:
        try:
            print(f"Scoring File: {test}")
            # subprocess.run lets us run terminal commands in python
            result = subprocess.run(
                "pylint " + test + " --output-format=text",
                capture_output = True,
                text = True)
            results.append(result.stdout)
        except Exception as e:
            print(f"Error Scoring File {test}: {e}")
            continue
        
    return results

def score_java(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_javascript(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_html(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_css(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_sql(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_csharp(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_cpp(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

def score_c(file_prefix: str, num_files: int):
    # TODO: Implement
    return None

# More can be added, these are just some I thought of

if __name__ == "__main__":
    if len(argv) != 4:
        raise Exception("Usage: python auto_score.py [language] [file name prefix] [number of files]")
    
    language = str(argv[1])
    prefix = str(argv[2])
    num_files = int(argv[3])

    if language == "python":
        write(score_python(prefix, num_files))
    elif language == "java":
        write(score_java(prefix, num_files))
    elif language == "javascript":
        write(score_javascript(prefix, num_files))
    elif language == "html":
        write(score_html(prefix, num_files))
    elif language == "css":
        write(score_css(prefix, num_files))
    elif language == "csharp":
        write(score_csharp(prefix, num_files))
    elif language == "cpp" or language == "c++":
        write(score_cpp(prefix, num_files))
    elif language == "c":
        write(score_c(prefix, num_files))
    else:
        raise Exception("Error: Invalid Language")