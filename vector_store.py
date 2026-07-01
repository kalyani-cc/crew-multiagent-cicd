from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []

# Load documents
for file in os.listdir("data"):

    with open(
        f"data/{file}",
        encoding="utf-8"
    ) as f:

        documents.append(
            {
                "source": file,
                "text": f.read()
            }
        )

# Generate embeddings
vectors = []

for doc in documents:

    embedding = model.encode(
        doc["text"]
    )

    vectors.append(
        {
            "source": doc["source"],
            "text": doc["text"],
            "vector": embedding
        }
    )

# Search Function
def search(question):

    question_vector = model.encode(
        question
    )

    best_score = -1
    best_doc = None

    for item in vectors:

        score = cosine_similarity(
            [question_vector],
            [item["vector"]]
        )[0][0]

        if score > best_score:

            best_score = score

            best_doc = item

    return best_doc