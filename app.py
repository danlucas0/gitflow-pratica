"""Sistema simples de cadastro de alunos."""

VERSION = "1.0.0"

alunos = []


def cadastrar_aluno(nome, idade):
    """Cadastra um aluno e retorna o registro criado."""
    if not nome:
        raise ValueError("O nome e obrigatorio")
    if idade < 0:
        raise ValueError("A idade nao pode ser negativa")
    aluno = {"nome": nome, "idade": idade}
    alunos.append(aluno)
    return aluno


def listar_alunos():
    """Retorna a lista de alunos em texto."""
    linhas = []
    for i, aluno in enumerate(alunos, start=1):
        linhas.append(f"{i}. {aluno['nome']} - {aluno['idade']} anos")
    return "\n".join(linhas)


def main():
    print(f"Sistema de Alunos v{VERSION}")
    cadastrar_aluno("Ana", 17)
    cadastrar_aluno("Bruno", 18)
    print(listar_alunos())


if __name__ == "__main__":
    main()
