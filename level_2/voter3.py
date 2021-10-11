#!/usr/bin/python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sitetoload = 'http://158.69.76.135/level2.php'

def gecko_test(site=sitetoload):
    """
    Use of gecko in firefox
    change of preferences in user-agent so simulate windows OS
    """
    # set the driver
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", \
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) \
        Gecko/20100101 Firefox/47.0")
    driver = webdriver.Firefox(profile)

    # load the site
    driver.get(site)
    wait = WebDriverWait(driver, 4)
    # set the value
    for x in range(0, 1024):
        # find the input text
        theid = driver.find_element_by_name('id')
        wait.until(EC.presence_of_element_located((By.NAME, 'id')));
        theid.send_keys("3360")
        # send the form
        theid.send_keys(Keys.RETURN)
        # wait
        sleep(1)

    # close site.
    driver.quit()


# make runable
if __name__ == '__main__':
    # here we go
    gecko_test()
