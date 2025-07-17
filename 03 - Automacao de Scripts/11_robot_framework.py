"""
======================================================
FERRAMENTA: Robot Framework – Testes Automatizados e RPA
======================================================

O **Robot Framework** é um framework de automação de testes **baseado em palavras-chave (keyword-driven)**, usado principalmente para:
- Testes automatizados (web, APIs, desktop)
- Automação de processos (RPA)
- Integrações com bibliotecas externas (como Selenium, Appium, Database, etc.)

✅ É uma ferramenta de **alto nível**, ideal para equipes técnicas e não técnicas.

Instalação (via pip):
    pip install robotframework

Para uso com web (Selenium):
    pip install robotframework-seleniumlibrary

-----------------------------------------------
CARACTERÍSTICAS PRINCIPAIS:
-----------------------------------------------
- Sintaxe simples e legível (quase como linguagem natural)
- Modular e expansível com bibliotecas externas
- Suporte a logs e relatórios automáticos
- Suporte a testes de aceitação, BDD, e automação RPA

-----------------------------------------------
EXEMPLO BÁSICO: teste com Selenium
(Salvar como: exemplo_teste.robot)
-----------------------------------------------

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     https://www.google.com

*** Test Cases ***
Abrir o Google e Buscar Termo
    Open Browser    ${URL}    chrome
    Input Text      name=q    Robot Framework
    Press Keys      name=q    ENTER
    Sleep           2s
    Capture Page Screenshot
    Close Browser

"""

"""
-----------------------------------------------
COMO EXECUTAR UM TESTE:
-----------------------------------------------

1. Salve o script com extensão `.robot`
2. Execute no terminal com:
       robot exemplo_teste.robot

3. Relatórios automáticos gerados:
       - `log.html`
       - `report.html`
       - `output.xml`

-----------------------------------------------
OUTRAS BIBLIOTECAS POPULARES:
-----------------------------------------------
- SeleniumLibrary → automação web
- RPA Framework → automações estilo robôs
- DatabaseLibrary → automação com bancos de dados
- OperatingSystem → comandos do sistema
- RequestsLibrary → testes de API REST

-----------------------------------------------
DICAS:
-----------------------------------------------
- Use *** Keywords *** para criar palavras-chave personalizadas
- Pode ser integrado com CI/CD (ex: Jenkins)
- Ideal para automação de testes em times ágeis

Documentação oficial: https://robotframework.org/
Exemplos e tutoriais: https://robotframework.org/#resources
"""