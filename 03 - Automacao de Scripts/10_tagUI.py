"""
======================================================
MÓDULO: TagUI – Automação RPA com Python Simples e Intuitiva
======================================================

O `TagUI` é uma ferramenta de **automação RPA (Robotic Process Automation)** de código aberto, criada pela AI Singapore.
Ele permite automatizar tarefas repetitivas em websites, sistemas desktop, arquivos e muito mais.

⚙️ Com o módulo `tagui` do Python, é possível usar comandos TagUI diretamente com scripts Python.

Instalação do módulo Python:
    pip install tagui

Primeira execução (apenas uma vez, baixa o mecanismo TagUI):
    import tagui as t
    t.init()

-----------------------------------------------
VANTAGENS DO TAGUI:
-----------------------------------------------
- Sintaxe super simples e legível
- Pode interagir com sites, PDFs, Excel, telas do computador
- Não requer conhecimentos profundos de programação
- Compatível com Windows, Linux e macOS
- Ideal para tarefas de RPA sem ferramentas pagas

-----------------------------------------------
EXEMPLO BÁSICO DE AUTOMATIZAÇÃO WEB
-----------------------------------------------
"""

import tagui as t

t.init()
t.url('https://www.google.com')
t.type('q', 'automação com tagui[enter]')
t.snap('page', 'resultado.png')  # tira print da página
t.close()

"""
-----------------------------------------------
OUTROS COMANDOS ÚTEIS:
-----------------------------------------------
t.click('Texto ou seletor')          → clicar em botão/elemento
t.type('campo', 'valor')             → digitar em campo
t.read('seletor ou posição')         → ler conteúdo da tela
t.wait(2.5)                          → esperar X segundos
t.hover('elemento')                 → passar o mouse

-----------------------------------------------
DICAS:
-----------------------------------------------
- O TagUI pode usar **OCR (leitura de texto na tela)** e **visão computacional** para encontrar elementos
- Pode interagir com arquivos PDF, Excel, navegadores e até comandos de terminal
- Ideal para automações simples de sistemas legados ou sem API

Documentação oficial: https://tagui.readthedocs.io/en/latest/
GitHub do projeto: https://github.com/tebelorg/tagui
"""
