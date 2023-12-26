# wikipedia-scraper

## Usage
- run `pip install -r requirements.txt` to install dependencies
- update `url` variable in `main.py` to the url of the wikipedia page you want to scrape
- run `python main.py` to scrape the page and store the results into a .txt file


## Web scraping steps
- inspect the HTML structure of the web page
- identify the HTML element(s) that contain the data you want to extract
- get the HTML content using the `requests` library
- extract the data from the HTML element(s) with the `BeautifulSoup` library
- utilize the data in desired manner 


## Example URLs
- https://en.wikipedia.org/wiki/Web_scraping
- https://en.wikipedia.org/wiki/Tampa,_Florida