import logging
import os 
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag
from requests import Response






class Scraper():
    
    def store_page_contents_from_url(self, url: str) -> str:
        html: bytes = self._get_raw_html(url)
        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        page_title: str = self._get_page_title(soup)
        content_text: str = self._get_content_text(soup)
        file_path: str = self._store_content_text_to_file(page_title, content_text)
        logging.info(f'    - Page contents from {url} stored to {file_path}')
        return file_path
        
        
        
    def _get_raw_html(self, url: str) -> bytes:
        response: Response = requests.get(url)
        status_code: int = response.status_code
        if status_code != 200:
            raise Exception(f'Error requesting {url}: status code {status_code}')
        html: bytes = response.content
        return html
    
    
    def _get_page_title(self, soup: BeautifulSoup) -> str:
        title_tag: Tag = soup.find('title')
        title: str = title_tag.text
        return title
    
    
    def _get_content_text(self, soup: BeautifulSoup) -> str:
        content_div: Tag = soup.find(class_="mw-parser-output")
        content_text: str = content_div.text
        return content_text
    
    
    def _store_content_text_to_file(
            self, 
            page_title: str, 
            content_text: str,
            filestore_dir_path: str = 'filestore'
        ) -> str:
        
        Path(filestore_dir_path).mkdir(exist_ok=True)
        filename: str = f'{page_title}.txt'
        file_path: str = os.path.join(filestore_dir_path, filename)
        with open(file_path, 'w') as f:
            f.write(content_text)
        return file_path
    
    
    def _get_links(self, html: bytes) -> list:
        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        links: list = soup.find_all('a')
        for link in links[:5]:
            print(link.get('href'))
        return links
        
        
        
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    url: str = 'https://en.wikipedia.org/wiki/Web_scraping'
    Scraper().store_page_contents_from_url(url)