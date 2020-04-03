from WebLogin import WebLogin
from dotenv import load_dotenv
import os
import base64
from selenium import webdriver

chrome_driver = None

def fetch_necessary_data():
    return {
        'username': os.getenv("MESSIER_USERNAME"),
        'password': base64.b64decode(os.getenv("MESSIER_PASS")).decode("ascii")
    }, \
    {
        'username': os.getenv("HC_USERNAME"),
        'password': base64.b64decode(os.getenv("HC_PASS")).decode("ascii")
    }

def prep_chrome_driver():
    global chrome_driver
    chrome_driver = webdriver.Chrome()


if __name__ == '__main__':
    load_dotenv()
    prep_chrome_driver()
    messier_credential, hc_credential = fetch_necessary_data()
    WebLogin(chrome_driver, "https://messier.slc.net/Login.aspx", messier_credential).messier_login()