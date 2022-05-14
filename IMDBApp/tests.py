# # from django.test import LiveServerTestCase
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys

# # # Create your tests here.
# # class PlayerFormTest(LiveServerTestCase):

# #   def testform(self):
# #     selenium = webdriver.Chrome()
# #     #Choose your url to visit
# #     selenium.get('http://127.0.0.1:8000/prediction/main')
# #     #find the elements you need to submit form
# #     movie_name = selenium.find_element_by_id('movie_name')
# #     duration = selenium.find_element_by_id('duration')
# #     genre = selenium.find_element_by_id('genre')
# #     director = selenium.find_element_by_id('director')
# #     actor1 = selenium.find_element_by_id('actor1')
# #     actor2 = selenium.find_element_by_id('actor2')
# #     movie_budget = selenium.find_element_by_id('movie_budget')

# #     submit = selenium.find_element_by_id('submit_button')

# #     #populate the form with data
# #     movie_name.send_keys('RRR')
# #     duration.send_keys('122')
# #     genre.send_keys('90')
# #     director.send_keys('120')
# #     actor1.send_keys('120')
# #     actor2.send_keys('150')
# #     movie_budget.send_keys('50')


# #     #submit form
# #     submit.send_keys(Keys.RETURN)

# #     #check result; page source looks at entire html document
# #     assert 'RRR' in selenium.page_source
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
