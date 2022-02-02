from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv


def get_html():
    url = 'https://www.amazon.com.br/s?k=iphone'
    options = Options()
    options.headless = True
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get(url)
    body_page = browser.page_source
    soup = BeautifulSoup(body_page, 'lxml')
    cards = soup.find_all(
        'div', {'data-asin': True, 'data-component-type': 's-search-result'}
    )
    return cards


def scrape_data(card):
    try:
        h2 = card.h2
    except:
        title = ''
    else:
        title = h2.text.strip()
    try:
        price = card.find('span', class_='a-offscreen').text
    except:
        price = ''
    else:
        price = card.find('span', class_='a-offscreen').text
    data = {'Title': title, 'Price': price}
    return data


def format_data(html):
    ads_data = []
    for card in html:
        data = scrape_data(card)
        ads_data.append(data)
    return ads_data


def write_csv(ads):
    with open('iphone_price.csv', 'w', newline='', encoding='utf-8') as f:
        fields = ['Title', 'Price']
        writer = csv.DictWriter(
            f, fieldnames=fields, delimiter=';', quoting=csv.QUOTE_MINIMAL
        )
        for ad in ads:
            writer.writerow(ad)
    df = pd.read_csv("iphone_price.csv", sep=';', index_col=False)
    df.to_excel("iphone_price.xlsx", header=["Title", "Price"], index=False)
    os.remove('iphone_price.csv')


def main():
    html = get_html()
    prices = format_data(html)
    write_csv(prices)


if __name__ == '__main__':
    main()
