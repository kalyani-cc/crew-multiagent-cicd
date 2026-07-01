# main.py

from scraper import scrape_website

urls = {
    "arogyadeep":
    "https://arogyadeep.shopenup.com/",

    "storefront":
    "https://storefront.shopenup.com/",

    "codecolonies":
    "https://codecolonies.com/"
}

for name, url in urls.items():

    text = scrape_website(url)

    with open(
        f"data/{name}.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)

    print(
        f"{name} saved"
    )


#Wihout LangGraph
# from vector_store import search

# result = search(
#     "What services does Code Colonies provide?"
# )

# print("\nBest Match:")
# print(result["source"])

# print("\nContent:")
# print(result["text"][:1000])

#With LangGraph

# from graph import graph;

# graph.invoke(
#     {
#         "question":
#         "which products shopenup have ?",

#         "answer":
#         ""
#     }
# )


#Crew Multi Agent

from crew_setup import crew

result = crew.kickoff()

print("\nFinal Result:\n")

print(result)