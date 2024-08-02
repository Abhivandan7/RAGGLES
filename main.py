import os
# from groq import Groq
from dotenv import load_dotenv
from llama_index.llms.groq import Groq
# from sentence_transformers import SentenceTransformer
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
# from chromadb import PersistentClient
# from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.core.query_engine import TransformQueryEngine
# from llama_index.core.indices.query.query_transform import HyDEQueryTransform
# from llama_index.core.query_engine import
# from llama_ import ch

load_dotenv()

llm = Groq(model="llama3-70b-8192", api_key=os.environ.get("GROQ_API_KEY"))

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

Settings.llm = llm
Settings.embed_model = embed_model

docs = SimpleDirectoryReader("./data").load_data()

# db = PersistentClient("./chroma")
# chroma_collection = db.get_or_create_collection("rag_data")

# vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)

# index = VectorStoreIndex.from_vector_store(
#     vector_store=vector_store,
#     storage_context=storage_context,
#     embed_model = embed_model
# )

index = VectorStoreIndex.from_documents(
    documents=docs,
)

engine = index.as_query_engine(
    llm=llm
)
# hyde_engine = TransformQueryEngine(engine, HyDEQueryTransform(include_original=True))

def generate_response(query : str):
    response = engine.query(query)
    return response


if __name__ == "__main__":
    print(generate_response("Hi").response)






