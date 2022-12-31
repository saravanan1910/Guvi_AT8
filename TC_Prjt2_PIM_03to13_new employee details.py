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
        3.In PIM module, Add new employee details 
        4.Fill the All details of employee and save it
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
        
# ADD NEW EMPLOYEE IN PIM MODULE (TC_PIM_03)
        # Select Add employee option
        xpath_of_add_employee = "//*[contains(text(),'Add')]"
        add_employee = driver.find_element(By.XPATH,xpath_of_add_employee)
        add_employee.click()
        time.sleep(5)
        

        # Add employee first name
        xpath_of_employee_first_name = "//input[@placeholder='First Name']"
        first_name = driver.find_element(By.XPATH,xpath_of_employee_first_name)
        first_name.send_keys("Rahul")
        time.sleep(5)
       

        # Add employee last name
        xpath_of_employee_last_name = "//input[@placeholder='Last Name']"
        last_name = driver.find_element(By.XPATH,xpath_of_employee_last_name)
        last_name.send_keys("Dravid")
        time.sleep(5)

        # Create Login Details
        xpath_of_login_deatils = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
        login_details = driver.find_element(By.XPATH,xpath_of_login_deatils)
        login_details.click()
        time.sleep(6)

        sel_status = driver.find_element(By.XPATH,"(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")
        sel_status.click()
        time.sleep(3)

        enter_user_name = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
        enter_user_name.send_keys("rahul")
        time.sleep(3)

        enter_password = driver.find_element(By.XPATH,"(//input[@type='password'])[1]")
        enter_password.send_keys("Rahul@123")
        time.sleep(5)

        confirm_password = driver.find_element(By.XPATH,"(//input[@type='password'])[2]")
        confirm_password.send_keys("Rahul@123")
        time.sleep(5)

       
        # Enter or Click save button
        xpath_of_save_button = "//button[@type='submit']"
        save_button = driver.find_element(By.XPATH,xpath_of_save_button)
        save_button.click()
        time.sleep(8)

        # Validate Tabs Present in Employee List Page (TC_PIM_04)

        em_details_list = driver.find_elements(By.XPATH,"//div[@class='orangehrm-tabs']//a")
        for i in em_details_list:
            print(i.text)
        time.sleep(5)

        waiter = WebDriverWait(driver,20)

        # Enter Personal Details of employee (TC_PIM_05)
        nick_name = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        nick_name.send_keys("Wall")
        time.sleep(6)

        dr_license_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]")
        dr_license_no.send_keys("191919")
        time.sleep(5)

        # li_expiry_date = driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[1]")
        # li_expiry_date.send_keys("2022-12-22")
        # time.sleep(6)

        ssn_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[6]")
        ssn_no.send_keys("123456654321")
        time.sleep(3)

        sin_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[7]")
        sin_no.send_keys("987654321")

        dob_0f_employee = driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]")
        dob_0f_employee.send_keys("1973-01-11")
        time.sleep(6)
                 
        xpath_of_gender = "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']"
        gender_of_employee = waiter.until(EC.element_to_be_clickable((By.XPATH,xpath_of_gender)))
        gender_of_employee.click()
        time.sleep(6)

        xpath_of_nationality = "(//div[@class='oxd-select-text-input'])[1]"
        nationality = driver.find_element(By.XPATH,xpath_of_nationality)
        nationality.send_keys("Indian")
        sel_indian=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='Indian']")))
        sel_indian.click()
        time.sleep(5)

                              
        xpath_of_marital_status = "(//div[@class='oxd-select-text-input'])[2]"
        marital_status = driver.find_element(By.XPATH,xpath_of_marital_status)
        marital_status.send_keys("Married")
        sel_single=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='Married']")))
        sel_single.click()
        time.sleep(5)

        military_service = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[10]")
        military_service.send_keys("Yes")
        time.sleep(5)

        save_button1 = driver.find_element(By.XPATH,"(//button[@type='submit'])[1]")
        save_button1.click()
        time.sleep(6)

       
        blood_group = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[3]")
        blood_group.send_keys("A+")
        sel_group=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='A+']")))
        sel_group.click()
        time.sleep(6)

        save_button2 = driver.find_element(By.XPATH,"(//button[@type='submit'])[2]")
        save_button2.click()
        time.sleep(5)
       
       # Enter Contact Details of employee (TC_PIM_06)

        contact_details = driver.find_element(By.XPATH,"(//a[@class='orangehrm-tabs-item'])[1]")
        contact_details.click()
        time.sleep(6)

        street1 = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        street1.send_keys("No.5")
        time.sleep(5)

        street2 = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
        street2.send_keys("Indira Nagar")
        time.sleep(3)

        city = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]")
        city.send_keys("Bangalore")
        time.sleep(3)

        state = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]")
        state.send_keys("Karnataka")
        time.sleep(3)

        pin_code = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[6]")
        pin_code.send_keys("560038")
        time.sleep(3)

        country = driver.find_element(By.XPATH,"//div[@class='oxd-select-text oxd-select-text--focus']")
        country.send_keys("India")
        sel_india=waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='option']//span[text()='India']")))
        sel_india.click()
        time.sleep(5)

        home_mob_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[7]")
        home_mob_no.send_keys("7896543210")
        time.sleep(5)

        mob_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[8]")
        mob_no.send_keys("7896873210")
        time.sleep(5)

        work_mob_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[9]")
        work_mob_no.send_keys("9896543567")
        time.sleep(5)

        work_email = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[10]")
        work_email.send_keys("rahul.icc@gmail.com")
        time.sleep(5)

        other_email = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[11]")
        other_email.send_keys("rahul.dravid@gmail.com")
        time.sleep(5)

        save_contact_details = driver.find_element(By.XPATH,"//button[@type='submit']")
        save_contact_details.click()
        time.sleep(5)

        # Emergency Contact Details of employee (TC_PIM_07)
        Em_contact_details = driver.find_element(By.XPATH,"//a[text()='Emergency Contacts']")
        Em_contact_details.click()
        time.sleep(6)

        add_em_contacts = driver.find_element(By.XPATH,"(//button[@type='button'])[2]")
        add_em_contacts.click()
        time.sleep(6)

        em_cont_name = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        em_cont_name.send_keys("Vijeta")
        time.sleep(5)

        relation_ship = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
        relation_ship.send_keys("Spouse")
        time.sleep(5)

        em_cont_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]")
        em_cont_no.send_keys("9876543218")
        time.sleep(5)

        save_em_contact_details = driver.find_element(By.XPATH,"//button[@type='submit']")
        save_em_contact_details.click()
        time.sleep(6)

        # Dependents details of employee (TC_PIM_08)
        dependents = driver.find_element(By.XPATH,"//a[@class='orangehrm-tabs-item --active']")
        dependents.click()
        time.sleep(6)

        add_dependents = driver.find_element(By.XPATH,"(//button[@type='button'])[2]")
        add_dependents.click()
        time.sleep(6)

        name_dependents = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        name_dependents.send_keys("Anvay Dravid")
        time.sleep(5)

        relation_dependents = driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']")
        relation_dependents.send_keys("Child")
        sel_child = waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Child']")))
        sel_child.click()
        time.sleep(5)

        dob_dependents = driver.find_element(By.XPATH,"//input[@placeholder = 'yyyy-mm-dd']")
        dob_dependents.send_keys("2009-10-11")

        save_dependents_details = driver.find_element(By.XPATH,"//button[@type='submit']")
        save_dependents_details.click()
        time.sleep(6)

        # Job Details of employee (TC_PIM_09)
        job = driver.find_element(By.XPATH,"//a[normalize-space()='Job']")
        job.click()
        time.sleep(6)

        joined_date = driver.find_element(By.XPATH,"//input[@placeholder='yyyy-mm-dd']")
        joined_date.send_keys("2009-10-22")
        time.sleep(5)

        job_title = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
        job_title.send_keys("Associate Engineer")
        sel_AE = waiter.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Associate Engineer']")))
        sel_AE.click()
        time.sleep(6)

        job_category = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")
        job_category.send_keys("Professionals")
        sel_pro = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Professionals']")))
        sel_pro.click()
        time.sleep(6)

        sub_unit = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[3]")
        sub_unit.send_keys("Engineering")
        sel_engg = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Engineering']")))
        sel_engg.click()
        time.sleep(6)

        location = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[4]")
        location.send_keys("Texas R&D")
        sel_texas = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Texas R&D']")))
        sel_texas.click()
        time.sleep(6)

        emply_status = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[5]")
        emply_status.send_keys("Full-Time Permanent")
        sel_full_time = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Full-Time Permanent']")))
        sel_full_time.click()
        time.sleep(6)

        em_contract_details = driver.find_element(By.XPATH,"//input[@type='checkbox']")
        em_contract_details.click()
        time.sleep(6)

        contract_start_date = driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]")
        contract_start_date.send_keys("2021-03-12")
        time.sleep(5)

        contract_end_date = driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[3]")
        contract_end_date.send_keys("2023-03-12")
        time.sleep(5)

        save_job_details = driver.find_element(By.XPATH,"//button[@type='submit']")
        save_job_details.click()
        time.sleep(5)

        # Employee Termination Details (TC_PIM_10)
        termination = driver.find_element(By.XPATH,"(//button[@type='button'])[2]")
        termination.click()
        time.sleep(6)

        termination_date = driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]")
        termination_date.send_keys("2023-03-13")
        time.sleep(5)

        termination_reason = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[6]")
        termination_reason.send_keys("Contract Not Renewed")
        sel_cont_not_renewed = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Contract Not Renewed']")))
        sel_cont_not_renewed.click()
        time.sleep(6)

        save_termination_details = driver.find_element(By.XPATH,"(//button[@type='submit'])[2]")
        save_termination_details.click()
        time.sleep(10)

        # Employee Activation Details (TC_PIM_11)
        activation = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--ghost-success --termination-button']")
        activation.click()
        time.sleep(10)

        # Employee Salary Details (TC_PIM_12)
        salary_details = driver.find_element(By.XPATH,"//a[@class='orangehrm-tabs-item --active']")
        salary_details.click()
        time.sleep(6)

        add_salary_comp = driver.find_element(By.XPATH,"(//button[@type='button'])[2]")
        add_salary_comp.click()
        time.sleep(6)

        salary_comp = driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']")
        salary_comp.send_keys("Gross Salary")
        time.sleep(5)

        pay_grade = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
        pay_grade.send_keys("Grade 1")
        sel_grade_1 = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Grade 1']")))
        sel_grade_1.click()
        time.sleep(5)

        pay_frequency = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")
        pay_frequency.send_keys("Monthly")
        sel_monthly = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Monthly']")))
        sel_monthly.click()
        time.sleep(5)

        currency = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[3]")
        currency.send_keys("Australian Dollar")
        sel_dollar = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Australian Dollar']")))
        sel_dollar.click()
        time.sleep(5)

        amount = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
        amount.send_keys("100000")
        time.sleep(5)

        direct_deposit = driver.find_element(By.XPATH,"//input[@type='checkbox']")
        direct_deposit.click()
        time.sleep(6)

        ac_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]")
        ac_no.send_keys("564653754")
        time.sleep(5)

        ac_type = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[4]")
        ac_type.send_keys("Savings")
        sel_savings = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Savings']")))
        sel_savings.click()
        time.sleep(5)

        route_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]")
        route_no.send_keys("765653754")
        time.sleep(5)

        sal_amount = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[6]")
        sal_amount.send_keys("90000")
        time.sleep(5)

        save_salary_details = driver.find_element(By.XPATH,"//button[@type='submit']")
        save_salary_details.click()
        time.sleep(10)

        # Employee Tax Exemptions Details (TC_PIM_13)
        tax_exmp_details = driver.find_element(By.XPATH,"//a[text()='Tax Exemptions']")
        tax_exmp_details.click()
        time.sleep(6)

        state_tax = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")
        state_tax.send_keys("Texas")
        sel_texas = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Texas']")))
        sel_texas.click()
        time.sleep(6)

        state_status = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[3]")
        state_status.send_keys("Married")
        sel_married = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Married']")))
        sel_married.click()
        time.sleep(6)

        exemption = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
        exemption.send_keys("90")
        time.sleep(5)

        work_state = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[5]")
        work_state.send_keys("Texas")
        sel_texas = waiter.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Texas']")))
        sel_texas.click()
        time.sleep(6)

        save_taxexmp_details = driver.find_element(By.XPATH,"//button[@type='submit']")
        save_taxexmp_details.click()
        time.sleep(10)





tc = orange_hrm()
tc.test()