dados = []
# Deve-se popular a variavel dados com algo parecido com:
#    ["Tassio", 10, 9, 9, 9],
#    ["Tassio2", 10, 8, 8, 8],
#    ["Tassio3", 10, 7, 7, 7]
# Uma lista com uma sublista. [[]]

def buscar_candidato(dados, entrevista, teste_teorico, teste_pratico, soft_skills):
    resultado = []
    for candidato in dados:
        nome, e, t, p, s = candidato
        if e >= entrevista and t >= teste_teorico and p >= teste_pratico and s >= soft_skills:
            notas = [add_prefixo(nota, prefixo) for nota, prefixo in zip(candidato[1:], ['e', 't', 'p', 's'])]
            resultado.append([nome, '_'.join(notas)])
    return resultado

def add_prefixo(nota, prefixo):
    return f"{prefixo}{nota}"

busca = buscar_candidato(dados, 1, 1, 1, 1)
print(busca)
