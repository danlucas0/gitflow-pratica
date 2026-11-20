"""Sistema simples de cadastro de alunos."""

VERSION = "0.1.0-dev"

alunos = []


def cadastrar_aluno(nome, idade):
    """Cadastra um aluno e retorna o registro criado."""
    if not nome:
        raise ValueError("O nome e obrigatorio")
    aluno = {"nome": nome, "idade": idade}
    alunos.append(aluno)
    return aluno


def main():
    print(f"Sistema de Alunos v{VERSION}")


if __name__ == "__main__":
    main()
