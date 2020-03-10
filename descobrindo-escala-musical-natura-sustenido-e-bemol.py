
acidente = ('natural', 'sustenido', 'bemol')

escalaDo = ('C', 'D', 'E', 'F', 'G', 'A', 'B', 'C')
escalaRe = ('D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D')
escalaMi = ('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E')
escalaFa = ('F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F')
escalaSol = ('G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G')
escalaLa = ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A')
escalaSi = ('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B')

escalaDoSustenido = ('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#')
escalaReSustenido = ('D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##', 'D#')
escalaMiSustenido = ('E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##', 'E#')
escalaFaSustenido = ('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#', 'F#')

print('-'*30)
acidenteEscala = str(input('[ NATURAL / SUSTENIDO / BEMOL ]: ')).lower()[0]
escala = str(input('Digite a escala: ')).lower()[0:3]

if acidenteEscala == 'n':
    while escala not in 'cdefgabc':
        escala = str(input('Escala Invalida! Digite a escala: ')).lower()[0:3]

    if escala == 'c' or escala == 'do' or escala == 'dó':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaDo[contagem]}')

    if escala == 'd':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaRe[contagem]}')

    if escala == 'e':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaMi[contagem]}')

    if escala == 'f':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaFa[contagem]}')

    if escala == 'g':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaSol[contagem]}')

    if escala == 'a':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaLa[contagem]}')

    if escala == 'b':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()} = {escalaSi[contagem]}')


if acidenteEscala == 's':
    while escala not in 'cdefgab':
        escala = str(input('Escala Invalida! Digite a escala sem acidente: ')).lower()[0:3]

    if escala == 'c':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()}# = {escalaDoSustenido[contagem]}')

    if escala == 'd':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()}# = {escalaReSustenido[contagem]}')

    if escala == 'e':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()}# = {escalaMiSustenido[contagem]}')

    if escala == 'f':
        for contagem in range(0,7):
            print(f'{contagem + 1}o GRAU DE {escala.upper()}# = {escalaFaSustenido[contagem]}')