"""
=====================================================
MÓDULO: PyAutoGUI – Automação de Tarefas com o Mouse e Teclado
=====================================================

O PyAutoGUI é uma biblioteca Python usada para automação de tarefas
que envolvem controle do mouse, teclado e telas. Ideal para:
- Automatizar cliques e digitação
- Preencher formulários
- Capturar a tela (screenshots)
- Testes automatizados em interfaces gráficas

Instalação:
    pip install pyautogui

-----------------------------------------------
PRINCIPAIS FUNCIONALIDADES:
-----------------------------------------------

1. Movimentação e clique do mouse
2. Digitação automática
3. Captura de tela e reconhecimento de imagem
4. Comandos de teclado (atalhos, teclas especiais)
5. Mensagens de alerta ou confirmação (popup)

-----------------------------------------------
EXEMPLOS BÁSICOS:
-----------------------------------------------
"""

import pyautogui
import time

# Espera de segurança para o usuário cancelar (Ctrl + C)
pyautogui.PAUSE = 1.0

# 1. Obter a posição atual do mouse
pos = pyautogui.position()
print(f"Posição atual do mouse: {pos}")

# 2. Mover o mouse para uma posição específica
pyautogui.moveTo(100, 200, duration=1)

# 3. Clicar com o mouse
pyautogui.click()  # Clique esquerdo onde o mouse estiver
pyautogui.rightClick()
pyautogui.doubleClick()

# 4. Digitar texto
pyautogui.write("Olá, mundo!", interval=0.1)
pyautogui.press("enter")

# 5. Usar combinações de teclas (atalhos)
pyautogui.hotkey("ctrl", "s")  # Ex: salvar arquivo

# 6. Capturar tela
screenshot = pyautogui.screenshot()
screenshot.save("tela.png")

# 7. Localizar imagem na tela
# (útil para encontrar botões ou ícones visuais)
# pyautogui.locateOnScreen('imagem_botao.png')

# 8. Mensagem de alerta (popup)
# pyautogui.alert("Automação concluída!")

"""
DICAS:
- Use time.sleep(x) para dar tempo entre ações
- Use pyautogui.FAILSAFE = True para interromper movendo o mouse para o canto superior esquerdo
- Evite automatizar ações perigosas sem testes!

Documentação: https://pyautogui.readthedocs.io
"""
