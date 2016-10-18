import requests
from bs4 import BeautifulSoup
import sqlite3
import numpy as np

response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = [tr.find_all('td') for tr in table.find_all('tr')]
cropped_rows = rows[1:-1]

extract = [row[4].text for row in cropped_rows]
neighborhoods = np.hstack([element.split(', ') for element in extract]).tolist()
values = zip([el for el in range(len(neighborhoods))], neighborhoods)

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("CREATE TABLE neighborhoods (id INTEGER PRIMARY KEY, neighborhood TEXT)")
c.executemany("INSERT INTO neighborhoods VALUES (?, ?)", values)
conn.commit()

c.execute("SELECT * FROM neighborhoods")
c.fetchall()
