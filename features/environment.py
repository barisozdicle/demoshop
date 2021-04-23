from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('start-maximized')
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
