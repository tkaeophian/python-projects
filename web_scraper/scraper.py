import pandas as pd
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

import os

# create downloads folder if not exists
root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "files")
if not os.path.exists(path):
    os.mkdir(path)


def Scrape():

    html = urlopen(
        "https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
    soup = BeautifulSoup(html, "html.parser")
    table = soup.findAll("table", {"class": "wikitable"})[0]
    rows = table.findAll("tr")

    with open(path + "/language.csv", "wt+", newline="") as f:
        writer = csv.writer(f)
        for i in rows:
            row = []
            for cell in i.findAll(["td", "th"]):
                row.append(cell.get_text())
            writer.writerow(row)

    a = pd.read_csv(path + "/language.csv")
    a.head()


Scrape()
