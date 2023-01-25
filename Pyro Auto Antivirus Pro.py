import requests
import os
import time
apitext = """
Do you have Virustotal API KEY?

[1] I have 
[2] No I havent (you may get an errors)
[3] Create an API key 

"""
uc = "3"
iki = "2"
bir = "1"
apivarmi = input(apitext)
if apivarmi == iki:


    api_key = "6dd8022c274eb6a4ebf4e64d6afcdb61f0de63c77d94bda58ce4251f35db28ba"
    os.system('cls')

if apivarmi == uc:
    os.system('cls')
    print("Create account and enter the API you received!")
    time.sleep(2)
    os.system('https://www.virustotal.com/gui/my-apikey')
    api_key = input("API KEY: ")

if apivarmi == bir:
    os.system('cls')
    api_key = input("API KEY: ")


file_path = input("Enter the exact file location (for example: C:\Windows\VIRUSFILE.exe): ")

url = "https://www.virustotal.com/vtapi/v2/file/scan"
params = {"apikey": api_key}
files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files, params=params)


data = response.json()
print("File status::", data["verbose_msg"])


if data["response_code"] == 1:
    resource = data["resource"]
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    params = {"apikey": api_key, "resource": resource}
    response = requests.get(url, params=params)
    data = response.json()
    print("Virus status:", data["positives"], "/", data["total"])
    print("File status:", data["verbose_msg"])
time.sleep(10)
