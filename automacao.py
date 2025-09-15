from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configurações do WebDriver
options = webdriver.ChromeOptions()
download_dir = "C:/Users//boletos_facul"
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)

# Inicia o WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()


try:
    # Acessa o site da faculdade
    driver.get("") #link do ceub
    time.sleep(2)

    # Faz login
    usuario = driver.find_element(By.CSS_SELECTOR, "#coAcesso")
    senha = driver.find_element(By.CSS_SELECTOR, "#coSenha")
    usuario.send_keys("") #CPF
    senha.send_keys("") #SENHA
    senha.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navega até a seção de boletos
    driver.get("")  # link seção de boletos
    time.sleep(5)

    # Aguarda o carregamento da seção
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "resultadoMensalidadeEmAberto"))
    )
    time.sleep(10)
    # Usa ActionChains para clicar em uma posição específica na tela
    actions = ActionChains(driver)
    actions.move_by_offset(1060, 320).click().perform()
    time.sleep(10)
    # actions.move_by_offset(1200, 320).click().perform()

    # Aguarda um tempo para garantir que o clique foi processado
    time.sleep(15)

finally:
    # Fecha o navegador
    driver.quit()
    
    
