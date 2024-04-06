# from update_contact import update_contact
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup

# def fill_out_form(firstName, lastName, mailingStreet, mailingCity, mailingPostalCode, contactId):
#     try:
#         print("Starting form filling process...")
#         # Initialize Chrome options
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=options)
#         print(contactId)
#         print("Navigating to the Real Comp website...")
#         # Navigate to the Real Comp Website
#         driver.get("https://infosearch.real-comp.com/ash/faces/protected/databaseSelect.jsp")

#         print("Finding username and password input fields...")
#         # Find username and password input fields
#         username_input = driver.find_element(By.NAME, "j_username")
#         password_input = driver.find_element(By.NAME, "j_password")

#         print("Inputting username and password...")
#         # Input username and password
#         username_input.send_keys("TGSInsurance")
#         password_input.send_keys("Pytxo$1003295")

#         print("Submitting the form...")
#         # Submit the form
#         password_input.submit()

#         print("Waiting for image to be clickable...")
#         # Wait for the image to be clickable
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")))

#         print("Clicking on the image...")
#         # Find and click on the image using the provided XPath
#         image = driver.find_element(By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")
#         image.click()

#         house_number_input = driver.find_element(By.ID, "form:houseNumber")
#         street_name_input = driver.find_element(By.ID, "form:streetName")

#         # Extract house number and street name from mailingStreet
#         mailing_street = mailingStreet
#         if mailingStreet is not None:
#             street_components = mailing_street.split(' ')
#             house_number = street_components[0]
#             street_name = ' '.join(street_components[1:-1])

#         print("Filling out house number and street name...")
#         # Input house number and street name
#         house_number_input.send_keys(house_number)
#         street_name_input.send_keys(street_name)
        
#         print("Clicking on the search button...")
#         # Find and click on the search button
#         search_button = driver.find_element(By.NAME, "form:j_id_id133")
#         search_button.click()
#         time.sleep(5)

#         # Get the HTML content of the table
#         table_html = driver.find_element(By.ID, "form:table").get_attribute('outerHTML')

#         # Target last name and first name to search for
#         target_last_name = lastName
#         target_first_name = firstName

#         # Get the driver's license number associated with the target name
#         dl_number = get_dl_number_by_name(table_html, target_last_name, target_first_name)

#         if dl_number:
#             print(f"Driver's License Number for {target_first_name} {target_last_name}: {dl_number}")
#             update_contact(dl_number, contactId)
#         else:
#             print(f"No matching record found for {target_first_name} {target_last_name}")

#     except Exception as e:
#         print("An error occurred:", e)
#     finally:
#         # Close the browser window
#         driver.quit()

# def get_dl_number_by_name(table_html, target_last_name, target_first_name):
#     try:
#         # Parse the HTML table using BeautifulSoup
#         soup = BeautifulSoup(table_html, 'html.parser')

#         # Find all table rows
#         rows = soup.find_all('tr')

#         # Iterate through each row (skipping the header row)
#         for row in rows[1:]:
#             # Extract data from each column in the row
#             columns = row.find_all('td')
            
#             # Extract last name, first name, and driver's license number
#             last_name = columns[2].get_text()
#             first_name = columns[3].get_text()
#             dl_number = columns[0].get_text()

#             # Check if the current row matches the target name
#             if last_name.lower() == target_last_name.lower() and first_name.lower() == target_first_name.lower():
#                 # Return the driver's license number if a match is found
#                 return dl_number

#         # Return None if no match is found
#         return None
#     except Exception as e:
#         print("An error occurred")



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from bs4 import BeautifulSoup
from update_contact import update_contact
from selenium.webdriver.chrome.options import Options

