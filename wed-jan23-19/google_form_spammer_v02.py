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


while( True ):
	input_data = []
	input_data.append( ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]) )
	input_data.append( str(random.randint(11111111,99999999)) )
	input_data.append( str(random.randint(1, 68)) )
	input_data.append( str(random.randint(1111111111, 9999999999)) )
	input_data.append( str(random.randint(1,2)) )

	for i in range(0, 4):
		final_xpath = xpath_field_a + str(i + 1) + xpath_field_b
		driver.find_element_by_xpath( final_xpath ).send_keys( input_data[i] )
		time.sleep(0.5)

	driver.find_element_by_xpath( xpath_radio_a + input_data[4] + xpath_radio_b ).click()
	time.sleep(0.5)
	driver.find_element_by_xpath( xpath_submit ).click()

	time.sleep( random.randint(1,3) )
	driver.find_element_by_xpath( xpath_newResponce ).click()
