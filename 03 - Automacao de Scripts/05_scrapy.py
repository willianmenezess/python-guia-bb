"""
======================================================
MÓDULO: Scrapy – Framework de Web Scraping com Python
======================================================

O Scrapy é um **framework poderoso e rápido para extração de dados (web scraping)**
usado para coletar, estruturar e armazenar informações de páginas web.

É ideal para:
- Coletar grandes volumes de dados da web de forma estruturada
- Navegar entre links e extrair dados de múltiplas páginas
- Projetos profissionais de coleta de dados, como crawlers

Instalação:
    pip install scrapy

Para iniciar um projeto:
    scrapy startproject nome_do_projeto

-----------------------------------------------
VANTAGENS:
-----------------------------------------------
- Estrutura profissional com organização em spiders, itens e pipelines
- Suporte a middlewares, filtros de resposta e múltiplas requisições simultâneas
- Permite exportar dados para JSON, CSV, XML etc.
- Otimizado para performance e reuso de código

-----------------------------------------------
EXEMPLO BÁSICO DE SPIDER:
-----------------------------------------------
"""

# Após criar o projeto com `scrapy startproject`, crie um arquivo Spider:

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # Nome da spider, vai servir para rodar o crawler

    start_urls = ["http://quotes.toscrape.com"] # URL inicial para começar a coleta

    def parse(self, response): # Método chamado para processar a resposta da URL inicial
        for frase in response.css("div.quote"):
            yield {
                "texto": frase.css("span.text::text").get(),
                "autor": frase.css("small.author::text").get(),
                "tags": frase.css("div.tags a.tag::text").getall(),
            }

        # Segue para a próxima página (se existir)
        proxima_pagina = response.css("li.next a::attr(href)").get()
        if proxima_pagina:
            yield response.follow(proxima_pagina, callback=self.parse)

"""
COMANDOS ÚTEIS:
-----------------------------------------------
- Criar projeto: scrapy startproject nome_projeto
- Rodar spider: scrapy crawl quotes
- Exportar dados: scrapy crawl quotes -o dados.json
- Testar seletor CSS/XPath: scrapy shell "URL"

DICAS:
- Use o scrapy shell para testar seletores CSS/XPath antes de implementar.
- Crie pipelines para processar e salvar os dados (limpeza, banco de dados etc.).
- Scrapy ignora domínios externos por padrão, mas isso pode ser alterado.
- Use logs e configurações no settings.py para personalizar o comportamento do crawler.

Documentação oficial: https://docs.scrapy.org/
"""