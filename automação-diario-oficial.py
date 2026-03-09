import os
import time
import pyautogui
import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def diario (pesquisa):
    navegador = webdriver.Chrome()
    navegador.get("https://doweb.rio.rj.gov.br/")
    navegador.maximize_window()
    espera = WebDriverWait(navegador, 5)
    botao = espera.until(EC.element_to_be_clickable((By.ID, "baixar-diario-completo")))
    botao.click()
    pyautogui.PAUSE = 3
    pyautogui.press('alt')
    pyautogui.press('enter')
    pyautogui.press('down', presses= 6)
    pyautogui.press('enter')
    pyautogui.press('tab', presses= 2)
    pyautogui.press('enter')
    pyautogui.press('alt')
    pyautogui.press('enter')
    pyautogui.press('up', presses= 6)
    pyautogui.press('enter', presses= 2)
    pyautogui.write(pesquisa)
def trabalho():
    try:
        diario('eduardo Pereira de azevedo')
        pyautogui.PAUSE = 4
        pyautogui.press('prtsc')
        os.system('start whatsapp://')
        time.sleep(7)
        pyautogui.click(x=191, y=122)
        pyautogui.write('agenda')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    except Exception as e:
        print(f'Erro na primeira busca: {e}')

    try:
        diario('Edital SME')
        pyautogui.PAUSE = 3
        time.sleep(4)
        pyautogui.press('prtsc')
        os.system('start whatsapp://')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.hotkey('alt', 'f4')
        os.system("taskkill /F /IM chrome.exe")


    except Exception as e:
        print(f'Erro na segunda busca: {e}')
schedule.every().day.at("08:14").do(trabalho)
while True:
    schedule.run_pending()
    time.sleep(1)