def fill_out_form(firstName, lastName, mailingStreet, mailingCity, mailingPostalCode, contactId):
    try:
        print("Starting form filling process...")
        options = Options()
        options.headless = True
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        print(contactId)
        print("Navigating to the Real Comp website...")
        driver.get("https://infosearch.real-comp.com/ash/faces/protected/databaseSelect.jsp")

        print("Finding username and password input fields...")
        username_input = driver.find_element(By.NAME, "j_username")
        password_input = driver.find_element(By.NAME, "j_password")

        print("Inputting username and password...")
        username_input.send_keys("TGSInsurance")
        password_input.send_keys("Pytxo$1003295")

        print("Submitting the form...")
        password_input.submit()

        print("Waiting for image to be clickable...")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")))

        print("Clicking on the image...")
        image = driver.find_element(By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")
        image.click()

        house_number_input = driver.find_element(By.ID, "form:houseNumber")
        street_name_input = driver.find_element(By.ID, "form:streetName")

        mailing_street = mailingStreet
        if mailingStreet is not None:
            street_components = mailing_street.split(' ')
            house_number = street_components[0]
            street_name = ' '.join(street_components[1:-1])

        print("Filling out house number and street name...")
        house_number_input.send_keys(house_number)
        street_name_input.send_keys(street_name)
        
        print("Clicking on the search button...")
        search_button = driver.find_element(By.NAME, "form:j_id_id133")
        search_button.click()
        
        # Wait for the table to be visible
        try:
            table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "form:table")))
            table_html = table.get_attribute('outerHTML')
            
            # Now proceed with parsing the table HTML and extracting the driver's license number
            target_last_name = lastName
            target_first_name = firstName
            dl_number = get_dl_number_by_name(table_html, target_last_name, target_first_name)
    
            if dl_number:
                print(f"Driver's License Number for {target_first_name} {target_last_name}: {dl_number}")
                update_contact(dl_number, contactId)
            else:
                print(f"No matching record found for {target_first_name} {target_last_name}")
        
        except TimeoutException:
            print("Timed out waiting for table to load.")
            
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

def get_dl_number_by_name(table_html, target_last_name, target_first_name):
    try:
        soup = BeautifulSoup(table_html, 'html.parser')
        rows = soup.find_all('tr')

        for row in rows[1:]:
            columns = row.find_all('td')
            last_name = columns[2].get_text()
            first_name = columns[3].get_text()
            dl_number = columns[0].get_text()

            if last_name.lower() == target_last_name.lower() and first_name.lower() == target_first_name.lower():
                return dl_number

        return None
    except Exception as e:
        print("An error occurred")

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from update_contact import update_contact

# def fill_out_form(firstName, lastName, mailingStreet, mailingCity, mailingPostalCode, contactId):
#     try:
#         print("Starting form filling process...")
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=options)
        
#         print("Navigating to the Real Comp website...")
#         driver.get("https://infosearch.real-comp.com/ash/faces/protected/databaseSelect.jsp")

#         print("Finding username and password input fields...")
#         username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_username")))
#         password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_password")))

#         print("Inputting username and password...")
#         username_input.send_keys("TGSInsurance")
#         password_input.send_keys("Pytxo$1003295")

#         print("Submitting the form...")
#         password_input.submit()

#         print("Waiting for image to be clickable...")
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")))

#         print("Clicking on the image...")
#         image = driver.find_element(By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")
#         image.click()

#         house_number_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "form:houseNumber")))
#         street_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "form:streetName")))

#         mailing_street = mailingStreet
#         if mailingStreet is not None:
#             street_components = mailing_street.split(' ')
#             house_number = street_components[0]
#             street_name = ' '.join(street_components[1:-1])

#         print("Filling out house number and street name...")
#         house_number_input.send_keys(house_number)
#         street_name_input.send_keys(street_name)
        
#         print("Clicking on the search button...")
#         search_button = driver.find_element(By.NAME, "form:j_id_id133")
#         search_button.click()
        
#         # Wait for the table to be visible
#         try:
#             table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "form:table")))
#             table_html = table.get_attribute('outerHTML')
            
#             # Now proceed with parsing the table HTML and extracting the driver's license number
#             target_last_name = lastName
#             target_first_name = firstName
#             dl_number = get_dl_number_by_name(table_html, target_last_name, target_first_name)
    
#             if dl_number:
#                 print(f"Driver's License Number for {target_first_name} {target_last_name}: {dl_number}")
#                 update_contact(dl_number, contactId)
#             else:
#                 print(f"No matching record found for {target_first_name} {target_last_name}")
        
#         except TimeoutException:
#             print("Timed out waiting for table to load.")
            
#     except NoSuchElementException as e:
#         print(f"Element not found: {e}")
#     except TimeoutException:
#         print("Timed out waiting for element.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         if driver:
#             driver.quit()

# def get_dl_number_by_name(table_html, target_last_name, target_first_name):
#     try:
#         soup = BeautifulSoup(table_html, 'html.parser')
#         rows = soup.find_all('tr')

#         for row in rows[1:]:
#             columns = row.find_all('td')
#             last_name = columns[2].get_text()
#             first_name = columns[3].get_text()
#             dl_number = columns[0].get_text()

#             if last_name.lower() == target_last_name.lower() and first_name.lower() == target_first_name.lower():
#                 return dl_number

#         return None
#     except Exception as e:
#         print("An error occurred")
