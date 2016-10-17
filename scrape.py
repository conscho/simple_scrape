import requests
from bs4 import BeautifulSoup
import sqlite3

response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

soup = BeautifulSoup(response.text, 'html.parser')
