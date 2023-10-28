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

# Esquema para una llamada de emergencia con razones de peligro
schema = {
    "properties": {
        "nombre": {"type": "string", "description": "Nombre de la persona que llama"},
        "edad": {"type": "integer", "description": "Edad de la persona que llama"},
        "ubicacion": {"type": "string", "description": "Ubicación de la emergencia"},
        "descripcion": {"type": "string", "description": "Breve descripción de la emergencia"},
        "razones_peligro": {"type": "string", "description": "Razones específicas de peligro"}
    },
    "required": ["nombre", "ubicacion", "descripcion", "razones_peligro"]
}

# Input 
inp = """Hola, mi nombre es Juan. Estoy llamando desde la calle Principal número 456. 
Necesitamos ayuda urgente. Mi esposa, María, ha perdido el conocimiento y está teniendo dificultades para respirar. 
Las razones de peligro incluyen dificultad respiratoria extrema y pérdida de conocimiento."""


# Run chain
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
chain = create_extraction_chain(schema, llm)
print(chain.run(inp))