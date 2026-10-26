
def calcular_media(notas):
    return sum(notas) / len(notas)


def situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


nome = input("Digite o nome do estudante: ")
notas = []

for i in range(4):
    while True:
        try:
            nota = float(
                input(f"Digite a {i + 1}ª nota (0 a 10): ")
            )

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Digite um valor de 0 a 10.")

        except ValueError:
            print("Entrada inválida! Digite um número.")


media = calcular_media(notas)

print("\n--- RESULTADO ACADÊMICO ---")
print("Estudante:", nome)
print(f"Média: {media:.2f}")
print("Situação:", situacao(media))
