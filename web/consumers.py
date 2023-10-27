from channels.generic.websocket import AsyncWebsocketConsumer
from dotenv import load_dotenv
from deepgram import Deepgram

import os

load_dotenv()

class TranscriptConsumer(AsyncWebsocketConsumer):
   dg_client = Deepgram(os.getenv('DEEPGRAM_API_KEY'))

    async def connect(self):
       await self.connect_to_deepgram()
       await self.accept()

      async def receive(self, bytes_data):
       self.socket.send(bytes_data)