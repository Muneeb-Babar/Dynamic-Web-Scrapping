
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
options = Options()
# options.add_argument("--headless")  # Run in headless mode (no GUI)

driver.get("https://coinmarketcap.com/")

# Wait for the page to load
driver.implicitly_wait(10)  

# table = driver.find_element("xpath", "//table")
# rows = table.find_elements("xpath", ".//tr")

table= driver.find_element(By.CLASS_NAME,"cmc-table")
rows = table.find_elements(By.TAG_NAME,"tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    
# Skip rows that don't have enough cells
    if len(cells) < 9:
        continue

    try:
        rank = cells[1].text.strip()
        name = cells[2].text.strip()
        price = cells[3].text.strip()
        hour_change = cells[4].text.strip()
        day_change = cells[5].text.strip()
        seven_day = cells[6].text.strip()
        market_cap = cells[7].text.strip()
        volume = cells[8].text.strip()

        print(f" Rank: {rank}, Name: {name}, Price: {price}, Hour Change: {hour_change}, Day Change: {day_change}, 7-Day Change: {seven_day}, Market Cap: {market_cap}, Volume: {volume}")
    except IndexError:
        # Optional: log the issue for debugging
        print("Skipping a malformed row.")
        continue