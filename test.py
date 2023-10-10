import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Start application by app.exe --remote-debugging-port=9515
app_path = "app.exe"


caps = webdriver.DesiredCapabilities.CHROME.copy() 
caps['acceptInsecureCerts'] = True
caps['platformName'] = "WINDOWS"

options = Options()
options.binary_location = app_path
options.add_argument("ignore-certificate-errors")
options.add_argument("remote-debugging-port=9515")
options.add_argument("start-maximized")

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Remote(command_executor="http://10.163.60.64:4444/wd/hub", options=options, desired_capabilities=caps)

try:
    # This works instead of driver.maximum_window()
    driver.execute_script('window.moveTo(0, 0);window.resizeTo(screen.width, screen.height);')
    time.sleep(10)
    print(driver.window_handles)
    # time.sleep(20)   # Wait for App ready

    # # Login
    driver.find_element_by_name("alias").send_keys("user_name")
    # # driver.find_element_by_name("password").send_keys("password")
    # # driver.find_element(By.XPATH, "//button[text()='SIGN IN']").click()
    # # time.sleep(2)
    # # driver.find_element(By.XPATH, "//button[text()='CONTINUE']").click()
    # # time.sleep(3)

    # driver.get("https://axoncar.local:8090/ui/index.html#/")
    # time.sleep(2)
    # driver.get("https://axoncar.local:8090/ui/index.html#/settings")
    # # Write your test logic here
    # # Example: Click a button
    # button_element = driver.find_element(By.XPATH, '//button[contains(., "ADD DEVICE")]')
    # button_element.click()
    # time.sleep(2)
    # button_element = driver.find_element(By.XPATH, '//button[contains(., "CLOSE")]')
    # button_element.click()

    # time.sleep(3)
    # driver.get("https://axoncar.local:8090/ui/index.html#/")
    # time.sleep(2)
    # button_element = driver.find_element(By.XPATH, '//button[contains(., "RECORD")]')
    # button_element.click()
    # time.sleep(5)
    # button_element = driver.find_element(By.XPATH, '//button[contains(., "STOP")]')
    # button_element.click()
    # time.sleep(3)
    
    # driver.get("https://axoncar.local:8090/ui/index.html#/review")
    # time.sleep(2)

    print("Test done!")

finally:
    # Clean up: Close the WebDriver and stop the Electron app
    driver.close()
    driver.quit()