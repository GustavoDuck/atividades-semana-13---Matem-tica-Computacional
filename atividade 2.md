# Atividade 2: Cálculo de Idades - Soma e Produto Entre Homens e Mulheres

## Objetivo
Criar um algoritmo que, ao ler as idades de dois homens e duas mulheres, calcule a soma das idades do homem mais velho com a mulher mais nova, além do produto das idades do homem mais novo com a mulher mais velha.

## Descrição do Problema
Um estudo antropológico busca relacionar variáveis demográficas com regras específicas. Para o cálculo da idade total, precisamos da soma entre a idade do homem mais velho e a da mulher mais nova, e o produto entre a idade do homem mais novo e a da mulher mais velha.

## Regras de Negócio
1. O algoritmo deve identificar o homem mais velho e o homem mais novo, assim como a mulher mais velha e a mais nova, a partir das idades fornecidas.
2. A idade do homem mais velho deve ser somada com a idade da mulher mais nova.
3. A idade do homem mais novo deve ser multiplicada pela idade da mulher mais velha.

## Tabela Verdade

| Idade Homem 1 | Idade Homem 2 | Idade Mulher 1 | Idade Mulher 2 | Homem Mais Velho | Homem Mais Novo | Mulher Mais Velha | Mulher Mais Nova | Soma | Produto |
|---------------|---------------|----------------|----------------|------------------|-----------------|-------------------|------------------|------|---------|
| 30            | 25            | 20             | 22             | 30               | 25              | 22                | 20               | 50   | 500     |
| 40            | 35            | 30             | 28             | 40               | 35              | 30                | 28               | 68   | 980     |
| 50            | 45            | 33             | 30             | 50               | 45              | 33                | 30               | 80   | 1350    |
| 22            | 30            | 25             | 20             | 30               | 22              | 25                | 20               | 50   | 440     |
| 29            | 18            | 21             | 23             | 29               | 18              | 23                | 21               | 50   | 378     |
| ...           | ...           | ...            | ...            | ...              | ...             | ...               | ...              | ...  | ...     |

## Lógica do Algoritmo
1. **Entrada de Dados**: Solicita as idades de dois homens e duas mulheres.
2. **Validação de Idade**: Verifica se todas as idades são números inteiros positivos e exibe uma mensagem de erro se não forem.
3. **Determinação das Idades**:
   - Usa as funções `max()` e `min()` para encontrar o homem mais velho, o homem mais novo, a mulher mais velha e a mulher mais nova.
4. **Cálculo da Soma e do Produto**:
   - A soma é calculada entre a idade do homem mais velho e a idade da mulher mais nova.
   - O produto é calculado entre a idade do homem mais novo e a idade da mulher mais velha.
5. **Saída de Resultados**: Exibe a soma e o produto calculados.

## Exemplo de Execução
Ao executar o programa, o usuário pode entrar com as seguintes idades:
- Idade do primeiro homem: 30
- Idade do segundo homem: 25
- Idade da primeira mulher: 20
- Idade da segunda mulher: 22

O programa irá calcular e exibir:
- Soma: 30 (homem mais velho) + 20 (mulher mais nova) = 50
- Produto: 25 (homem mais novo) * 22 (mulher mais velha) = 550

## Conclusão
O algoritmo é eficiente e fornece resultados rapidamente, garantindo que as entradas sejam validadas para evitar erros. As operações básicas de cálculo são diretas, facilitando a manutenção e a compreensão do código.
