"""
======================================================
MÓDULO: Splinter – Automação de Navegadores com Python
======================================================

O Splinter é uma biblioteca que serve como uma **camada de alto nível sobre o Selenium**.
Ela torna a automação de navegador mais **simples e legível**, ideal para testes ou web scraping controlado.

✅ Pode ser usada com drivers como:
- Chrome (via ChromeDriver)
- Firefox (via GeckoDriver)
- Safari, Edge ou até browser headless (como o `zope.testbrowser`)

Instalação:
    pip install splinter

⚠️ Assim como o Selenium, exige que o driver do navegador (ex: ChromeDriver) esteja disponível no sistema.

-----------------------------------------------
VANTAGENS DO SPLINTER:
-----------------------------------------------
- Código mais limpo e direto que Selenium puro
- Sintaxe mais parecida com linguagem natural
- Ótimo para automações rápidas e testes de interface

-----------------------------------------------
EXEMPLO BÁSICO:
-----------------------------------------------
"""

from splinter import Browser
import time

# 1. Iniciar o navegador (Chrome)
with Browser("chrome") as navegador:
    # 2. Acessar um site
    navegador.visit("https://www.google.com")

    # 3. Preencher o campo de pesquisa
    navegador.fill("q", "Python Splinter")

    # 4. Submeter o formulário (pressiona Enter)
    navegador.find_by_name("q").first.type("Python Splinter\n")

    # 5. Esperar alguns segundos (simulando tempo de leitura)
    time.sleep(3)

    # 6. Capturar um print da tela
    navegador.screenshot("pesquisa_google.png")

"""
DICAS:
- Use `find_by_name`, `find_by_id`, `find_by_text`, `find_by_tag`, `find_by_css`, `find_by_xpath`, etc.
- Use `.click()`, `.fill()`, `.type()`, `.is_visible()`, `.value`, entre outros métodos fáceis de usar.
- O Splinter pode ser executado em modo "headless" com o argumento `headless=True`.

Exemplo:
    with Browser("chrome", headless=True) as navegador:

Documentação oficial: https://splinter.readthedocs.io/
"""
