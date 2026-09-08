# Calcula a media de duas notas
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")