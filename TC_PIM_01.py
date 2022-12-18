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
        3.In PIMmodule, Add new employee details 
        4.Fill the Personal details of employee and save it
        5. Result - Updated Sucessfully & Saved Sucessfully
      
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
        
        # Select PIM option
        xpath_of_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        pim_option_box = driver.find_element(By.XPATH,xpath_of_pim)
        pim_option_box.click()
        time.sleep(5)
        

        # Select Add employee option
        xpath_of_add_employee = "//*[contains(text(),'Add')]"
        add_employee = driver.find_element(By.XPATH,xpath_of_add_employee)
        add_employee.click()
        time.sleep(5)
        

        # Add employee first name
        xpath_of_employee_first_name = "//input[@placeholder='First Name']"
        first_name = driver.find_element(By.XPATH,xpath_of_employee_first_name)
        first_name.send_keys("Naren")
        time.sleep(5)
       

        # Add employee last name
        xpath_of_employee_last_name = "//input[@placeholder='Last Name']"
        last_name = driver.find_element(By.XPATH,xpath_of_employee_last_name)
        last_name.send_keys("Karthik")
        time.sleep(5)
       
       
        # Enter or Click save button
        xpath_of_save_button = "//button[@type='submit']"
        save_button = driver.find_element(By.XPATH,xpath_of_save_button)
        save_button.click()
        time.sleep(5)

        driver.execute_script("window.scrollBy(0,400)")
        time.sleep(5)

        # Enter DOB of Employee
        xpath_for_DOB = "(//input[@placeholder='yyyy-mm-dd'])[2]"
        dob_0f_employee = driver.find_element(By.XPATH,xpath_for_DOB)
        dob_0f_employee.send_keys("1990-03-13")
        time.sleep(6)
        
        waiter = WebDriverWait(driver,20)
        # Select gender of employee
        xpath_of_gender = "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']"
        gender_of_employee = waiter.until(EC.element_to_be_clickable((By.XPATH,xpath_of_gender)))
        gender_of_employee.click()
        time.sleep(6)

        # Select nationality of employee
        xpath_of_nationality = "(//div[@class='oxd-select-text-input'])[1]"
        nationality = driver.find_element(By.XPATH,xpath_of_nationality)
        nationality.send_keys("American")
        sel_american=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='American']")))
        sel_american.click()
        time.sleep(5)

                                 
        #Select marital status of employee
        xpath_of_marital_status = "(//div[@class='oxd-select-text-input'])[2]"
        marital_status = driver.find_element(By.XPATH,xpath_of_marital_status)
        marital_status.send_keys("Single")
        sel_single=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='Single']")))
        sel_single.click()
        time.sleep(5)

        # Saving the updates in employee details
        xpath_for_save_button1 = "(//button[@type='submit'])[1]"
        save_button1 = driver.find_element(By.XPATH,xpath_for_save_button1)
        save_button1.click()
        time.sleep(6)

        # Add Blood group of employee
        xpath_of_blood_group = "(//div[@class='oxd-select-text-input'])[3]"
        blood_group = driver.find_element(By.XPATH,xpath_of_blood_group)
        blood_group.send_keys("A+")
        sel_group=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='A+']")))
        sel_group.click()
        time.sleep(6)

        # Again Saving the updates in employee details
        xpath_for_save_button2 = "(//button[@type='submit'])[2]"
        save_button2 = driver.find_element(By.XPATH,xpath_for_save_button2)
        save_button2.click()
        time.sleep(5)
       


tc = orange_hrm()
tc.test()