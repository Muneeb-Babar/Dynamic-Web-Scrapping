import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment to run in headless mode (no GUI)


CHROMEDRIVER_PATH = r"c:\Users\AAC\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

def extract_coin_data():
    """Extract coin data from the current page"""
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    coin_data = []

    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 9:
                name_cell = cols[2]
                name = name_cell.text.split('\n')[0]

                try:
                    symbol = name_cell.find_element(By.TAG_NAME, 'p').text
                except:
                    symbol = "N/A"

                price = cols[3].text if cols[3].text != '####' else "N/A"
                percent_24h = cols[4].text
                percent_7d = cols[5].text
                market_cap = cols[6].text
                volume_24h = cols[7].text if cols[7].text != '####' else "N/A"

                coin_data.append({
                    'Name': name,
                    'Symbol': symbol,
                    'Price': price,
                    '24h %': percent_24h,
                    '7d %': percent_7d,
                    'Market Cap': market_cap,
                    'Volume (24h)': volume_24h
                })
        except Exception as e:
            print(f"Error processing row: {e}")
            continue
    
    return coin_data


all_data = []

# Loop through the first 10 pages
for page in range(1, 11):  # Pages 1 to 10
    url = f"https://coinmarketcap.com/?page={page}"
    print(f"Scraping Page {page}: {url}")
    driver.get(url)
    time.sleep(5)  # Let the page load completely

    # Scroll down to ensure content loads
    for _ in range(10):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(0.5)

    coin_data = extract_coin_data()

    if not coin_data:
        print(f"No data found on page {page}. Skipping...")
        continue

    all_data.extend(coin_data)

# Close the driver
driver.quit()

# Convert to DataFrame and save to CSV
df = pd.DataFrame(all_data)
df.to_csv('coinmarketcap_data.csv', index=False)
print("Data extraction complete. Data saved to coinmarketcap_data.csv")



# This code logic gets the whole data of the coinmarketcap website and saves it to a csv file.

# while True:
#     url = f"https://coinmarketcap.com/?page={page}"
#     print(f"Scraping Page {page}: {url}")
#     driver.get(url)
#     time.sleep(5)  # Wait for the page to fully load

#     # Scroll down to ensure content loads
#     for _ in range(10):
#         driver.execute_script("window.scrollBy(0, 1000);")
#         time.sleep(0.5)

#     coin_data = extract_coin_data()

#     # Stop if no more data is found
#     if not coin_data:
#         print(f"No data found on page {page}. Stopping...")
#         break

#     all_data.extend(coin_data)
#     page += 1

# driver.quit()