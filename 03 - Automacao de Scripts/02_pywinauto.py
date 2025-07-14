"""
=====================================================
MÓDULO: Pywinauto – Automação de Aplicações Windows
=====================================================

O Pywinauto é uma biblioteca Python usada para automatizar aplicações nativas do Windows.
Ideal para:
- Automatizar interações com janelas, caixas de diálogo, menus e botões
- Preencher campos em aplicativos como Bloco de Notas, Calculadora, Word, etc.
- Automatizar testes de GUI (interface gráfica)

Instalação:
    pip install pywinauto

⚠️ Funciona apenas no Windows (não compatível com Linux/Mac)

-----------------------------------------------
PRINCIPAIS FUNCIONALIDADES:
-----------------------------------------------
1. Abrir e controlar janelas de programas
2. Clicar em botões, digitar em campos e interagir com menus
3. Acessar elementos por nome, ID, classe ou título
4. Automatizar testes e tarefas repetitivas em aplicativos legados

-----------------------------------------------
EXEMPLOS BÁSICOS:
-----------------------------------------------
"""

from pywinauto import Application
import time

# 1. Iniciar um aplicativo (ex: Bloco de Notas)
app = Application().start("notepad.exe")

# 2. Acessar a janela principal
janela = app.window(title_re=".*Notepad")

# 3. Escrever no Bloco de Notas
janela.type_keys("Olá, mundo! Automação com pywinauto.", with_spaces=True)

# 4. Acessar menus (ex: Arquivo > Salvar Como)
janela.menu_select("File->Save As")

# 5. Esperar e preencher nome do arquivo
time.sleep(1)
salvar_janela = app.window(title_re=".*Save As")
salvar_janela["Edit"].type_keys("arquivo_automacao.txt", with_spaces=True)
salvar_janela["Save"].click()

# 6. Fechar o aplicativo
janela.close()
# Tratar o popup "Salvar?" se aparecer
app.window(title_re=".*Notepad").window(auto_id="CommandButton_7").click()  # Botão "Don't Save"

"""
DICAS:
- Use app.connect() para se conectar a janelas já abertas
- Use print(janela.print_control_identifiers()) para descobrir os controles acessíveis
- É útil para automatizar programas que não têm API ou interface web

Documentação oficial: https://pywinauto.readthedocs.io/en/latest/
"""