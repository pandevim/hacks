# This is the spammer bot I made to overload our class information form.

from selenium import webdriver
import random
import string
import time


url = "https://goo.gl/forms/cZtBjpxbLVIcGMkr2"

driver = webdriver.Firefox()
driver.get( url )

xpath_field_a = "/html/body/div/div[2]/form/div/div[2]/div[2]/div["
xpath_field_b = "]/div/div[2]/div/div[1]/div/div[1]/input"
xpath_radio_a = "/html/body/div/div[2]/form/div/div[2]/div[2]/div[6]/div/div[2]/div/content/div/label["
xpath_radio_b = "]/div/div[1]/div[3]/div"
xpath_submit = "/html/body/div/div[2]/form/div/div[2]/div[3]/div[1]/div/div/content/span"
xpath_newResponce = "/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/a"

name = xpath_field_a + str(1) + xpath_field_b
reg_no = xpath_field_a + str(2) + xpath_field_b
roll_no = xpath_field_a + str(3) + xpath_field_b
mob_no = xpath_field_a + str(4) + xpath_field_b


for _ in range(0, 200):
	random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

	driver.find_element_by_xpath(name).send_keys( random_string )
	time.sleep(0.5)
	driver.find_element_by_xpath(reg_no).send_keys(str( random.randint(11111111,99999999) ))
	time.sleep(0.5)
	driver.find_element_by_xpath(roll_no).send_keys(str( random.randint(1, 68) ))
	time.sleep(0.5)
	driver.find_element_by_xpath(mob_no).send_keys(str( random.randint(1111111111, 9999999999) ))
	time.sleep(0.5)
	driver.find_element_by_xpath( xpath_radio_a + str( random.randint(1,2) ) + xpath_radio_b ).click()
	time.sleep(0.5)
	driver.find_element_by_xpath( xpath_submit ).click()

	time.sleep( random.randint(1,3) )
driver.find_element_by_xpath( xpath_newResponce ).click()
