from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class orange_hrm():

    def test(self):

        """
        1.Open orangehrm website in browser 
        2.Login with correct username and password
        3.In Admin page,from Menu options (sidepane name) is available
        4.Fill in search box by send letters to validate
       
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
        time.sleep(5)
        
       
        menu_option=[]
        side_pane = driver.find_elements(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
        for i in side_pane:
            print(i.text)
            menu_option.append(i.text)
        print(menu_option)

        for i in menu_option:
            driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(i)
            time.sleep(5)  
   
            result = driver.find_element(By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']//span").text
            assert result.lower() == i.lower()
            time.sleep(3)

            driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.CONTROL+"a")
            time.sleep(5)

            driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.BACK_SPACE)
            time.sleep(5)

tc = orange_hrm()
tc.test()
