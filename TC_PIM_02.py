from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class orange_hrm():

    def test(self):

        """
        1.Open orangehrm website in browser 
        2.Login with correct username and password
        3.In PIMmodule,Edit employee details in already employee list
        3. Result - Updated Sucessfully & Saved Sucessfully
        """
        
        # Open orangehrm login page in browser
        url1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Firefox()
        driver.get(url1)
        driver.maximize_window()
        time.sleep(5)

        # Enter login user name
        xpath_of_user_name = "//input[@placeholder='Username']"
        user_dialog_box = driver.find_element(By.XPATH,xpath_of_user_name)
        user_dialog_box.send_keys("Admin")
        time.sleep(3)

        # Enter login password
        xpath_of_password = "//input[@placeholder='Password']"
        password_dialog_box = driver.find_element(By.XPATH,xpath_of_password)
        password_dialog_box.send_keys("admin123")
        time.sleep(3)

        # Enter or Click login button
        xpath_of_login_button = "//button[@type='submit']"
        enter_login = driver.find_element(By.XPATH,xpath_of_login_button)
        enter_login.click()
        time.sleep(6)

        # Select PIM option
        xpath_of_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        pim_option_box = driver.find_element(By.XPATH,xpath_of_pim)
        pim_option_box.click()
        time.sleep(6)

        # Select Edit employee option
        xpath_of_edit_employee = "(//i[@class='oxd-icon bi-pencil-fill'])[2]"
        edit_employee = driver.find_element(By.XPATH,xpath_of_edit_employee)
        edit_employee.click()
        time.sleep(6)

        # Change Smoker option in employee details
        xpath_of_Smoker_option = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
        smoker_option = driver.find_element(By.XPATH,xpath_of_Smoker_option)
        smoker_option.click()
        time.sleep(6)

        # Saving the updates in employee details
        xpath_for_save_button1 = "(//button[@type='submit'])[1]"
        save_button1 = driver.find_element(By.XPATH,xpath_for_save_button1)
        save_button1.click()
        time.sleep(6)

        waiter = WebDriverWait(driver,20)
        # Add or Change Blood group of employee
        xpath_of_blood_group = "(//div[@class='oxd-select-text-input'])[3]"
        blood_group = driver.find_element(By.XPATH,xpath_of_blood_group)
        blood_group.send_keys("B+")
        sel_group=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='B+']")))
        sel_group.click()
        time.sleep(6)

        # Again Saving the updates in employee details
        xpath_for_save_button2 = "(//button[@type='submit'])[2]"
        save_button2 = driver.find_element(By.XPATH,xpath_for_save_button2)
        save_button2.click()
        time.sleep(5)


       
        

tc = orange_hrm()
tc.test()