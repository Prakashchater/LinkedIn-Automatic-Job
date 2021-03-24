from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
PHONE = "YOUR PHONE NUMBER"
webdriver_path = "YOUR PATH FILE"
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
email = "YOUR LINKEDIN EMAIL ID"
password1 = "YOUR PASSWORD"
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url)

time.sleep(5)
sign_up = driver.find_element_by_link_text("Sign in")
sign_up.click()

#time.sleep() will wait for the page to load
time.sleep(5)
login = driver.find_element_by_id("username")
login.send_keys(email)
password = driver.find_element_by_id("password")
password.send_keys(password1)
password.send_keys(Keys.ENTER)

time.sleep(5)

all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in all_jobs:
    print("calling")
    job.click()
    time.sleep(5)

    try:
        apply = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply.click()
        time.sleep(5)

        # phone = driver.find_element_by_class_name(".fb-single-line-text__input")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")


        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(3)
            discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Application Skipped.")
            continue
        else:
            submit_button.click()


        time.sleep(5)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No Application button, skipped.")
        continue

time.sleep(5)
driver.quit()


