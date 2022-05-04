import sys
import os
from requests import request as httpClient

file_csv = "database_pdfs.csv"
base_dir_path = "downloads"
dataSet = []

try:
    file_csv = sys.argv[1]
except:
    ...

file = open(file_csv, encoding="utf-8")

try:
    os.mkdir(base_dir_path)    
except:
    ...


def download_pdf(url, file_name):
    file_path = f"{base_dir_path}/{file_name}.pdf"
    try:
        response = httpClient("GET", url, allow_redirects=True)
        if response.status_code == 200:
            print(f"{file_name} - ok")
            open(file_path, "wb").write(response.content)
        else:
            print(f"{file_name} - error")
    except:
        print(f"{file_name} - error")


for i in file:
    if ";" in i:
        row = i.split(";")
    else:
        row = i.split(",")
    dataSet.append({
        "link": row[0],
        "file_name": f"{row[1]}".replace("\n", "")
    })

for ccb in dataSet[1:3]:
    download_pdf(ccb["link"], ccb["file_name"])
