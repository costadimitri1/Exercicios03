# media_aprovacao.py
# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação da situação do aluno
if media >= 7:
    print(f"Aprovado com média {media:.2f}.")
elif 5 <= media < 7:
    print(f"Recuperação com média {media:.2f}.")
else:
    print(f"Reprovado com média {media:.2f}.")