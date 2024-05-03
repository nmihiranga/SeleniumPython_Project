#import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#os.environ['PATH'] += r"Driver path here"

#To stop chrome being closing immediately
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#driver.maximize_window()

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

driver.implicitly_wait(5)
downloadBtn = driver.find_element(By.ID, "downloadButton")
downloadBtn.click()

progressElement = driver.find_element(By.CLASS_NAME, "progress-label")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"), "Complete!"
    )
)