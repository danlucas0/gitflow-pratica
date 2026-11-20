# Prática GitFlow

Projeto simples (sistema de cadastro de alunos em Python) usado para praticar o fluxo **GitFlow completo**.

## Branches

| Branch | Função |
|---|---|
| `main` | Código em produção, marcado com tags de versão |
| `develop` | Integração do desenvolvimento |
| `feature/*` | Uma branch por funcionalidade (sai e volta para `develop`) |
| `release/*` | Prepara uma versão (sai de `develop`, vai para `main` e `develop`) |
| `hotfix/*` | Correção urgente em produção (sai de `main`, vai para `main` e `develop`) |

## Fluxo realizado

1. Criação da `main` e da `develop`
2. `feature/cadastro-aluno` → merge na `develop`
3. `feature/listar-alunos` → merge na `develop`
4. `release/1.0.0` → merge na `main` e na `develop` + tag `v1.0.0`
5. Bug encontrado em produção → `hotfix/1.0.1` → merge na `main` e na `develop` + tag `v1.0.1`

## Como ver o histórico

```bash
git log --graph --oneline --all --decorate
```

## Como rodar

```bash
python app.py
```
