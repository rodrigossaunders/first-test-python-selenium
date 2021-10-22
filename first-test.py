import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://docket-test.herokuapp.com/register")
driver.maximize_window()


driver.find_element(By.NAME,"username").send_keys("Ryanxsss")
driver.find_element(By.NAME,"email").send_keys("testxsss@email.com")
driver.find_element(By.NAME,"password").send_keys("12345")
driver.find_element(By.NAME,"password2").send_keys("12345" + Keys.ENTER)

current_url = driver.current_url
assert current_url == "https://docket-test.herokuapp.com/login"

message = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]").text
assert message == "Congratulations, you are now registered"


driver.quit()