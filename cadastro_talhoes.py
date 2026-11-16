# AgroControl - Cadastro de talhoes
# Artefato inicial do projeto (versao 1.0)

talhoes = []


def cadastrar_talhao(nome, area_ha, cultura):
    talhao = {"nome": nome, "area_ha": area_ha, "cultura": cultura}
    talhoes.append(talhao)
    return talhao


if __name__ == "__main__":
    print(cadastrar_talhao("Talhao 01", 12.5, "Soja"))

# Alteracao solicitada pelo time de operacoes (versao 1.1)
def listar_talhoes():
    for t in talhoes:
        print(t["nome"], "-", t["area_ha"], "ha -", t["cultura"])
