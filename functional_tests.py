from selenium import webdriver
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
		self.fail('Finish the test!')

		# He is invited to enter a to-do item straight away

		# He types "Buy GTAV for PS4" into a text box (Jamie likes games)

		# When he hits enter, the page updates and now the page shows;
		# "1: Buy GTAV for PS4" as an item in a to-do list

		# There is still a text box inviting him to add another item
		# He enters "Buy FFVIIHD on SEN" (Jamie's favourite game in the world)

		# The page updates again and now shows both items on his list

		# Jamie wonders if the site will remember his to-do items
		# He sees that the site has generated a unique URL for him

		# He visits the unique URL and the to-do list is there

		# He is satisfied and closes the browser
		browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')