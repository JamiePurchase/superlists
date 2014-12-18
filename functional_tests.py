from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	
	# This gets run before each test
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	# This gets run after each test
	def tearDown(self):
		self.browser.quit()
		
	# We use the word test at the start so that the test runner knows that it's a test
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Jamie is going to try a new online to-do app.
		# He navigates to the homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention to do lists
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		# He is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		# He types "Buy GTAV for PS4" into a text box (Jamie likes games)
		inputbox.send_keys('Buy GTAV for PS4')

		# When he hits enter, the page updates and now the page shows;
		# "1: Buy GTAV for PS4" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		import time
		# time.sleep(10)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy GTAV for PS4', [row.text for row in rows])

		# There is still a text box inviting him to add another item
		# He enters "Buy FFVIIHD on SEN" (Jamie's favourite game in the world)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy FFVIIHD on SEN')
		inputbox.send_keys(Keys.ENTER)

		# The page updates again and now shows both items on his list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy GTAV for PS4', [row.text for row in rows])
		self.assertIn('2: Buy FFVIIHD on SEN', [row.text for row in rows])

		# Jamie wonders if the site will remember his to-do items
		# He sees that the site has generated a unique URL for him
		self.fail('Finish the test!')

		# He visits the unique URL and the to-do list is there

		# He is satisfied and closes the browser
		browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')