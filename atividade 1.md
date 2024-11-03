# Cálculo do Salário de Vendedores em uma Revendedora de Carros

## Objetivo

Este projeto visa desenvolver um algoritmo para calcular o salário final dos vendedores de uma revendedora de carros, considerando um sistema de comissão que inclui um salário fixo, comissão por carro vendido e uma porcentagem sobre o total das vendas.

## Descrição do Problema

A revendedora de carros deseja automatizar o cálculo do salário de seus vendedores, levando em conta os seguintes fatores:

1. **Salário Fixo**: Cada vendedor recebe um valor fixo mensal.
2. **Comissão Fixa por Carro Vendido**: O vendedor ganha uma quantia adicional fixa para cada carro vendido.
3. **Percentual sobre o Total de Vendas**: O vendedor recebe 5% sobre o valor total das vendas que realizou.
4. **Incentivo Adicional**: Se o vendedor vender mais de 10 carros, ele recebe um bônus de 10% sobre o total das vendas.

## Regras de Negócio

O cálculo do salário final deve atender às condições especificadas na tabela abaixo:

| Número de Carros Vendidos | Salário Fixo | Comissão por Carro | 5% sobre Vendas | Bônus de 10% sobre Vendas |
|---------------------------|--------------|---------------------|-----------------|---------------------------|
| 0                         | Sim          | Não                | Não             | Não                        |
| 1 a 10                    | Sim          | Sim                | Sim             | Não                        |
| > 10                      | Sim          | Sim                | Sim             | Sim                        |

## Estrutura do Cálculo

1. **Salário Base**: O salário fixo é sempre considerado, independentemente do número de carros vendidos.
2. **Comissão**: A comissão por carro vendido é adicionada ao salário quando o número de carros vendidos é maior que zero.
3. **Percentual sobre Vendas**: Um adicional de 5% sobre o total das vendas é aplicado caso o vendedor tenha vendido ao menos um carro.
4. **Bônus Adicional**: Caso o vendedor tenha vendido mais de 10 carros, ele recebe um bônus de 10% sobre o total das vendas, além da comissão e do percentual sobre vendas.

## Como Executar o Código

1. Certifique-se de que o Python está instalado no seu sistema.
2. Execute o script no terminal ou em um ambiente de desenvolvimento que suporte Python.
3. Insira os valores solicitados (salário fixo, comissão por carro, total de vendas e número de carros vendidos) para calcular o salário final.
4. O salário final será exibido com base nas regras estabelecidas.

## Autor

Este projeto foi desenvolvido para demonstrar a lógica de cálculo salarial baseada em regras de comissão, aplicando condições e bonificações para vendedores em uma revendedora de carros.
