# import datetime
# import json
# import openai
# import os
# import pandas as pd
# import pinecone
# import re
# from tqdm.auto import tqdm
# from typing import List, Union
# import zipfile

# # Langchain imports
# from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
# from langchain.prompts import BaseChatPromptTemplate, ChatPromptTemplate
# from langchain import SerpAPIWrapper, LLMChain
# from langchain.schema import AgentAction, AgentFinish, HumanMessage, SystemMessage
# # LLM wrapper
# from langchain.chat_models import ChatOpenAI
# from langchain import OpenAI
# # Conversational memory
# from langchain.memory import ConversationBufferWindowMemory
# # Embeddings and vectorstore
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Pinecone


# ///// PINECONE FAILED CALL
# Vectorstore Index
# index_name = 'podcasts'
# api_key = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"
# pinecone.init(api_key=api_key, environment="gcp-starter")
# pinecone.whoami()
# pinecone.list_indexes()



# Set env var OPENAI_API_KEY or load from a .env file:
import dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain
dotenv.load_dotenv()

# Schema
schema = {
    "properties": {
        "name": {"type": "string"},
        "height": {"type": "integer"},
        "hair_color": {"type": "string"},
    },
    "required": ["name", "height"],
}

# Input 
inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde."""

# Run chain
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
chain = create_extraction_chain(schema, llm)
print(chain.run(inp))