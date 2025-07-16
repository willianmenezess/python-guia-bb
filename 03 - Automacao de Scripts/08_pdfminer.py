"""
======================================================
MÓDULO: pdfminer.six – Extração de Texto de Arquivos PDF
======================================================

O `pdfminer.six` é uma biblioteca Python especializada em **extrair texto, estrutura e metadados de arquivos PDF**.
É ideal para:
- Analisar conteúdo textual de PDFs (relatórios, boletos, faturas, artigos)
- Fazer scraping de documentos PDF com layout complexo
- Converter PDFs em texto estruturado (como HTML ou XML)

Instalação:
    pip install pdfminer.six

⚠️ É uma das poucas bibliotecas que consegue lidar com PDFs "reais" (textuais e com estrutura), diferente de ferramentas que só leem imagens.

-----------------------------------------------
FUNCIONALIDADES PRINCIPAIS:
-----------------------------------------------
- Extrair texto com precisão, respeitando layout e fontes
- Suporte a arquivos com múltiplas páginas
- Conversão para TXT, HTML, XML
- Acesso a estrutura do PDF: caixas de texto, posição dos caracteres etc.

-----------------------------------------------
EXEMPLO BÁSICO: extraindo texto de um PDF
-----------------------------------------------
"""

from pdfminer.high_level import extract_text

# Extrai texto de um PDF inteiro
texto = extract_text("documento_exemplo.pdf") # nao utilizou o with open pq extract_text já abre o arquivo internamente
print(texto)

"""
-----------------------------------------------
EXEMPLO COM VÁRIAS PÁGINAS E CONFIGURAÇÕES
-----------------------------------------------
"""

from pdfminer.high_level import extract_text_to_fp # Usado para extrair texto para um arquivo ou objeto em memória
from io import StringIO # Usado para capturar a saída e salvar em memória

output = StringIO()

with open("documento_exemplo.pdf", "rb") as pdf_file: # Abre o PDF em modo binário
    extract_text_to_fp(pdf_file, output)

texto_extraido = output.getvalue()
print(texto_extraido)

"""
-----------------------------------------------
DICAS:
-----------------------------------------------
- Use `extract_text()` para tarefas simples e rápidas.
- Para capturar posição e detalhes dos elementos (ex: tabelas), use a camada de layout com `pdfminer.layout`.
- Não funciona bem com PDFs escaneados (imagem). Use `OCR` (ex: Tesseract) nesse caso.
- Útil em conjunto com ferramentas como `re` (expressões regulares) para extrair campos específicos.

Documentação oficial: https://pdfminersix.readthedocs.io/
"""