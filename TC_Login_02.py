from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class orange_hrm():

    def test(self):

        """
        1.Open orangehrm website in browser 
        2.Login with wrong password
        3. Result - invalid credential
                   
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

        # Enter wrong or invalid password

        xpath_of_password = "//input[@placeholder='Password']"
        password_dialog_box = driver.find_element(By.XPATH,xpath_of_password)
        password_dialog_box.send_keys("Invalid password")
        time.sleep(3)

        # Enter or Click login button

        xpath_of_login_button = "//button[@type='submit']"
        enter_login = driver.find_element(By.XPATH,xpath_of_login_button)
        enter_login.click()
  

tc = orange_hrm()
tc.test()