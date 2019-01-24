from db_setup import input_data, string, random
from selenium import webdriver


url = "https://goo.gl/forms/cZtBjpxbLVIcGMkr2"

driver = webdriver.Firefox()
driver.get( url )

xpath_field_a = "/html/body/div/div[2]/form/div/div[2]/div[2]/div["
xpath_field_b = "]/div/div[2]/div/div[1]/div/div[1]/input"
xpath_radio_a = "/html/body/div/div[2]/form/div/div[2]/div[2]/div[6]/div/div[2]/div/content/div/label["
xpath_radio_b = "]/div/div[1]/div[3]/div"
xpath_submit = "/html/body/div/div[2]/form/div/div[2]/div[3]/div[1]/div/div/content/span"
xpath_newResponce = "/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/a"

row = 0

while( True ):
	for i in range(0, 4):
		final_xpath = xpath_field_a + str(i + 1) + xpath_field_b
		driver.find_element_by_xpath( final_xpath ).send_keys( str(input_data[row][i]) )
		time.sleep(0.5)
	row += 1
	driver.find_element_by_xpath( xpath_radio_a + str(random.randint(1,2)) + xpath_radio_b ).click()
	time.sleep(0.5)
	driver.find_element_by_xpath( xpath_submit ).click()

	time.sleep( random.randint(1,3) )
	driver.find_element_by_xpath( xpath_newResponce ).click()
