# AutomatizaRegBot ⚙
Este script automatiza o registro de atendimentos feitos por um bot de conversa, cujos dados ficam armazenados em uma planilha (protocolo, número e roteiro utilizado). O processo era feito manualmente no trabalho, o que era repetitivo e sujeito a erros.

A primeira versão foi feita com PyAutoGui, funcional, mas limitada (dependência de posição de mouse, tela ativa, etc.). Esta nova versão, feita com Selenium, garante uma automação robusta, confiável e portável entre colaboradores.

## Funcionalidades 🔎

- Registro automatizado completo via navegador
- Uso de WebDriverWait para carregamento dinâmico sem necessidade de sempre utilizar sleep()
- Preenchimento de formulários com ActionChains
- Lógica condicional para classificar atendimento como "Chat Abandonado" ou "Informação Completa"
- Verificação de sucesso no envio com tentativas automáticas (até 10)
- Execução em loop com número de iterações definido pelo usuário
- Reutilizável por qualquer colaborador via entrada de dados simples (login, senha, nome, planilha, etc.)

## Como funciona 📝

Pré-requisitos manuais:

- Filtrar a planilha original, mantendo apenas dados essenciais.

- Julgar manualmente os roteiros mais adequados para cada entrada e gerar uma nova planilha.

- Entrada de dados pelo usuário:

- Login, senha e nome completo (vinculados ao registro).

- Links da planilha já filtrada e do sistema de registro (não fornecido por razões éticas e de segurança interna).

Execução automatizada:

- Abre as abas necessárias (CitSmart, planilha, registro).

- Percorre e interage com os elementos da interface web usando Selenium.

- Preenche campos, insere dados da planilha, seleciona opções, e submete o formulário.

- Em caso de erro, realiza até 10 novas tentativas antes de encerrar com erro.

## Tecnologias Utilizadas 💻
- Python 3.10.5
- Selenium 4.34.0

## Requisitos 📦

Python: [Download oficial](https://www.python.org/downloads/)

Selenium: instale via pip, pelo windows é o comando: `py -m pip install selenium`

[Página oficial](https://selenium-python.readthedocs.io/installation.html), onde também consta a documentação.

## Executando ▶️

Com o Python e Selenium instalados:

Basta apenas baixar o arquivo .py e executar.

