import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://realpython.github.io/fake-jobs'
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

content = soup.find_all("div", {"class": "card-content"})
all_jobs = list()
for specific in content:
    job = dict()
    job["JobPost  "] = specific.find("h2", class_="title is-5").text.strip()
    job["Company Name  "] = specific.find("h3", class_="subtitle is-6 company").text.strip()
    job["Location  "] = specific.find("p", class_="location").text.strip()
    job["Due date  "] = specific.find("p", class_="is-small has-text-grey").text.strip()
    all_jobs.append(job)

data_frame = pd.DataFrame(all_jobs)
data_frame.to_csv("JobsData.csv", mode="w", index=False)
print("Job Data successfully added to the \"JobsData.csv\" file")