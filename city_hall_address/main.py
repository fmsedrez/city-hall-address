from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_city_hall_address(city_name: str):
    driver.get(
        f'https://www.google.com/search?q=endere%C3%A7o+prefeitura+municipal+de'
        f'+{city_name.replace(" ", "%20")}')
    element = driver.find_element(By.CLASS_NAME,
                                  'LrzXr')
    print(element.text)


if __name__ == "__main__":
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    get_city_hall_address('Pelotas')
    get_city_hall_address('Cascavel')
    get_city_hall_address('Porto Alegre')
    driver.quit()
