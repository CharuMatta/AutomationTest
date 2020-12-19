import unittest
import time
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class KiwiSaver(unittest.TestCase):
    
    def setUp(self):
        """I want that the KiwiSaver Retirement Calculator users are able to calculate what their KiwiSaver projected balance would be at retirement"""
        self.config = configparser.ConfigParser()
        self.config.read('Westpac_Test/config.ini')
        # create a new Firefox session
        firefox_path = self.config['PATH']['FIREFOX_PATH'] #path of your local firefox driver
        self.driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
        # navigate to the application home page
        self.driver.get(self.config['LOGIN']['BASE_URL'])

    def test_retirement_calculater_case1(self):
        """TScenario 2.1 :-User whose Current age is 30 is Employed @ a Salary 82000 p/a, contributes to KiwiSaver @ 4% and chooses a Defensive risk profile can calculate his projected balances at retirement"""  
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
        #input data to current age tab
        current_age_xpath= self.config['XPATH']['CURRENT_AGE_INPUT'] #navigating to icon button
        current_age_input=self.driver.find_element_by_xpath(current_age_xpath)
        current_age_input.send_keys('30') #input data
        time.sleep(2)
        #to click dropdown options
        mySelectElement = self.config['XPATH']['DROPDOWN_LIST']
        dropDownMenu = self.driver.find_element_by_xpath(mySelectElement)
        dropDownMenu.click()
        #selecting options from dropdown list
        empl_status_xpath = self.config['XPATH']['EMPLOYMENT_STATUS_INPUT']
        empl_status_input = self.driver.find_element_by_xpath(empl_status_xpath)
        empl_status_input.click()
        time.sleep(2)
        #sending input to salary tab
        salary_xpath= self.config['XPATH']['SALARY_INPUT'] 
        salary_input=self.driver.find_element_by_xpath(salary_xpath)
        salary_input.send_keys('84000')
        time.sleep(2)
        #clicking options from membership %
        membership_xpath= self.config['XPATH']['MEMBERSHIP_INPUT']
        radio_input=self.driver.find_element_by_xpath(membership_xpath)
        radio_input.click()
        time.sleep(2)
        #clicking option for risk profile
        risk_profile_xpath= self.config['XPATH']['RISK_PROFILE_DEFENSIVE'] #navigating to icon button
        risk_profile_input=self.driver.find_element_by_xpath(risk_profile_xpath)
        risk_profile_input.click()
        time.sleep(3)
        #clicking button for calculation
        calculate_xpath= self.config['XPATH']['CALCULATE_BUTTON'] #navigating to icon button
        calculate_button=self.driver.find_element_by_xpath(calculate_xpath)
        time.sleep(3)
        calculate_button.click()
        time.sleep(5)
        #getting balance for retirement
        result_xpath= self.config['XPATH']['CAL_RESULT'] #navigating to icon button
        result_text=self.driver.find_element_by_xpath(result_xpath).text
        print("Calculated balances at retirement:- ",result_text)
        time.sleep(2)

    def test_retirement_calculater_case2(self):
        """TScenario 2.1 :-User whose current aged 45 is Self-employed, current KiwiSaver balance is $100000, voluntary contributes $90 fortnightly and chooses Conservative risk profile with saving goals requirement of $290000 can calculate his projected balances at retirement"""  
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
        #input data to current age tab
        current_age_xpath= self.config['XPATH']['CURRENT_AGE_INPUT'] #navigating to icon button
        current_age_input=self.driver.find_element_by_xpath(current_age_xpath)
        current_age_input.send_keys('45') #input data
        time.sleep(2)
        #to click dropdown options
        mySelectElement = self.config['XPATH']['DROPDOWN_LIST']
        dropDownMenu = self.driver.find_element_by_xpath(mySelectElement)
        dropDownMenu.click()
        #selecting options from dropdown list
        self_empl_status_xpath = self.config['XPATH']['SELF_EMPLOYMENT_STATUS_INPUT']
        self_empl_status_input = self.driver.find_element_by_xpath(self_empl_status_xpath)
        self_empl_status_input.click()
        time.sleep(2)
        #sending input to kiwi current balance
        kiwi_bal_xpath= self.config['XPATH']['CURRENT_KIWI_BALANCE'] 
        kiwi_bal_input=self.driver.find_element_by_xpath(kiwi_bal_xpath)
        kiwi_bal_input.send_keys('100000')
        time.sleep(2)
        #clicking options from valuntary contribution
        voluntary_xpath= self.config['XPATH']['VOLUNTARY_CONTRI_INPUT']
        voluntary_input=self.driver.find_element_by_xpath(voluntary_xpath)
        voluntary_input.send_keys('90')
        time.sleep(2)
        #to click dropdown options-Frequency DropList
        mySelectElement = self.config['XPATH']['VOLUNTARY_CONTRI_DROPDOWN']
        dropDownMenu = self.driver.find_element_by_xpath(mySelectElement)
        dropDownMenu.click()
        #selecting options from Frequency DropList
        frequncy_xpath = self.config['XPATH']['VOLUNTARY_CONTRI_DROPDOWN_FORTNIGHTLY']
        frequncy_input = self.driver.find_element_by_xpath(frequncy_xpath)
        frequncy_input.click()
        time.sleep(2)
        #clicking option for risk profile
        risk_profile_xpath= self.config['XPATH']['RISK_PROFILE_CONSERVATIVE'] #navigating to icon button
        risk_profile_input=self.driver.find_element_by_xpath(risk_profile_xpath)
        risk_profile_input.click()
        time.sleep(2)
        #clicking options from saving goals %
        saving_xpath= self.config['XPATH']['SAVING_GOAL_INPUT']
        saving_input=self.driver.find_element_by_xpath(saving_xpath)
        saving_input.send_keys('290000')
        time.sleep(2)
        #clicking button for calculation
        calculate_xpath= self.config['XPATH']['CALCULATE_BUTTON'] #navigating to icon button
        calculate_button=self.driver.find_element_by_xpath(calculate_xpath)
        time.sleep(2)
        calculate_button.click()
        time.sleep(2)
        #getting balance for retirement
        result_xpath= self.config['XPATH']['CAL_RESULT'] #navigating to icon button
        result_text=self.driver.find_element_by_xpath(result_xpath).text
        print("Calculated balances at retirement:- ",result_text)
        time.sleep(2)

    def test_retirement_calculater_case3(self):
        """TScenario 2.2 :-User whose current aged 55 is not employed, current KiwiSaver balance is $140000, voluntary contributes $10 annually and chooses Balanced risk profile with saving goals requirement of $200000 is able to calculate his projected balances at retirement"""  
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
        #input data to current age tab
        current_age_xpath= self.config['XPATH']['CURRENT_AGE_INPUT'] #navigating to icon button
        current_age_input=self.driver.find_element_by_xpath(current_age_xpath)
        current_age_input.send_keys('55') #input data
        time.sleep(2)
        #to click dropdown options
        mySelectElement = self.config['XPATH']['DROPDOWN_LIST']
        dropDownMenu = self.driver.find_element_by_xpath(mySelectElement)
        dropDownMenu.click()
        #selecting options from dropdown list
        self_empl_status_xpath = self.config['XPATH']['NOT_EMPLOYMENT_STATUS_INPUT']
        self_empl_status_input = self.driver.find_element_by_xpath(self_empl_status_xpath)
        self_empl_status_input.click()
        time.sleep(2)
        #sending input to kiwi current balance
        kiwi_bal_xpath= self.config['XPATH']['CURRENT_KIWI_BALANCE'] 
        kiwi_bal_input=self.driver.find_element_by_xpath(kiwi_bal_xpath)
        kiwi_bal_input.send_keys('140000')
        time.sleep(2)
        #clicking options from valuntary contribution
        voluntary_xpath= self.config['XPATH']['VOLUNTARY_CONTRI_INPUT']
        voluntary_input=self.driver.find_element_by_xpath(voluntary_xpath)
        voluntary_input.send_keys('10')
        time.sleep(2)
        #to click dropdown options-Frequency DropList
        mySelectElement = self.config['XPATH']['VOLUNTARY_CONTRI_DROPDOWN']
        dropDownMenu = self.driver.find_element_by_xpath(mySelectElement)
        dropDownMenu.click()
        #selecting options from Frequency DropList
        frequncy_xpath = self.config['XPATH']['VOLUNTARY_CONTRI_DROPDOWN_ANNUAL']
        frequncy_input = self.driver.find_element_by_xpath(frequncy_xpath)
        frequncy_input.click()
        time.sleep(2)
        #clicking option for risk profile
        risk_profile_xpath= self.config['XPATH']['RISK_PROFILE_BALANCED'] #navigating to icon button
        risk_profile_input=self.driver.find_element_by_xpath(risk_profile_xpath)
        risk_profile_input.click()
        time.sleep(2)
        #clicking options from saving goals %
        saving_xpath= self.config['XPATH']['SAVING_GOAL_INPUT']
        saving_input=self.driver.find_element_by_xpath(saving_xpath)
        saving_input.send_keys('200,000')
        time.sleep(2)
        #clicking button for calculation
        calculate_xpath= self.config['XPATH']['CALCULATE_BUTTON'] #navigating to icon button
        calculate_button=self.driver.find_element_by_xpath(calculate_xpath)
        time.sleep(2)
        calculate_button.click()
        time.sleep(2)
        #getting balance for retirement
        result_xpath= self.config['XPATH']['CAL_RESULT'] #navigating to icon button
        result_text=self.driver.find_element_by_xpath(result_xpath).text
        print("Calculated balances at retirement:- ",result_text)
        time.sleep(2)

    def tearDown(self):
        #closing the Firefox session
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
