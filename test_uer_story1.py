import unittest
import time
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class KiwiSaver(unittest.TestCase):
    
    def setUp(self):
        """I want that while using the KiwiSaver Retirement Calculator all fields in the calculator have got the information icon present"""
        self.config = configparser.ConfigParser()
        self.config.read('Westpac_Test/config.ini')
        # create a new Firefox session
        firefox_path = self.config['PATH']['FIREFOX_PATH'] #path of your local firefox driver
        self.driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
        # navigate to the application home page
        self.driver.get(self.config['LOGIN']['BASE_URL'])

    def test_kiwiSaver_retirement_calculater(self):
        """TScenario 1 :-Given User Clicks information icon besides Current age the message “This calculator has an age limit of 64 years old as you need to be under the age of 65 to join KiwiSaver.” is displayed below the current age field."""
       
        #navigating kiwisaver tab using id
        kiwisaver_tab = self.driver.find_element_by_id(self.config['LOGIN']['KIWISAVER_TAB'])
        actions = ActionChains(self.driver) #using mouse hover funcationality
        actions.move_to_element(kiwisaver_tab).perform()
        time.sleep(2)
        #navigating kiwisaver calculater button by id
        retirement_cal_tab = self.driver.find_element_by_id(self.config['LOGIN']['RETIREMENT_CAL_TAB'])
        retirement_cal_tab.click() #clicking button
        time.sleep(2)
        #navigating Westpac KiwiSaver Scheme Retirement Calculator button 
        retirement_cal_form = self.driver.find_element_by_id(self.config['LOGIN']['RETIREMENT_CAL_FORM'])
        retirement_cal_form.click() #clicking button
        time.sleep(2)

        # switching to iframe 
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name(self.config['IFRAME']['PATH']))
        button_xpath= self.config['XPATH']['ICON_BUTTON'] #navigating to icon button
        icon_button=self.driver.find_element_by_xpath(button_xpath)
        icon_button.click()
        time.sleep(2)

        #getting text for validating content
        tag_text = self.driver.find_element_by_xpath(self.config['XPATH']['TAG_TEXT']).text
        time.sleep(5)
        self.assertTrue(tag_text,(self.config['TEXT']['TEXT_MATCH'])) #validation
        self.driver.switch_to.default_content() #switch to normal window
        time.sleep(1)

    def tearDown(self):
        #closing the Firefox session
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
