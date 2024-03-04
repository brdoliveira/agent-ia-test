from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Define chave API
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_llm = ChatOpenAI(model_name='gpt-4-1106-preview', api_key=openai_api_key)

# Agente de Pesquisa de Eventos
agente_pesquisa_eventos = Agent(
    role='Pesquisador de Eventos Culturais',
    goal='Identificar os eventos culturais e sazonais mais relevantes com base nos interesses do usuário.',
    backstory="Você é um especialista em cultura e eventos, com amplo conhecimento sobre festivais, exposições artísticas e celebrações sazonais. Sua missão é descobrir eventos que ofereçam experiências autênticas e enriquecedoras.",
    verbose=True,
    llm=openai_llm
)

# Agente de Planejamento de Itinerários
agente_planejamento_itinerarios = Agent(
    role='Planejador de Itinerários',
    goal='Criar itinerários personalizados que integrem os eventos identificados, otimizando a experiência do usuário.',
    backstory="Com sua habilidade em logística e planejamento de viagens, você transforma a pesquisa de eventos em um itinerário detalhado, considerando localização, datas e preferências do usuário para garantir uma experiência inesquecível.",
    verbose=True,
    llm=openai_llm
)

# Tarefa para o Agente de Pesquisa de Eventos
tarefa_pesquisa_eventos = Task(
    description='''
    Identifique eventos culturais e sazonais que correspondam aos interesses e à disponibilidade do usuário delimitado entre as tags <evento></evento>. Sua resposta final deve ser uma lista de eventos recomendados, com detalhes sobre cada um, incluindo datas, localizações e uma breve descrição.
    
    <evento>
    - Disponibilidade: 25 a 30 de março de 2024
    - Eventos de interesse: Concerto de música clássica
    </evento>
    ''',
    agent=agente_pesquisa_eventos,
    expected_output="Gostaria de uma lista com tópicos"
)

# Tarefa para o Agente de Planejamento de Itinerários
tarefa_planejamento_itinerarios = Task(
    description='Com base nos eventos identificados, crie um itinerário detalhado que otimize a viagem do usuário. Inclua recomendações de transporte, acomodações e dicas locais. A resposta final deve ser um plano de viagem completo, com um cronograma diário.',
    agent=agente_planejamento_itinerarios,
    expected_output="Gostaria de uma lista com tópicos"
)

# Criando a equipe com processo sequencial
equipe = Crew(
    agents=[agente_pesquisa_eventos, agente_planejamento_itinerarios],
    tasks=[tarefa_pesquisa_eventos, tarefa_planejamento_itinerarios],
    verbose=True
)

# Iniciar o trabalho da equipe
resultado = equipe.kickoff()