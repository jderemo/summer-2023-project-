import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = "https://www.timeanddate.com/sun/usa/columbia"
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the sunset time element and extract the text
table = soup.find('table', {'class': 'sep c'})
#sunset_time = soup.find('div', {'class': 'four columns'}).find_all('span')[3].text

presidents = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    if len(cells) > 1:
        president_name = cells[1].find('a').text
        presidents.append(president_name)

# Print the list of presidents
print(presidents)