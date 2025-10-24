# Projeto de Attrition

Projeto de Attrition que é capaz de prever a possibilidade de um funcionário sair de uma empresa, junto de seu percentual. Projeto feito por mim, [Pedro Henrique Sampaio](https://github.com/pedrohgravina?tab=repositories)

![imagem](imagens/imagem.jpg)

## Organização do projeto

```
├── .env               <- Arquivo de variáveis de ambiente (não versionar)
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto se uma for escolhida
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter.
│
├── imagens            <- Imagem do README                       
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|      └── models_rus   <- Script para criar DataFrames, Pipelines.. De forma a organizar melhor os dados
| 
├── referencias        <- Dicionários de dados
|
├── relatorios         <- Análises geradas em HTML, PDF, LaTeX, etc.
│   └── imagens        <- Gráficos e figuras gerados para serem usados em relatórios
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone https://github.com/pedrohgravina?tab=repositories
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o gerenciador de ambientes de sua preferência.

      ```bash
      conda env export > ambiente.yml
      ```
      
## Um pouco mais sobre a base de dados

[Clique aqui](referencias/02_dicionario_de_dados.md) para ver o dicionário de dados da base utilizada