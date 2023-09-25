from load_env import getEnvVirable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def login():
   
    name_field = driver.find_element(By.NAME, "user.login")
    password_field = driver.find_element(By.NAME, "user.senha")

    name_field.send_keys(getEnvVirable("USER_NAME"))
    password_field.send_keys(getEnvVirable("USER_PASSWORD"))

    driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()
    password_field.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 100)  
    wait.until(EC.presence_of_element_located((By.ID, "perfil-docente")))




def teste():

    dropdown = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/form/div/div[1]/table/tbody/tr[17]/td[2]"))

    dropdown.select_by_visible_text("Option Text")




if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://sigaa.unifei.edu.br/sigaa/verTelaLogin.do")

    login()
    teste()

    driver.quit()
