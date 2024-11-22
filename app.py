import pyautogui

#### Desafio criar uma nova pasta ####

# Movendo o cursor na tela
pyautogui.moveTo(x=1456, y=585, duration=2) 

# clicar com o botão Direito
pyautogui.click(button='right')

# mover o mouse até "NOVO"
pyautogui.move(50,-160, duration=1)

# clicar com o botão Esquerdo
pyautogui.click(button='left')

# Mover o cursor até "PASTA"
pyautogui.move(-90,0, duration=1)

# clicar com o botão Esquerdo para criar a pasta
pyautogui.click(button='left')