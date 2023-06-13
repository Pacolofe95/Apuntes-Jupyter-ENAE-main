import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://blitz.gg/lol/champions/overview?queue=RANKED_SOLO_5X5&region=EUW1&tier=DIAMOND'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all elements with class "⚡db7c12ce"
elements = soup.find_all(class_='⚡f5978295 card-body')

# Create an empty list to store the data
data = []

# Extract the text content of each element and append to the data list
for element in elements:
    data.append(element.text.strip())

# Create a pandas dataframe from the data list
df = pd.DataFrame(data, columns=['Content'])

# Print the dataframe

print('Hola')