def AcharPrefixo(Prefixo1, Prefixo2):
    if Prefixo1 == Prefixo2:
        return Prefixo2

    else:
        letras1 = [char for char in Prefixo1]
        letras2 = [char for char in Prefixo2]

        prefixo = []
        i = 0

        while i < min(len(letras1), len(letras2)):
            if letras1[i] == letras2[i]:
                prefixo.append(letras1[i])
                i += 1
            else:
                break

        prefixo = "".join(prefixo)

        return prefixo


def MaiorPrefixo(strings, ini, fim):

    if ini == fim:
        return strings[ini]

    else:
        meio = (ini + fim) // 2
        Prefixo1 = MaiorPrefixo(strings, ini, meio)
        Prefixo2 = MaiorPrefixo(strings, meio + 1, fim)

    return AcharPrefixo(Prefixo1, Prefixo2)


strings = [
    'batata',
    'batatinha',
    'batalhão',
    'bater',
    'bateria',
    'batman',
    'batedeira',
    'batom',
]
print(MaiorPrefixo(lista1, 0, len(strings) - 1))
