from crewai.tools import tool
from vector_store import search

@tool
def website_search(question: str) -> str:
    """
    Search company website knowledge base.
    """

    result = search(question)

    return f"""
    Source: {result['source']}

    Content:
    {result['text']}
    """