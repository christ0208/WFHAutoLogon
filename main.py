from WebLogin import WebLogin
from dotenv import load_dotenv
import os
import base64
from selenium import webdriver

CURRENT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--user-agent=' + CURRENT_USER_AGENT)
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')

chrome_driver = None

def fetch_necessary_data():
    return os.getenv("MESSIER_URL"), {
        'username': os.getenv("MESSIER_USERNAME"),
        'password': base64.b64decode(os.getenv("MESSIER_PASS")).decode("ascii")
    }, os.getenv("HC_URL"), \
    {
        'username': os.getenv("HC_USERNAME"),
        'password': base64.b64decode(os.getenv("HC_PASS")).decode("ascii")
    }

def prep_chrome_driver():
    global chrome_driver
    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)


if __name__ == '__main__':
    load_dotenv()
    prep_chrome_driver()
    messier_url, messier_credential, hc_url, hc_credential = fetch_necessary_data()
    WebLogin(chrome_driver, messier_url, messier_credential).messier_login()
    WebLogin(chrome_driver, hc_url, hc_credential).hc_login()