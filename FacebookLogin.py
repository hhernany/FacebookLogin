from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print("Configurando acesso inseguro")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path="/Users/hugosc/Downloads/chromedriver", options=options)

print("Realizando login")
driver.get("https://www.facebook.com.br")
driver.find_element(By.ID, "email").send_keys("SEU_EMAIL")
password = driver.find_element(By.ID, "pass")
password.send_keys("SUA_SENHA")
password.send_keys(Keys.ENTER)

# print("Aguardando confirmação da autenticação de 2 fatores")
# time.sleep(40.0)
# print("Tempo de espera excedido. Seguindo com a execução.")

print("Realizando logout")
driver.find_element_by_css_selector("div[aria-label='Conta']").click()
time.sleep(3.0)
logoutButton = driver.find_element(By.XPATH('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]'))
#driver.find_element(By.XPATH("//span[text()='Sair']")).click()
webdriver.ActionChains(driver).move_to_element(logoutButton).click(logoutButton).perform()

print("Encerrando execução")
driver.quit()
