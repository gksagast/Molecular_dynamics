from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import easygui
import os
import time
from bs4 import BeautifulSoup


#input_filepath = easygui.fileopenbox("Select the input .mol2 file")
#output_filepath = easygui.fileopenbox("Where to save?")
input_filepath = 
output_filepath = 
base_name = os.path.splitext(os.path.basename(input_filepath))[0]  
print(base_name)
search_name = base_name + ".str"
print(search_name)

#if input_filepath is None:
#   sys.exit("No input file selected. Exiting.")

# Initialize the Chrome driver (you can use Firefox or others too)
driver = webdriver.Chrome()

# Open the website
driver.get('https://cgenff.silcsbio.com/initguess/')

#input user login
usr = 
pwd = 


#wait for presence of username
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'usrName'))
)
#time.sleep(5)  # pauses the execution for 5 seconds

#wait for presence of pwd
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'curPwd'))
)

#input login info
username.send_keys(usr)
#time.sleep(5)  # pauses the execution for 5 seconds

password.send_keys(pwd)
#time.sleep(5)  # pauses the execution for 5 seconds

login_button = driver.find_element(By.NAME, 'submitBtn')  # Replace 'login_button' with the actual ID or other locator
login_button.click()
#time.sleep(5)  # pauses the execution for 5 seconds


# Assuming the input field has an id 'file_upload', you can directly send the file path to it
file_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'filename'))
)
file_input = driver.find_element(By.NAME, 'filename')
file_input.send_keys(input_filepath)

# Now, click the 'Upload File' button (assuming its id is 'upload_button')
upload_button = driver.find_element(By.CLASS_NAME, 'uploadbtn1')
upload_button.click()

# Wait for a link where the title contains the substring "SheI5"
link_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//a[@title='{search_name}']"))
)
link_element.click()
new_window_handle = driver.window_handles[-1]  # Usually the new tab will be the last in the list
driver.switch_to.window(new_window_handle)


time.sleep(3)
#Get the entire HTML of the page
html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')

# Extracting text from the <pre> tag
text = soup.pre.get_text()

# Define the path to save the .mol2 file
#out_path = os.path.join(output_filepath, f"{base_name}.mol2")
out_path = os.path.join(output_filepath, f"NAMEHERE.str")

# Write the HTML content to the .mol2 file
with open(out_path, "w") as file:
    file.write(text)
