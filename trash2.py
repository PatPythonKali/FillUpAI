from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.maximize_window()
# location = "file://<Specify Path to Simple_Alert.HTML>"
location = "file://C:/Users/Automation-Dev/Desktop/Meenakshi/Selenium%20Python/Simple_Alert.HTML"
driver.get(location)

# Press the "Alert" button to demonstrate the Simple Alert
button = driver.find_element_by_name('alert')
button.click()

try:
    # Wait as long as required, or maximum of 10 sec for alert to appear
    WebDriverWait(driver, 10).until(cond.alert_is_present())

    # Change over the control to the Alert window
    obj = driver.switch_to.alert

    # Retrieve the message on the Alert window
    msg = obj.text
    print("Alert shows following message: " + msg)

    # Use the accept() method to accept the alert
    obj.accept()

except (NoAlertPresentException, TimeoutException) as py_ex:
    print("Alert not present")
    print(py_ex)
    print(py_ex.args)
finally:
    driver.quit()