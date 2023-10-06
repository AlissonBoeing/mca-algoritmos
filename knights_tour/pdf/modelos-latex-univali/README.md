[![GitHub license](https://img.shields.io/badge/license-CC0-blue.svg)](https://raw.githubusercontent.com/paulosell/modelos-latex-univali/master/LICENSE)

# Modelos de documentos em LaTeX para discentes

Modelos de documentos em LaTeX para docentes e discentes para uso no Programa de Mestrado em Computação Aplicada da Universidade do Vale do Itajaí. 

## Modelos para área acadêmica

- **Apresentação (slides)**
  - [Tema *Título Leve*](apresentacao/titulo-leve)
- **Lista de exercício ou Prova**
  - [Modelo que faz uso da classe exam](lista-ou-prova/exam)
- **Relatório**
  - [Modelo que faz uso da classe `article`](relatorio/article)
  - [Modelo de relatório para trabalhos de disciplina](relatorio/homework)
- **Dissertação**
  - [Modelo que faz uso da classe anTeX2 para dissertação de mestrado](dissertacao)

## Utilização

- Instalar o pacote `latexmk` e o `texlive`
```shell
$ sudo apt-get install latexmk texlive-full 
```
- Compilar os projetos
```bash
latexmk -outdir=out -pdf apresentacao/titulo-leve/titulo-leve.tex
```
> Também é possível exportar os modelos e compilar diretamente no [overleaf](https://pt.overleaf.com/). :leaves:

## Extensões recomendadas para o vscode

Estes modelos funcionam bem no vscode utilizando as seguintes extensões:

- [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- [bibtexLanguage](https://marketplace.visualstudio.com/items?itemName=phr0s.bib)
- [Brazilian Portuguese - Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-portuguese-brazilian)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

> A extensão [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) usa por padrão o latexmk para compilar.



## Créditos

:warning: Este repositório e seus respectivos modelos/classes são **fortemente** baseados nos modelos criados pelo professor [Emerson Ribeiro de Mello](https://github.com/emersonmello) para o Instituto Federal de Santa Catarina. Todos os créditos das criações de modelos/apresentações vão para ele.

