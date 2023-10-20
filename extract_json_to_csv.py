import requests
import csv
import json

json_url = "https://raw.githubusercontent.com/NAIST-SE/DevGPT/main/snapshot_20230727/20230727_200003_commit_sharings.json"

def extract_json_to_csv(json_data):
    '''Function to extract ChatgptSharing URLs and Number of Prompts, and write to CSV'''
    data = json.loads(json_data)
    chatgpt_sharing_urls = []
    number_of_prompts = []
    
    for source in data.get("Sources", []):
        chatgpt_sharing = source.get("ChatgptSharing", [])
        for item in chatgpt_sharing:
            chatgpt_sharing_urls.append(item.get("URL"))
            number_of_prompts.append(item.get("NumberOfPrompts"))
    
    # Writing URLs and Number of Prompts to CSV with numbering
    with open("chatgpt_sharing_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["ID", "URL", "Number of Prompts"])  
        for idx, (url, prompts) in enumerate(zip(chatgpt_sharing_urls, number_of_prompts), start=1):
            csv_writer.writerow([idx, url, prompts])

response = requests.get(json_url)
if response.status_code == 200:
    json_data = response.text
    extract_json_to_csv(json_data)
    print("CSV file has been created successfully.")
else:
    print("Failed to fetch JSON data.")
