def calcular_salario_final():
    # Solicita os valores de entrada do usuário
    salario_fixo = float(input("Digite o salário fixo do vendedor: "))
    comissao_por_carro = float(input("Digite a comissão fixa por carro vendido: "))
    total_vendas = float(input("Digite o total das vendas realizadas pelo vendedor: "))
    carros_vendidos = int(input("Digite o número de carros vendidos pelo vendedor: "))

    # Inicializa o salário final com o salário fixo
    salario_final = salario_fixo
    
    # Verifica se o vendedor vendeu pelo menos um carro
    if carros_vendidos > 0:
        # Adiciona a comissão por cada carro vendido
        salario_final += comissao_por_carro * carros_vendidos
        # Adiciona 5% do total das vendas
        salario_final += 0.05 * total_vendas
        
        # Verifica se há direito ao bônus adicional
        if carros_vendidos > 10:
            salario_final += 0.10 * total_vendas  # Bônus de 10% sobre o total das vendas
    
    # Exibe o salário final calculado
    print(f"O salário final do vendedor é: R${salario_final:.2f}")

# Chama a função para calcular o salário final
calcular_salario_final()
