
from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Hosttest(LiveServerTestCase):
    def testhomepage(self):
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/')
        time.sleep(5)
        assert "IMDB Box Office Prediction" in driver.title
    
class LoginFormTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()
        driver.get('http:127.0.0.1:8000/accounts/login')
        time.sleep(3)
        
        user_name = driver.find_element_by_id('username')
        user_password = driver.find_element_by_id('password')
        time.sleep(3)
        
        submit = driver.find_element_by_id('submit1')
        user_name.send_keys('Karishma')
        user_password.send_keys('karishma')
        submit.send_keys(Keys.RETURN)
        
        # assert 'Karishma' in driver.page_source
      
class RegisterFormTest(LiveServerTestCase):
    def testform1(self):
        driver = webdriver.Chrome()
        driver.get('http:127.0.0.1:8000/accounts/register')
        time.sleep(3)
        
        firstname = driver.find_element_by_id('first_name1')
        lastname = driver.find_element_by_id('last_name1')
        username = driver.find_element_by_id('username1')
        email = driver.find_element_by_id('email1')
        password = driver.find_element_by_id('password1')
        passwordagain = driver.find_element_by_id('password2')
        time.sleep(3)
        
        submit2 = driver.find_element_by_id('submit2')
        firstname.send_keys('Deepika')
        lastname.send_keys('Padukone')
        username.send_keys('Deepika')
        email.send_keys('deepika@gmail.com')
        password.send_keys('deepika')
        passwordagain.send_keys('deepika')
        submit2.send_keys(Keys.RETURN)
        
        #assert 'Deepika' in driver.page_source  
        