from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj1 = Service()

driver = webdriver.Chrome(service=obj1)

driver.get("https://www.fitpeo.com/")

driver.maximize_window()
driver.find_element(By.XPATH,"//div[text()='Revenue Calculator']").click()
time.sleep(3)
dragbox = driver.find_element(By.XPATH,"//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-sy3s50']")
actionbox = ActionChains(driver)
actionbox.drag_and_drop_by_offset(dragbox,93,0).perform()
#above method changes the slider value with offset upto 817 which is reflected in below text box of the slider in webpage
time.sleep(3)
temp = driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']")
time.sleep(5)
temp.clear()
temp.send_keys("820")
#print(temp.text) #no output
#print("HI",temp.get_attribute("value"))

checks = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
subheads = driver.find_elements(By.XPATH,"//p[@class='MuiTypography-root MuiTypography-body1 inter css-1s3unkt']")
target = ['CPT-99091', 'CPT-99453', 'CPT-99454','CPT-99474']
for j in subheads:
    if j.text in target:
        ind = subheads.index(j)
        #print(index)
        checks[ind].click()



#2 part of program for loop -> accessing checkboxes works fine.