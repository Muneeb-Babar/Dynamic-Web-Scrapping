import requests
from bs4 import BeautifulSoup

url="https://coinmarketcap.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table in the HTML
table = soup.find('table')

# Find all rows in the table
rows = table.find_all('tr')

for row in rows[1:11]:
    cells = row.find_all('td')
    
    rank = cells[1].text.strip()
    name = cells[2].text.strip()
    price = cells[3].text.strip()
    hour_change = cells[4].text.strip()
    day_change = cells[5].text
    seven_day = cells[6].text
    market_cap = cells[7].text
    volume = cells[8].text
    

    print(f" Rank: {rank}, Name: {name}, Price: {price}, Hour Change: {hour_change}, Day Change: {day_change}, 7-Day Change: {seven_day}, Market Cap: {market_cap}, Volume: {volume}")


#This code will print the first 10 rows of the table, excluding the header row.
# Because this is a dynamic website, the table may not be present in the HTML response.


# Loop through each row and print the text of each cell
# for row in rows:
#     cells = row.find_all('td')
#     for cell in cells:
#         print(cell.text.strip(), end=' | ')
#     print()  # Print a newline after each row   



