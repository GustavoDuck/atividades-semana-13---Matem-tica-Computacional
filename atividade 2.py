def calcular_idades():
    try:
        # Coletar idades dos usuários
        idade1_homem = int(input("Informe a idade do primeiro homem: "))
        idade2_homem = int(input("Informe a idade do segundo homem: "))
        idade1_mulher = int(input("Informe a idade da primeira mulher: "))
        idade2_mulher = int(input("Informe a idade da segunda mulher: "))

        # Verificação se as idades são válidas
        if idade1_homem <= 0 or idade2_homem <= 0 or idade1_mulher <= 0 or idade2_mulher <= 0:
            print("Erro: As idades devem ser números inteiros positivos.")
            return

        # Determinando as idades máximas e mínimas
        homem_mais_velho = max(idade1_homem, idade2_homem)
        homem_mais_novo = min(idade1_homem, idade2_homem)
        mulher_mais_velha = max(idade1_mulher, idade2_mulher)
        mulher_mais_nova = min(idade1_mulher, idade2_mulher)

        # Realizando os cálculos requeridos
        soma_idades = homem_mais_velho + mulher_mais_nova
        produto_idades = homem_mais_novo * mulher_mais_velha

        # Apresentando os resultados
        print(f"A soma da idade do homem mais velho com a mulher mais nova é: {soma_idades}")
        print(f"O produto da idade do homem mais novo com a mulher mais velha é: {produto_idades}")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos inteiros válidos.")

# Executa a função
calcular_idades()
