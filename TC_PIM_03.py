from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class orange_hrm():

    def test(self):

        """
        1.Open orangehrm website in browser 
        2.Login with correct username and password
        3.In PIMmodule, delete one employee in employee list
        3. Result -  Sucessfully Deleted
                   
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
        time.sleep(5)

        # Select PIM option
        xpath_of_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        pim_option_box = driver.find_element(By.XPATH,xpath_of_pim)
        pim_option_box.click()
        time.sleep(5)

        # Select Delete employee option
        xpath_of_delete_employee = "(//i[@class='oxd-icon bi-trash'])[1]"
        delete_employee = driver.find_element(By.XPATH,xpath_of_delete_employee)
        delete_employee.click()
        time.sleep(5)

        # Confirming Delete process
        xpath_of_confirm_delete = "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"
        confirm_delete = driver.find_element(By.XPATH,xpath_of_confirm_delete)
        confirm_delete.click()
        time.sleep(5)

        

tc = orange_hrm()
tc.test()