from youtube_transcript_api import YouTubeTranscriptApi
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
import dotenv
import os

Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small", embed_batch_size=100
)

# Load documents from the specified directory
documents = SimpleDirectoryReader('./data-transcript').load_data()

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

def reply(query):
    response = query_engine.query(query)
    print('reply', response)
    return response
