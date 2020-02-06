from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui


fp = webdriver.FirefoxProfile()
fp.set_preference("http.response.timeout", 2)
fp.set_preference("dom.max_script_run_time", 2)
driver = webdriver.Firefox(firefox_profile=fp)


for i in range(1,255):
 addres = ""
 addres = "http://10.10.6."+str(i)
 print(addres)
 driver.get(addres)
 
 if "Yealink" in driver.title :
  print ("YES - To jest YeaLink")
  elem_user = driver.find_element_by_name("username")
  elem_user.clear()
  elem_user.send_keys("admin")
  
  elem_pass = driver.find_element_by_name("pwd")
  elem_pass.clear()
  elem_pass.send_keys("0000")
  
  driver.find_element_by_id('idConfirm').click()
  wait = ui.WebDriverWait(driver,10)
  driver.implicitly_wait(10)
 
  try:
    driver.find_element_by_id("page-logo")
    print("PassWord OK")
  except :
    print ("PassWord BAD!")
  
 else:
  print ("NO - To nie jest YeaLink")
driver.close()
