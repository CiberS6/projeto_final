# Projeto SQLite para Gerir os Picks do League of Legends

Este projeto apresenta uma aplicação baseada em SQLite para gerir dados relacionados a campeões, funções (roles) e builds para inserir num registo de picks do League of Legends.

## Estrutura do Projeto

A estrutura do diretório está organizada da seguinte forma:

```
sqlite_database/
├── lol.db                # Arquivo principal da base de dados SQLite
src/
├── app/
│   └── main.py           # Script principal que inicializa e interage com a base de dados
├── create/
│   ├── criar_tabelas.py            # Script para criar tabelas na base de dados
│   ├── inserir_builds.py           # Script para inserir dados na tabela 'builds'
│   ├── inserir_champions.py        # Script para inserir dados na tabela 'champions'
│   ├── inserir_jogo.py             # Script para inserir dados na tabela 'jogo'
│   ├── inserir_picks.py            # Script para inserir dados na tabela 'picks'
│   └── inserir_roles.py            # Script para inserir dados na tabela 'roles'
├── delete/
│   └── eliminar_picks.py      # Script para excluir registros na tabela 'champions'
├── functions/
│   ├── menu.py                # Script para executar o menu principal
│   └── math.py                # Script para efetuar cálculos matemáticos
├── read/
│   ├── ler_builds.py              # Script para consultar dados na tabela 'builds'
│   ├── ler_champions.py           # Script para consultar dados na tabela 'champions'
│   ├── ler_inner_join.py          # Script para realizar joins entre tabelas
│   ├── ler_picks.py               # Script para consultar dados na tabela 'picks'
│   └── ler_roles.py               # Script para consultar dados na tabela 'roles'
├── update/
│   └── atualizar_picks.py     # Script para atualizar dados na tabela 'champions'
└── README.md                      # Documentação do projeto
```

## Esquema da Base de Dados

A base de dados SQLite `lol.db` consiste nas seguintes tabelas:

1. **picks**
   - `id_pick` (INTEGER, Chave Primária)
   - `nome_pick` (TEXT,Obrigatório)
   - `id_champion` (INTEGER, Chave Estrangeira para a tabela `champions`)
   - `id_role` (INTEGER, Chave Estrangeira para a tabela `roles`)
   - `id_build` (INTEGER, Chave Estrangeira para a tabela `builds`)

2. **champions**
   - `id_champion` (INTEGER, Chave Primária)
   - `nome_champion` (TEXT, Obrigatório)

3. **roles**
   - `id_role` (INTEGER, Chave Primária)
   - `nome_role` (TEXT, Obrigatório)

4. **builds**
   - `id_build` (INTEGER, Chave Primária)
   - `nome_build` (TEXT, Obrigatório)

5. **jogo**
   - `id_jogo` (INTEGER, Chave Primária)
   - `id_pick` (INTEGER, Chave Estrangeira para a tabela `picks`)
   - `kills` (INTEGER, Obrigatório)
   - `deaths` (INTEGER, Obrigatório)
   - `assists` (INTEGER, Obrigatório)
   - `vitoria_derrota` (INTEGER, Obrigatório, Limitado aos valores 0 e 1<>)


## Funcionalidades

- **Criação de tabelas:** Cria automaticamente as tabelas `picks`, `champions`, `roles` e `builds`, caso ainda não existam.
- **Inserção de dados:** Permite adicionar registros manualmente em todas as tabelas.
- **Consulta de dados:** Realiza consultas SELECT para:
  - Listar todos os picks criados.
  - Obter detalhes de um campeão ou role pelo nome.
  - Realizar joins entre tabelas para obter detalhes combinados.
  - Listar todos os campeões cadastrados.
- **Exclusão de dados:** Remove registros específicos na tabela `picks`.
- **Atualização de dados:** Atualiza campos existentes na tabela `picks`.

## Utilização

### Pré-requisitos

- Python 3.x instalado no sistema.
- Módulo SQLite3 (incluído por padrão na maioria das distribuições Python).

### Passos para Executar

1. Clone este repositório ou copie os ficheiros para o seu computador local.
2. Navegue até o diretório do projeto.
3. Execute o script principal para interagir com a base de dados:

   ```bash
   python src/app/main.py
   ```

### Scripts Individuais

- **`criar_tabelas.py`:** Cria as tabelas principais na base de dados.
- **`inserir_builds.py`:** Adiciona novas builds.
- **`inserir_champions.py`:** Adiciona novos campeões.
- **`inserir_picks.py`:** Adiciona novos picks com campeões, roles e builds
- **`inserir_roles.py`:** Adiciona novos roles.
- **`eliminar_picks.py`:** Exclui registros específicos da tabela `picks`.
- **`ler_builds.py`:** Realiza consultas na tabela `builds`.
- **`ler_champions.py`:** Realiza consultas na tabela `champions`.
- **`ler_inner_join.py`:** Realiza joins entre tabelas para obter informações combinadas.
- **`ler_picks.py`:** Realiza consultas na tabela `picks`.
- **`ler_roles.py`:** Realiza consultas na tabela `roles`.
- **`atualizar_picks.py`:** Atualiza os registos na tabela `picks`.



## Exemplos de Consultas

Abaixo estão exemplos de consultas realizadas pelos scripts:

1. Buscar todos os picks para um campeão específico (`id_champion = 1`):
   ```sql
   SELECT id_pick, id_champion, id_role FROM picks WHERE id_champion = 1;
   ```

2. Obter detalhes de um campeão pelo nome (`nome_champion = "Akali"`):
   ```sql
   SELECT id_champion, nome_champion FROM champions WHERE nome_champion = "Akali";
   ```

3. Obter detalhes de uma função pelo nome (`nome_role = "Mid"`):
   ```sql
   SELECT id_role, nome_role FROM roles WHERE nome_role = "Mid";
   ```

4. Realizar join para obter detalhes combinados de campeões, roles e builds:
   ```sql
   SELECT picks.nome_pick, champions.nome_champion, roles.nome_role, builds.nome_build
   FROM picks
   INNER JOIN champions ON picks.id_champion = champions.id_champion
   INNER JOIN roles ON picks.id_roles = roles.id_role
   INNER JOIN builds ON picks.id_builds = builds.id_build
   ```

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma *issue* ou envie um *pull request* se desejar sugerir melhorias ou adicionar novas funcionalidades.
