'''
Created on Jun 25, 2023

@author: Hcl
'''

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

print('Facebook Login In Edge Browser')
driver=webdriver.ChromiumEdge()
driver.get('https://www.facebook.com/')
driver.find_element('id', 'email').send_keys('sathish@gmail.com')
driver.find_element('id', 'pass').send_keys('12345678')
driver.find_element('name','login').click()
print(driver.current_url,driver.title,sep='\n')
driver.close()