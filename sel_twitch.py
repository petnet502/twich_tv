#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

mobile_emulation={"deviceName": "iPhone SE"}
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://m.twitch.tv")
driver.maximize_window()
element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="ScCoreButton-sc-ocjdkq-0 jUzoXZ"]')))
element.click()
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH, value="//div[text()='Browse']").click()
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH, value='//input[@placeholder="Search"]').click()
search_field=driver.find_element(by=By.XPATH, value='//input[@type="search"]')
search_field.send_keys("StarCraft II")
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
# driver.find_element(by=By.XPATH, value='//div[@class="Layout-sc-1xcs6mc-0 kmSOnB"]').click()
driver.find_element(by=By.XPATH, value='//p[@class="CoreText-sc-1txzju1-0 bqCGPR"]').click()
# driver.find_element(by=By.XPATH, value='//p[@title="StarCraft II"]').click()
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,900)","")
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH, value='//h2[contains(text(), "THE WORST MARVEL RIVALS GAMEPLAY")]').click()
driver.implicitly_wait(15)
driver.save_screenshot('twitch_tv.png')
driver.quit()