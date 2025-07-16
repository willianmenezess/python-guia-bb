"""
======================================================
MÓDULO: Selenium – Automação de Navegadores com Python
======================================================

O Selenium é uma biblioteca que permite automatizar ações em navegadores web.
É amplamente usada para:
- Testes automatizados de interface (front-end)
- Preenchimento automático de formulários
- Extração de dados (web scraping controlado)
- Simulação de comportamento real de usuários

Instalação:
    pip install selenium

⚠️ Também é necessário baixar o driver do navegador correspondente, como:
- Chrome → ChromeDriver
- Firefox → GeckoDriver

Baixe o driver compatível com a versão do seu navegador e coloque-o no PATH ou no mesmo diretório do script.

-----------------------------------------------
FUNCIONALIDADES PRINCIPAIS:
-----------------------------------------------
1. Abrir páginas da web automaticamente
2. Localizar e interagir com elementos da página (botões, inputs, links)
3. Preencher formulários e clicar em botões
4. Simular teclas, rolagens, uploads e downloads
5. Esperar elementos carregarem (esperas explícitas ou implícitas)

-----------------------------------------------
EXEMPLO BÁSICO:
-----------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Iniciar o navegador (Chrome, neste exemplo)
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver no PATH

# 2. Acessar uma página
driver.get("https://www.google.com")

# 3. Localizar a barra de pesquisa e pesquisar algo
caixa_pesquisa = driver.find_element(By.NAME, "q")
caixa_pesquisa.send_keys("Python Selenium")
caixa_pesquisa.send_keys(Keys.RETURN)

# 4. Esperar alguns segundos (não recomendado em produção — use WebDriverWait)
time.sleep(3)

# 5. Fechar o navegador
driver.quit()

"""
DICAS:
- Use WebDriverWait para aguardar elementos de forma segura.
- Use diferentes seletores: By.ID, By.NAME, By.CLASS_NAME, By.XPATH, etc.
- Para testes automatizados, combine com frameworks como pytest.

Documentação oficial: https://www.selenium.dev/documentation/webdriver/
"""
