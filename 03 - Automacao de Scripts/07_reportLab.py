"""
======================================================
MÓDULO: ReportLab – Geração de Arquivos PDF com Python
======================================================

O `ReportLab` é uma biblioteca poderosa para **criação dinâmica de documentos PDF**.
É amplamente usada em sistemas que precisam gerar relatórios, boletos, certificados,
faturas e outros documentos formatados diretamente via código.

Instalação:
    pip install reportlab

-----------------------------------------------
FUNCIONALIDADES PRINCIPAIS:
-----------------------------------------------
- Criação de PDFs via código (texto, tabelas, imagens, gráficos)
- Controle total sobre layout: posição, fonte, cor, estilo, tamanho
- Suporte a parágrafos, páginas múltiplas e quebras de linha
- Geração de PDFs a partir de templates ou programaticamente

-----------------------------------------------
EXEMPLO BÁSICO:
-----------------------------------------------
"""

from reportlab.pdfgen import canvas

# 1. Cria o canvas (documento PDF)
pdf = canvas.Canvas("exemplo.pdf")

# 2. Escreve texto nas coordenadas (x, y)
pdf.drawString(100, 750, "Olá, este é um PDF gerado com ReportLab!")

# 3. Adiciona uma linha, retângulo e círculo (opcional)
pdf.line(100, 740, 400, 740)
pdf.rect(100, 700, 200, 30)
pdf.circle(300, 600, 40)

# 4. Salva o arquivo
pdf.save()

"""
-----------------------------------------------
EXEMPLO COM PARÁGRAFOS E TABELAS (modo avançado):
-----------------------------------------------
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Define documento
doc = SimpleDocTemplate("relatorio.pdf", pagesize=A4)
estilos = getSampleStyleSheet()
conteudo = []

# Adiciona um parágrafo
conteudo.append(Paragraph("Relatório de Exemplo", estilos["Title"]))
conteudo.append(Spacer(1, 20))

# Adiciona uma tabela
dados = [["Nome", "Idade"], ["Ana", 28], ["João", 32]]
tabela = Table(dados)
conteudo.append(tabela)

# Gera o PDF
doc.build(conteudo)

"""
-----------------------------------------------
DICAS:
-----------------------------------------------
- Sistema de coordenadas (0, 0) fica no canto inferior esquerdo da página
- Use `platypus` para documentos mais estruturados (textos, tabelas, fluxos)
- ReportLab é excelente para gerar PDFs a partir de sistemas backend

Documentação oficial: https://www.reportlab.com/documentation/
"""
