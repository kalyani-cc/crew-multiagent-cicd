from crewai import Crew

from agents import (
    research_agent,
    analysis_agent,
    writer_agent
)

from tasks import (
    research_task,
    analysis_task,
    writer_task
)

crew = Crew(
    agents=[
        research_agent,
        analysis_agent,
        writer_agent
    ],

    tasks=[
        research_task,
        analysis_task,
        writer_task
    ],

    verbose=True
)