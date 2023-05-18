import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the list of presidents
table = soup.find('table', {'class': 'wikitable'})

# Extract the names of the presidents from the table
presidents = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    if len(cells) > 1:
        president_name = cells[1].find('a').text
        presidents.append(president_name)

# Print the list of presidents
print(presidents)