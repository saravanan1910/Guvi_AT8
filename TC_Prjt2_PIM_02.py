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
        3.In Admin page,from user management option to check dropdowns
        4.Under user role & status dropdowns value to be validate
       
        """
        
        # Open orangehrm login page in browser
        url1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Firefox()
        driver.get(url1)
        driver.maximize_window()
        driver.implicitly_wait(10)
       

        # Enter login user name
        xpath_of_user_name = "//input[@placeholder='Username']"
        user_dialog_box = driver.find_element(By.XPATH,xpath_of_user_name)
        user_dialog_box.send_keys("Admin")
        time.sleep(5)
        

        # Enter login password
        xpath_of_password = "//input[@placeholder='Password']"
        password_dialog_box = driver.find_element(By.XPATH,xpath_of_password)
        password_dialog_box.send_keys("admin123")
        time.sleep(5)
        

        # Enter or Click login button
        xpath_of_login_button = "//button[@type='submit']"
        enter_login = driver.find_element(By.XPATH,xpath_of_login_button)
        enter_login.click()
        time.sleep(6)

        # Click Admin page
        admin_option = driver.find_element(By.XPATH,"//span[text()='Admin']")
        admin_option.click()
        time.sleep(8)

        # Click User mangement
        user_management = driver.find_element(By.XPATH,"(//span[@class='oxd-topbar-body-nav-tab-item'])[1]")
        user_management.click()
        time.sleep(6)

        # Click Users
        users = driver.find_element(By.XPATH,"//a[@role='menuitem']")
        users.click()
        time.sleep(6)


        # system_user = driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill']")
        # system_user.click()
        # time.sleep(6)

        waiter = WebDriverWait(driver,20)

        user_role_name = driver.find_element(By.XPATH,"//label[normalize-space()='User Role']")
        print(user_role_name.text)
        time.sleep(5)

        user_role_option = waiter.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")))
        user_role_option.click()
        time.sleep(5)

        user_box = driver.find_elements(By.XPATH,"//div[@role='listbox']//span")
        for i in user_box:
            print(i.text)
        time.sleep(5)

        status_name = driver.find_element(By.XPATH,"//label[normalize-space()='Status']")
        print(status_name.text)
        time.sleep(5)

        status = waiter.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")))
        status.click()
        time.sleep(5)

        status_box = driver.find_elements(By.XPATH,"//div[@role='listbox']//span")
        for i in status_box:
            print(i.text)
        time.sleep(5)


tc = orange_hrm()
tc.test()