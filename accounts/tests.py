# from django.test import TestCase

# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Create your tests here.
# class PlayerFormTest(LiveServerTestCase):

#   def login(self):
#     selenium = webdriver.Chrome()
#     #Choose your url to visit
#     selenium.get('http://127.0.0.1:8000/accounts/login')
#     #find the elements you need to submit form
    
#     username = selenium.find_element_by_id('username')
#     password = selenium.find_element_by_id('password')

#     submit = selenium.find_element_by_id('submit1')

#     #populate the form with data
    
#     username.send_keys('Arya')
#     password.send_keys('arya')


#     #submit form
#     submit.send_keys(Keys.RETURN)

#     #check result; page source looks at entire html document
#     assert 'Arya' in selenium.page_source

# # Create your tests here.
