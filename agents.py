from crewai import Agent, LLM
from tools import website_search

llm = LLM(
    model="ollama/llama3.2"
)

research_agent = Agent(
    role="Website Research Specialist",

    goal="Find information from websites",

    backstory="""
    Expert in searching company
    websites and extracting details.
    """,

    tools=[website_search],

    llm=llm,

    verbose=True
)

analysis_agent = Agent(
    role="Business Analyst",

    goal="Analyze business information",

    backstory="""
    Expert in understanding business
    models, services, and customer needs.
    """,

    llm=llm,

    verbose=True
)

writer_agent = Agent(
    role="Content Writer",

    goal="Create summaries",

    backstory="""
    Expert at creating clear and
    professional business summaries.
    """,

    llm=llm,

    verbose=True
)