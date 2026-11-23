# Gerenciador de Notas Escolares

Aplicativo de linha de comando feito em Python para cadastrar alunos, calcular médias e consultar a situação escolar (aprovado, em recuperação ou reprovado).

## Funcionalidades

1. Cadastrar aluno (nome e 3 notas)
2. Listar alunos com média e situação
3. Consultar a situação de um aluno pelo nome
4. Ver o aluno com a maior média
0. Sair

## Conceitos aplicados

- Funções com `def` (uma para cada funcionalidade)
- Parâmetros e argumentos (`calcular_media(notas)`, `verificar_situacao(media)`)
- Retorno de valores com `return`
- Estruturas condicionais `if`, `elif` e `else`
- Laço `while` para manter o menu em funcionamento
- `input()` e `print()` para interação com o usuário

## Como executar

```bash
python main.py
```

## Critério de situação

- Média maior ou igual a 7: Aprovado
- Média entre 5 e 6,99: Em recuperação
- Média abaixo de 5: Reprovado

## Integrantes

- Nome do aluno 1 Francisco Allyson Rafael de Freitas
- Nome do aluno 2 Caíque Alves Fernandes
