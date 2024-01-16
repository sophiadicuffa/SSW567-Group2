import csv
import os
import wget
import json
import requests

def get_filename_from_github_link(url: str) -> str:
    """Function for extracting filename from links starting with raw.githubusercontent"""
    output = url[url.rfind('/')::]
    return output

def download_file_from_github(url: str, output_path: str = "") -> None:
    """Function for downloading file from links starting with raw.githubusercontent"""
    try:
        if output_path == "":
            output_path = get_filename_from_github_link(url)
        wget.download(url, out=output_path)
        print(f"File '{output_path}' downloaded successfully.")
    except Exception as e:
        print(f"Failed to download file. Error: {e}")

def download_from_csv(csv_filename: str, directory_name: str) -> None:
    """Function for downloading a list of GitHub links in a one column csv file with header"""
    links = []
    with open(csv_filename, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) # skip header

        for row in csv_reader:
            links.append(row[0])
    
    try:
        os.chdir(directory_name)
    except:
        os.makedirs(directory_name)
        os.chdir(directory_name)
    
    for link in links:
        download_file_from_github(link)

# Legacy Code
if __name__ == "__main__":
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    csv_file_path = os.path.join(parent_directory, "filtered_big_file.csv")
    
    with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) # skip header row

        num = 0
        for row in csv_reader:
            num += 1
            url = row[1] # filtered_big_file.csv format: [Type, URL, Prompts, RepoLanguage]
            # Have to change the url slightly to be able to download directly
            url = url.replace("github", "raw.githubusercontent")
            url = url.replace("/blob", '')
            print(url)
            output_filename = f"sample{num}.py"
            try:
                download_file_from_github(url, output_filename)
                print(f"File '{output_filename}' downloaded successfully.")
            except Exception as e:
                print(f"Failed to download file. Error: {e}")