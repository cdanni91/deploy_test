# BeautifulSoup imports
from bs4 import BeautifulSoup

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Flask imports
from flask import Flask, request


'''0. We create the flask app'''
app = Flask(__name__)


'''1. Main function'''
def main_script():

    # Url to scrape
    url = 'https://www.wikipedia.org/'

    # Selenium parameters, headless for deploy

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)

    # Opens the url
    driver.get(url)

    # Parse the url with beautifulsoup
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    # Find the class that has the english text
    lang_elements = soup.find_all(class_='central-featured-lang lang2')

    # Get the 'English' text and print it from inside 'strong' attribute
    strong_texts = []

    for element in lang_elements:
        strong_tag = element.find('strong')
        if strong_tag:
            strong_texts.append(strong_tag.get_text())

    print(strong_texts)
    return strong_texts
    

'''2. Configs for the API and Flask'''

@app.route('/', methods = ['GET'])

def home():
    if (request.method == 'GET'):

        return main_script()


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')