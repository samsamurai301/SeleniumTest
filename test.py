from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep as slp

def click(x, w =1): #Enter xpath that you copied from element from inspect mode in chrome for wait time enter vlaue in seconds
    clickEle = driver.find_element(By.XPATH, x)
    clickEle.click()
    slp(w)
    return

def scroll(p, w=2): #Enter value in integer such as 100, 200, ..., etc for wait time enter value in seconds
    driver.execute_script("window.scrollBy(0, %s);"%p)
    slp(w)
    return

def text(x,s,w=1): #Enter xpath and then enter string value  and wait time in seconds(optional defaul = 1 second)
    driver.find_element(By.XPATH, x).send_keys(s)
    slp(w)
    return

parnerID = "21-220515" 
email = "21-220515@adi-gmbh.de"
pwd = "adi12345#"
options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome(options=options)
driver.get("https://mobile.drivenscan.app")
slp(3)
driver.maximize_window()
slp(1)

text('//*[@id="root"]/div/div/div/div/div/div[3]/div/form/div[1]/div/div/input', parnerID) #first partner ID field text entry
text('//*[@id="root"]/div/div/div/div/div/div[3]/div/form/div[2]/div/div/input', email) #second email field text entry
text('//*[@id="root"]/div/div/div/div/div/div[3]/div/form/div[3]/div/div/input', pwd) #third password field text entry
click('//*[@id="root"]/div/div/div/div/div/div[3]/div/form/div[4]/div/button') #clicking action on signin button
click('//*[@id="root"]/div[2]/div/div/div/div/div/div/div/div') #cliking action on Enable/Disable slider button 
click('//*[@id="qr"]') #clicking action on qr radio button
click('//*[@id="root"]/div[2]/div/div/div/form/div/div[1]/div[1]/div[3]/div[3]/div/div/ul/li[8]') #clicking action on color palet grey
scroll(200, 3) #scrolling to 200 pixle down side from current view
click('//*[@id="root"]/div[2]/div/div/div/form/div/div[1]/div[1]/div[6]/div[3]/div/div[1]',10) #clicking action on start/scan button

driver.quit()
