"""
======================================================
MÓDULO: Pytest – Framework de Testes Automatizados em Python
======================================================

O `pytest` é um dos frameworks de testes mais populares e poderosos do ecossistema Python.
É utilizado para criar, organizar e executar **testes automatizados**, sendo ideal tanto para:
- Testes unitários
- Testes de integração
- Testes funcionais

Instalação:
    pip install pytest

Execução dos testes (a partir do terminal):
    pytest nome_do_arquivo.py
    # ou simplesmente: pytest (para rodar todos os testes do projeto)

-----------------------------------------------
VANTAGENS:
-----------------------------------------------
- Sintaxe simples (usando funções comuns com prefixo `test_`)
- Detecção automática de arquivos e funções de teste
- Suporte a fixtures (dados reutilizáveis nos testes)
- Excelente integração com plugins e ferramentas como coverage, tox, CI/CD etc.
- Relatórios de erros legíveis e detalhados

-----------------------------------------------
ESTRUTURA BÁSICA DE UM TESTE:
-----------------------------------------------
"""

# Arquivo: test_exemplo.py

def soma(a, b):
    return a + b

def test_soma_com_numeros_positivos():
    assert soma(2, 3) == 5

def test_soma_com_zero():
    assert soma(0, 5) == 5

def test_soma_com_negativos():
    assert soma(-1, -1) == -2

"""
-----------------------------------------------
USANDO FIXTURES (recursos reutilizáveis):
-----------------------------------------------
"""

import pytest

@pytest.fixture
def dados_de_teste():
    return {"a": 10, "b": 5}

def test_uso_fixture(dados_de_teste):
    resultado = soma(dados_de_teste["a"], dados_de_teste["b"])
    assert resultado == 15

"""
-----------------------------------------------
DICAS:
-----------------------------------------------
- Prefixos obrigatórios: arquivos `test_*.py` e funções `test_*`
- Use `assert` puro, sem necessidade de bibliotecas externas
- Plugins úteis: `pytest-cov`, `pytest-mock`, `pytest-xdist`
- Pode ser integrado a CI/CD (ex: GitHub Actions, GitLab CI, etc.)

Documentação oficial: https://docs.pytest.org/
"""
