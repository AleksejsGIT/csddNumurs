import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver_path = "C:/Users/sepel/Documents/chromedriver.exe" # Norādīt, kur tika nolādēts chromedriver.exe
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 600) # Gaidīšanas laiks, lai lapai ielādētos 10min

def human_like_delay(minimum=2, maximum=5):
    time.sleep(random.uniform(minimum, maximum))

link_text = "Darbības ar transportlīdzekļiem"
link = driver.find_element(By.LINK_TEXT, link_text)
link.click()


next_link_text = "Izvēles numuri"
next_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, next_link_text)))
next_link.click()

text_to_enter = "NE420" # Ievadīt sava transportlīdzekļa numuru
input_field_id = "rn_find"
input_field = wait.until(EC.element_to_be_clickable((By.ID, input_field_id)))
input_field.send_keys(text_to_enter)

human_like_delay()
button_meklet = "RnFind"
find_button = wait.until(EC.element_to_be_clickable((By.ID, button_meklet)))
find_button.click()

human_like_delay()
button_accept = "confirmTl"
find_button = wait.until(EC.element_to_be_clickable((By.ID, button_accept)))
find_button.click()

human_like_delay()
button_choose = "chooseNrSeries"
find_button = wait.until(EC.element_to_be_clickable((By.ID, button_choose)))
find_button.click()

form_id = "uniforma_NZ106"  # ievadīt konkrētu numurzīmi, kuru pasūtīt
form = driver.find_element(By.ID, form_id)
submit_button = form.find_element(By.XPATH, ".//input[@type='submit']")
submit_button.click()

dropdown = Select(driver.find_element(By.ID, 'kac_select'))
dropdown.select_by_value("L") # Rīga, Bauskas iela

checkbox = driver.find_element(By.ID, "chkLaws")
checkbox.click()