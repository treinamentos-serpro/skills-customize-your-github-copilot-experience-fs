# 📘 Assignment: Python Text Processing

## 🎯 Objective

Aprenda a trabalhar com strings e arquivos de texto em Python. Você irá limpar texto, extrair informações e gerar um relatório com resultados mensuráveis.

## 📝 Tasks

### 🛠️ Clean and Normalize Text

#### Descrição
Complete as funções iniciais para transformar um texto em uma forma consistente antes de analisá-lo.

#### Requisitos

- Implementar `normalize_text(text)` no arquivo `starter-code.py`
- Remover espaços extras no início e no fim do texto
- Converter o texto para letras minúsculas
- Substituir sequências de espaços, tabs e quebras de linha por um único espaço
- Fazer `normalize_text("  Hello   WORLD  ")` retornar `"hello world"`

### 🛠️ Analyze String Content

#### Descrição
Crie funções que contem palavras e caracteres e encontrem as palavras mais frequentes em um texto normalizado.

#### Requisitos

- Implementar `count_words(text)` para retornar o número de palavras
- Implementar `count_characters(text)` para contar caracteres sem incluir espaços
- Implementar `most_common_words(text, limit)` para retornar uma lista de tuplas `(palavra, frequência)`
- Tratar pontuação de forma que `"Python,"` e `"Python"` sejam contadas como a mesma palavra
- Ordenar as palavras mais frequentes por frequência decrescente e, em caso de empate, em ordem alfabética

### 🛠️ Read and Write a Text Report

#### Descrição
Use file I/O para ler um arquivo de entrada e salvar um relatório de análise em outro arquivo. O relatório deve ser útil para alguém que não viu o código.

#### Requisitos

- Implementar `analyze_file(input_path, output_path)`
- Abrir o arquivo de entrada usando `with open(..., encoding="utf-8")`
- Analisar todo o conteúdo com as funções das tarefas anteriores
- Gravar no arquivo de saída o total de palavras, o total de caracteres sem espaços e as cinco palavras mais frequentes
- Usar `FileNotFoundError` para informar claramente quando o arquivo de entrada não existir
- Executar o programa pela linha de comando com `python starter-code.py input.txt report.txt`