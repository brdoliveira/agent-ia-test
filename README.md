# Teste de Aplicação de Agentes de Inteligência Artificial

## Introdução

Este projeto utiliza a biblioteca `crewai` para criar agentes de inteligência artificial especializados em pesquisar eventos culturais e planejar itinerários. Ele integra a API do OpenAI, especificamente o modelo `gpt-4-1106-preview`, para processar as solicitações dos usuários e gerar respostas úteis.

## Configuração

### Pré-requisitos

- Python 3.x
- Bibliotecas: `crewai`, `python-dotenv`, `langchain_openai`

### Instalação

1. Clone o repositório para o seu ambiente local.
2. Instale as dependências necessárias usando o pip:

```bash
pip install crewai python-dotenv langchain_openai
```

### Configure suas variáveis de ambiente:
Crie um arquivo .env no diretório raiz do projeto.

### Adicione sua chave de API do OpenAI:
```bash
OPENAI_API_KEY="sua_chave_de_api_aqui"
````

## Para utilizar a aplicação:
Inicialize os agentes e as tarefas conforme definido no código.

Execute o código para iniciar a pesquisa de eventos e o planejamento de itinerários com base nos interesses e na disponibilidade do usuário.

O script criará uma equipe de agentes que trabalharão juntos para identificar eventos culturais relevantes e criar um itinerário personalizado, incluindo recomendações de transporte, acomodações e dicas locais.

## Créditos
Este projeto utiliza as seguintes bibliotecas e APIs:
- crewai: Para a criação e gerenciamento de agentes de IA.
- python-dotenv: Para o gerenciamento de variáveis de ambiente.
- langchain_openai: Para a integração com a API do OpenAI.
- API do OpenAI: Para acessar modelos de linguagem avançados e realizar tarefas de processamento de linguagem natural.
