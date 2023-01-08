import pyautogui
import pyperclip
import time
import pandas as pd
pyautogui.PAUSE = 1.3
pyautogui.press('win')
pyautogui.write('Opera')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(3)
pyautogui.doubleClick(x=385, y=269)
time.sleep(2)
pyautogui.rightClick(x=385, y=269)
pyautogui.click(x=502, y=635)

tabela = pd.read_excel(r'C:\Users\lucas\Downloads\Vendas - Dez.xlsx')
print(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print('a quantidade de produtos vendidos é {}'.format(quantidade))
print('faturamento das vendas é de {}'.format(faturamento))



time.sleep(5)
p = pyautogui.position()
print(p)

