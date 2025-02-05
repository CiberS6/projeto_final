# Projeto SQLite para Gerir os Picks do League of Legends

Este projeto apresenta uma aplicação baseada em SQLite para gerir dados relacionados a campeões, funções (roles) e builds no League of Legends.

## Estrutura do Projeto

A estrutura do diretório está organizada da seguinte forma:

```
sqlite_database/
├── lol.db                # Arquivo principal da base de dados SQLite
├── lol copy.db           # Cópia de segurança do banco de dados
├── lol copy 2.db         # Outra cópia de segurança do banco de dados
├── lol copy 3.db         # Outra cópia de segurança do banco de dados
src/
├── app/
│   └── main.py           # Script principal que inicializa e interage com a base de dados
├── create/
│   ├── criar_tabelas.py            # Script para criar tabelas na base de dados
│   ├── criar_tabela_temporaria.py  # Script para criar tabelas temporárias ordenadas
│   ├── inserir_builds.py           # Script para inserir dados na tabela 'builds'
│   ├── inserir_champions.py        # Script para inserir dados na tabela 'champions'
│   └── inserir_roles.py            # Script para inserir dados na tabela 'roles'
├── delete/
│   └── eliminar_champions.py      # Script para excluir registros na tabela 'champions'
├── read/
│   ├── ler_champions.py           # Script para consultar dados na tabela 'champions'
│   ├── ler_champions_ordem.py     # Script para consultar dados de campeões ordenados
│   └── ler_inner_join.py          # Script para realizar joins entre tabelas
├── update/
│   └── atualizar_champions.py     # Script para atualizar dados na tabela 'champions'
└── README.md                      # Documentação do projeto
```

## Esquema da Base de Dados

A base de dados SQLite `lol.db` consiste nas seguintes tabelas:

1. **champions**
   - `id_champion` (INTEGER, Chave Primária)
   - `nome_champion` (TEXT, Obrigatório)
   - `id_role` (INTEGER, Chave Estrangeira para a tabela `roles`)
   - `id_build` (INTEGER, Chave Estrangeira para a tabela `builds`)

2. **roles**
   - `id_role` (INTEGER, Chave Primária)
   - `nome_role` (TEXT, Obrigatório)

3. **builds**
   - `id_build` (INTEGER, Chave Primária)
   - `nome_build` (TEXT, Obrigatório)

4. **picks** (referenciada em exemplos, mas ainda não implementada no código atual)
   - `id_pick` (INTEGER, Chave Primária)
   - `id_champion` (INTEGER, Chave Estrangeira para a tabela `champions`)
   - `id_role` (INTEGER, Chave Estrangeira para a tabela `roles`)

## Funcionalidades

- **Criação de tabelas:** Cria automaticamente as tabelas `champions`, `roles` e `builds`, caso ainda não existam.
- **Inserção de dados:** Permite adicionar registros manualmente em todas as tabelas.
- **Consulta de dados:** Realiza consultas SELECT para:
  - Buscar campeões ordenados alfabeticamente.
  - Realizar joins entre tabelas para obter detalhes combinados.
  - Obter detalhes de um campeão ou role pelo nome.
  - Listar todos os campeões cadastrados.
- **Exclusão de dados:** Remove registros específicos na tabela `champions`.
- **Atualização de dados:** Atualiza campos existentes na tabela `champions`.

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
- **`criar_tabela_temporaria.py`:** Cria tabelas temporárias para ordenação e manipulação.
- **`inserir_champions.py`:** Adiciona novos campeões com seus respectivos roles e builds.
- **`eliminar_champions.py`:** Exclui registros específicos da tabela `champions`.
- **`ler_champions.py`:** Realiza consultas na tabela `champions`.
- **`ler_champions_ordem.py`:** Lista campeões em ordem alfabética.
- **`ler_inner_join.py`:** Realiza joins entre tabelas para obter informações combinadas.
- **`atualizar_champions.py`:** Atualiza registros na tabela `champions`.

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

4. Listar todos os campeões em ordem alfabética:
   ```sql
   SELECT * FROM champions ORDER BY nome_champion;
   ```

5. Realizar join para obter detalhes combinados de campeões, roles e builds:
   ```sql
   SELECT champions.id_champion, champions.nome_champion, roles.nome_role, builds.nome_build
   FROM champions
   INNER JOIN roles ON champions.id_role = roles.id_role
   INNER JOIN builds ON champions.id_build = builds.id_build;
   ```

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma *issue* ou envie um *pull request* se desejar sugerir melhorias ou adicionar novas funcionalidades.
