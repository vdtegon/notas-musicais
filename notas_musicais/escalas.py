NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tonica e uma tonalidade

    Parameters:
        tonica (str): Nota que será a tonica da escala
        tonalidade (str): Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus

    Examples:
        >>> Escalas('C', 'Maior')
        {'notas':['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': [
            'I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> Escalas('A', 'Maior')
        {'notas':['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
            'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
