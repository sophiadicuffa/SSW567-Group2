import subprocess
import csv
from sys import argv

def write(results: list) -> None:
    """Function for Writing Scoring Results to CSV"""
    with open("scores.csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            for result in results:
                csv_writer.writerow([result])
    
    return None

# TODO: This took literal hours to run on my machine. There's probably a better way to implement this
def install_python_packages(filename: str) -> list:
    """Function for installing python packages in a file"""
    output = []

    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if line.find("import") != -1 and line.find('#') == -1:
                print(line)
                words = set(line.split(" "))
                remove_list = ["from", '"import"', "as", "import", 'import', "os", "sys", '']
                # Remove Python keywords so the next for loop doesn't try to install them with pip
                print(words)
                for word in remove_list:
                    try:
                        if word.find("\n") != -1:
                            word.replace("\n", '')
                        if word.find(',') != -1:
                            word.replace(',', '')
                        words.remove(word)
                    except:
                        continue
                # Try to install every word left in the list as packages with pip
                for word in words:
                    try:
                        print(f"Attempting installation of: {word}")
                        subprocess.run(f"pip install {word}")
                        output.append(word)
                    except:
                        continue     
    
    return output

# Realized after writing this probably isn't necessary to run. Not 100% sure it works                
def remove_python_packages(packages: list) -> None:
    """Function for removing python packages installed by install_python_packages"""
    for package in packages:
        try:
            subprocess.run(f"pip uninstall {package}")
        except Exception as e:
            print(f"Error removing {package}: {e}")
    
    return None

def score_python(file_prefix: str, num_files: int, install_packages: bool = False) -> list:
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
            if install_packages: # Not recommended until install_python_packages is refactored to not take hours
                install_python_packages(test+".py")
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

def score_java(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_javascript(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_html(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_css(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_sql(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_csharp(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_cpp(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

def score_c(file_prefix: str, num_files: int) -> list:
    # TODO: Implement
    return None

# More language scoring functions can be added (or removed), these are just some I thought of

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