from crewai import Task

from agents import (
    research_agent,
    analysis_agent,
    writer_agent
)

research_task = Task(
    description="""
    Use the website_search tool to find information
    from the available company websites.

    Find:
    - Company services
    - Products
    - Technologies used
    - Business offerings

    Focus on:
    - Arogyadeep
    - Shopenup Storefront
    - Code Colonies
    """,

    expected_output="""
    Detailed research report containing
    website information and business details.
    """,

    agent=research_agent
)

analysis_task = Task(
    description="""
    Analyze the research findings.

    Identify:
    - Business model
    - Core services
    - Target customers
    - Technical offerings
    - Unique selling points

    Create a business analysis report.
    """,

    expected_output="""
    Structured business analysis report.
    """,

    agent=analysis_agent
)

writer_task = Task(
    description="""
    Create a professional summary based on
    the analysis report.

    The summary should clearly explain:
    - What the company does
    - Services offered
    - Main business focus
    """,

    expected_output="""
    Professional company summary.
    """,

    agent=writer_agent
)