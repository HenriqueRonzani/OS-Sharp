# Projeto Final de Programação para Engenharia  
  
## 1. Sobre
O projeto foi desenvolvido para uma avaliação final da matéria de programação para engenharia, da primeira fase da graduação de **Engenharia da Computação**.

### 1.1 O que é
O objetivo do projeto é desenvolver um software para facilitar o registro de ordens de serviço para assistências técnicas, com cadastro de funcionários, ordens de serviço, atribuição de ordens de serviço à funcionários e geração de **PDF** com duas vias, para impressão e entrega ao cliente

## 2 Regras
Foi definido que o projeto deveria ser desenvolvido em python, podendo utilizar bibliotecas para facilitar desenvolvimento de funcionalidades específicas. Além disso, não foi se pôde utilizar de qualquer modo de permanência de dados. Também, era necessário haver a manipulação de listas e dicionários e uso de funções para o gerenciamento de dados.

## 3 Desenvolvimento
Com as regras definidas, o projeto foi desenvolvido, utilizando python. Para gerar os PDFs, foi utilizada a biblioteca **ReportLab**.

## 4 Resultado
O projeto desenvolvido atendeu as requisitos solicitados, com todas funcionalidades especificadas.

## 5 Considerações
Apesar do projeto ter atendido aos objetivos específicos, a falta de possibilidade de permanência de dados, mesmo que em um arquivo sqlite, trouxe grande verbosidade ao projeto, que precisou passar todos dados como parâmetros entre as funções.  

## Necessário
Devido ao uso da biblioteca reportlab, é necessário instalá-lo.
> pip install reportlab

Após isso o app pode rodar no terminal.
