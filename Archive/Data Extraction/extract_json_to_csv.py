'''Code to extract .json data for easier access when testing for our research paper'''

import csv
import json
import requests

JSON_URL = "https://raw.githubusercontent.com/NAIST-SE/DevGPT/main/snapshot_20230914/20230914_083202_commit_sharings.json"


def extract_json_to_csv(data):
    '''Function to extract data and write to CSV'''
    data = json.loads(data)
    chatgpt_sharing_urls = []
    number_of_prompts = []
    has_python_code = []

    for source in data.get("Sources", []):
        chatgpt_sharing = source.get("ChatgptSharing", [])
        for item in chatgpt_sharing:
            chatgpt_sharing_urls.append(item.get("URL"))
            number_of_prompts.append(item.get("NumberOfPrompts"))
            conversations = item.get("Conversations", [])
            has_python = False
            for conversation in conversations:
                listofcode_items = conversation.get("ListOfCode", [])
                if listofcode_items:
                    for code_item in listofcode_items:
                        if code_item.get("Type") == "python":
                            code_item["isPython"] = "isPython"
                            has_python = True
            # add True/False based on presence of 'isPython' key
            has_python_code.append(has_python)

    # Change the first three numbers to your own .json folder numbers!!

    with open("914_chatgpt_sharing_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["ID", "URL", "Number of Prompts", "Python?"])
        for idx, (url, prompts, has_python) in enumerate(zip(chatgpt_sharing_urls, number_of_prompts, has_python_code), start=1):
            csv_writer.writerow([idx, url, prompts, has_python])


response = requests.get(JSON_URL, timeout=10)
if response.status_code == 200:
    json_data = response.text
    extract_json_to_csv(json_data)
    print("CSV file has been created successfully.")
else:
    print("Failed to fetch JSON data.")