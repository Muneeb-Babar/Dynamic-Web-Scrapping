
# Dynamic Web Scraping

**Dynamic Web Scraping** is a project designed to extract data from dynamic websites efficiently. It leverages modern tools and techniques to handle JavaScript-rendered content and provides a flexible framework for scraping data from CoinMarketCap.

## Features

* **Dynamic Content Handling**: Scrape data from websites with JavaScript-rendered content (e.g., CoinMarketCap).
* **Customizable**: Easily configure scraping rules and targets.
* **Scalable**: Supports scraping multiple pages and large datasets.
* **Error Handling**: Robust mechanisms to handle common scraping issues (e.g., missing data, dynamic content loading).

## Requirements

* Python 3.x
* Required libraries (install via `requirements.txt`):

  * `requests`
  * `beautifulsoup4`
  * `selenium`
  * `pandas`
  * `chromedriver_autoinstaller`

You can install these dependencies by running:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/dynamic-web-scraping.git
   cd dynamic-web-scraping
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the appropriate ChromeDriver for your system from [here](https://sites.google.com/a/chromium.org/chromedriver/). Make sure to match the version with your installed Chrome browser version.

## Usage

1. Update the `CHROMEDRIVER_PATH` variable in the script (`scraper.py`) to the path of your `chromedriver.exe`.

2. Run the scraper:

   ```bash
   python scraper.py
   ```

   * This script will scrape data from the first 10 pages of CoinMarketCap.
   * It scrolls through the page to ensure dynamic content is loaded.
   * The extracted data will be saved in a CSV file called `coinmarketcap_data.csv`.

3. The data will be saved to the `coinmarketcap_data.csv` file, which includes:

   * **Name**: Coin name
   * **Symbol**: Coin symbol
   * **Price**: Current price of the coin
   * **24h %**: Percentage change in the last 24 hours
   * **7d %**: Percentage change in the last 7 days
   * **Market Cap**: Market capitalization of the coin
   * **Volume (24h)**: Trading volume in the last 24 hours

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

* Add new scraping features
* Improve error handling
* Create better configuration for scaling up the project

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact:
[muneeb63ahmad63@gmail.com](mailto:muneeb63ahmad63@gmail.com)

---

### Notes:

* The code currently scrapes data from CoinMarketCap for the first 10 pages. You can modify the `range(1, 11)` in the script to change the number of pages scraped.
* The project uses **Selenium** for dynamic web scraping and **Pandas** to store the extracted data.


