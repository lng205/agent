import chromadb
chroma_client = chromadb.PersistentClient(path="database_lg")

# Embedding function
API_KEY = "YOUR_API_KEY"
openai_ef = chromadb.utils.embedding_functions.OpenAIEmbeddingFunction(api_key=API_KEY, model_name="text-embedding-3-large")

def create_collection():
    collection = chroma_client.create_collection(name="memory", embedding_function=openai_ef)
    collection.add(
        documents=[
            "The master mentioned preferring coffee over tea in the mornings.",
            "The master expressed a fondness for jazz music last Thursday evening.",
            "The master revealed a dislike for cold weather during a conversation on Wednesday.",
            "The master shared a memorable story about hiking in the mountains during our chat yesterday.",
            "The master stated that the science fiction genre is their favorite for movies.",
            "A new set of green ceramic pots appeared on the kitchen shelf this Monday.",
            "There's a fresh stain on the living room carpet, noticed on Tuesday afternoon.",
            "The master brought in a large, leafy plant for the office corner on the weekend.",
            "Noticed a pile of unread mail accumulating on the hallway table since last Friday.",
            "The wall in the dining area has been repainted to a light lavender shade as of yesterday.",
            "The master seemed particularly cheerful after receiving a phone call on Saturday morning.",
            "The master completed assembling a wooden bookshelf for the study room this Sunday.",
            "The master appeared frustrated with a malfunctioning kitchen appliance during breakfast today.",
            "Observed the master practicing guitar for an upcoming family gathering next weekend.",
            "The master spent the evening organizing old photographs into albums last night."
            ],
        ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12","13","14","15"]
    )


# create_collection()
collection = chroma_client.get_collection(name="memory", embedding_function=openai_ef)
results = collection.query(
    query_texts=["Would master want oolong or latte?"],
    n_results=3
)

print(results)
