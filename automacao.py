import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3  # Pausa entre iterações

# Passo 1: entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrar no site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3) # Delay de segurança

# Passo 2: Fazer o login

# Seleciona o campo de e-mail
pyautogui.click(x=717, y=404)
# Escreve e-mail e senha
pyautogui.write('emaildelogin@email.com')
pyautogui.press('tab') # Passa para próxima linha
pyautogui.write('senhadousuario')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: Importar base de dados e cadastrar item

tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.click(x=698, y=292)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, "obs"])
    if obs != 'nan':
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000)